#!/usr/bin/env python3
"""
Download Monitor & Temp File Sharer for Gemini Control Skill.

Usage:
    python download_and_share.py [filepath]
    python download_and_share.py --watch [download_dir]

If a filepath is given, uploads that file directly.
If --watch is given, monitors the download directory for the newest file,
waits for download completion, then uploads it.
If no arguments, auto-detects the default download directory and watches it.

Uploads to 0x0.st (no API key needed). Falls back to file.io if 0x0.st fails.
"""

import os
import sys
import time
import glob
import subprocess
import platform
import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError
import mimetypes


# ─── Configuration ──────────────────────────────────────────────────────────

POLL_INTERVAL = 2          # seconds between file size checks
STABLE_CHECKS = 3          # consecutive same-size checks = download complete
MAX_WAIT_TIME = 600        # max seconds to wait for download (10 min)
FILE_RECENCY_WINDOW = 120  # only consider files modified in last N seconds

UPLOAD_SERVICES = [
    {
        "name": "0x0.st",
        "url": "https://0x0.st",
        "method": "curl",
        "max_size_mb": 512,
    },
    {
        "name": "file.io",
        "url": "https://file.io",
        "method": "curl",
        "max_size_mb": 100,
    },
    {
        "name": "tmpfiles.org",
        "url": "https://tmpfiles.org/api/v1/upload",
        "method": "curl",
        "max_size_mb": 100,
    },
]


# ─── Download Directory Detection ──────────────────────────────────────────

def get_default_download_dir() -> str:
    """Get the default downloads directory for the current OS."""
    system = platform.system()

    if system == "Windows":
        # Try the known Windows download folder
        download_dir = os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
        if os.path.isdir(download_dir):
            return download_dir
        # Fallback: use shell folder registry
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
            )
            download_dir = winreg.QueryValueEx(key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]
            download_dir = os.path.expandvars(download_dir)
            winreg.CloseKey(key)
            return download_dir
        except Exception:
            pass

    elif system == "Darwin":  # macOS
        return os.path.expanduser("~/Downloads")

    elif system == "Linux":
        # Try XDG
        try:
            result = subprocess.run(
                ["xdg-user-dir", "DOWNLOAD"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except Exception:
            pass
        return os.path.expanduser("~/Downloads")

    return os.path.expanduser("~/Downloads")


# ─── File Monitoring ───────────────────────────────────────────────────────

def get_newest_file(directory: str, recency_window: int = FILE_RECENCY_WINDOW) -> str | None:
    """Find the most recently modified file in the directory within the recency window."""
    now = time.time()
    newest_file = None
    newest_mtime = 0

    try:
        for entry in os.scandir(directory):
            if not entry.is_file():
                continue
            # Skip partial download files
            name = entry.name.lower()
            if name.endswith((".crdownload", ".part", ".tmp", ".download", ".partial")):
                continue

            stat = entry.stat()
            age = now - stat.st_mtime
            if age <= recency_window and stat.st_mtime > newest_mtime and stat.st_size > 0:
                newest_mtime = stat.st_mtime
                newest_file = entry.path
    except PermissionError:
        print(f"[ERROR] Permission denied: {directory}", file=sys.stderr)
        return None

    return newest_file


def wait_for_new_file(directory: str, timeout: int = MAX_WAIT_TIME) -> str | None:
    """Watch a directory for a new file to appear and return its path."""
    print(f"[WATCH] Monitoring {directory} for new downloads...")

    # Get existing files snapshot
    existing_files = set()
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                existing_files.add(entry.path)
    except PermissionError:
        print(f"[ERROR] Permission denied: {directory}", file=sys.stderr)
        return None

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            for entry in os.scandir(directory):
                if entry.is_file() and entry.path not in existing_files:
                    name = entry.name.lower()
                    # Found a new file (skip partial downloads)
                    if not name.endswith((".crdownload", ".part", ".tmp", ".download", ".partial")):
                        print(f"[FOUND] New file: {entry.name}")
                        return entry.path

                    # If it's a partial download, wait for it to finish
                    print(f"[WAIT] Download in progress: {entry.name}")
        except PermissionError:
            pass

        time.sleep(POLL_INTERVAL)

    print("[TIMEOUT] No new file detected within timeout.", file=sys.stderr)
    return None


def wait_for_download_complete(filepath: str, timeout: int = MAX_WAIT_TIME) -> bool:
    """Wait until a file's size stabilizes (download complete)."""
    print(f"[WAIT] Waiting for download to complete: {os.path.basename(filepath)}")

    start_time = time.time()
    stable_count = 0
    last_size = -1

    while time.time() - start_time < timeout:
        try:
            if not os.path.exists(filepath):
                # File might not exist yet, or was renamed
                time.sleep(POLL_INTERVAL)
                continue

            current_size = os.path.getsize(filepath)

            if current_size == last_size and current_size > 0:
                stable_count += 1
                if stable_count >= STABLE_CHECKS:
                    print(f"[DONE] Download complete: {os.path.basename(filepath)} ({format_size(current_size)})")
                    return True
            else:
                stable_count = 0
                if current_size > 0:
                    print(f"[PROGRESS] Size: {format_size(current_size)}...")

            last_size = current_size

        except (OSError, PermissionError):
            pass

        time.sleep(POLL_INTERVAL)

    print("[TIMEOUT] Download did not complete within timeout.", file=sys.stderr)
    return False


# Also check for .crdownload / .part companion files
def wait_for_download_complete_smart(filepath: str, timeout: int = MAX_WAIT_TIME) -> str | None:
    """
    Smart download wait — handles Chrome's .crdownload pattern.
    Returns the final filepath (which may differ from the partial path).
    """
    directory = os.path.dirname(filepath)
    basename = os.path.basename(filepath)

    # Check if this IS a partial file
    partial_extensions = (".crdownload", ".part", ".tmp", ".download", ".partial")
    is_partial = basename.lower().endswith(partial_extensions)

    if is_partial:
        # Wait for the partial file to be renamed to its final name
        expected_final = filepath
        for ext in partial_extensions:
            if expected_final.lower().endswith(ext):
                expected_final = expected_final[: -len(ext)]
                break

        print(f"[WAIT] Partial download detected, waiting for: {os.path.basename(expected_final)}")
        start_time = time.time()
        while time.time() - start_time < timeout:
            if os.path.exists(expected_final) and os.path.getsize(expected_final) > 0:
                # Final file appeared, verify it's stable
                if wait_for_download_complete(expected_final, timeout=30):
                    return expected_final
            time.sleep(POLL_INTERVAL)

        print("[TIMEOUT] Partial download never completed.", file=sys.stderr)
        return None

    # Normal file — wait for size to stabilize
    if wait_for_download_complete(filepath, timeout):
        return filepath
    return None


# ─── File Upload ───────────────────────────────────────────────────────────

def upload_file(filepath: str) -> str | None:
    """Upload a file to a temp file sharing service. Returns the shareable URL."""
    file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
    filename = os.path.basename(filepath)

    for service in UPLOAD_SERVICES:
        if file_size_mb > service["max_size_mb"]:
            print(f"[SKIP] {service['name']}: file too large ({file_size_mb:.1f}MB > {service['max_size_mb']}MB)")
            continue

        print(f"[UPLOAD] Uploading {filename} ({file_size_mb:.1f}MB) to {service['name']}...")

        try:
            url = upload_to_service(filepath, service)
            if url:
                print(f"[SUCCESS] Uploaded to {service['name']}")
                return url
        except Exception as e:
            print(f"[FAIL] {service['name']} failed: {e}", file=sys.stderr)
            continue

    print("[ERROR] All upload services failed.", file=sys.stderr)
    return None


def upload_to_service(filepath: str, service: dict) -> str | None:
    """Upload a file to a specific service using curl."""
    name = service["name"]
    url = service["url"]

    if name == "0x0.st":
        result = subprocess.run(
            ["curl", "-s", "-F", f"file=@{filepath}", url],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0 and result.stdout.strip().startswith("http"):
            return result.stdout.strip()
        return None

    elif name == "file.io":
        result = subprocess.run(
            ["curl", "-s", "-F", f"file=@{filepath}", url],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                if data.get("success"):
                    return data.get("link")
            except json.JSONDecodeError:
                pass
        return None

    elif name == "tmpfiles.org":
        result = subprocess.run(
            ["curl", "-s", "-F", f"file=@{filepath}", url],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                if data.get("status") == "success":
                    return data.get("data", {}).get("url")
            except json.JSONDecodeError:
                pass
        return None

    return None


# ─── Utility ───────────────────────────────────────────────────────────────

def format_size(size_bytes: int) -> str:
    """Format file size in human-readable form."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


# ─── Main ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Download monitor & temp file sharer for Gemini Control Skill"
    )
    parser.add_argument(
        "filepath",
        nargs="?",
        help="Path to the file to upload. If omitted, watches the download directory."
    )
    parser.add_argument(
        "--watch", "-w",
        nargs="?",
        const="auto",
        default=None,
        help="Watch a directory for new downloads. 'auto' uses default Downloads dir."
    )
    parser.add_argument(
        "--newest", "-n",
        action="store_true",
        help="Upload the newest file in the download directory."
    )

    args = parser.parse_args()

    # Mode 1: Direct file upload
    if args.filepath and not args.watch:
        filepath = os.path.abspath(args.filepath)
        if not os.path.exists(filepath):
            print(f"[ERROR] File not found: {filepath}", file=sys.stderr)
            sys.exit(1)

        # Wait for download to complete if it's still in progress
        final_path = wait_for_download_complete_smart(filepath)
        if not final_path:
            print("[ERROR] File download did not complete.", file=sys.stderr)
            sys.exit(1)

        url = upload_file(final_path)
        if url:
            print(f"\n{'='*60}")
            print(f"✅ Upload successful!")
            print(f"📁 File: {os.path.basename(final_path)}")
            print(f"📦 Size: {format_size(os.path.getsize(final_path))}")
            print(f"🔗 URL:  {url}")
            print(f"{'='*60}")
        else:
            print("[ERROR] Upload failed.", file=sys.stderr)
            sys.exit(1)
        return

    # Mode 2: Watch for new downloads
    if args.watch:
        watch_dir = get_default_download_dir() if args.watch == "auto" else args.watch
        if not os.path.isdir(watch_dir):
            print(f"[ERROR] Directory not found: {watch_dir}", file=sys.stderr)
            sys.exit(1)

        new_file = wait_for_new_file(watch_dir)
        if not new_file:
            sys.exit(1)

        final_path = wait_for_download_complete_smart(new_file)
        if not final_path:
            print("[ERROR] Download did not complete.", file=sys.stderr)
            sys.exit(1)

        url = upload_file(final_path)
        if url:
            print(f"\n{'='*60}")
            print(f"✅ Upload successful!")
            print(f"📁 File: {os.path.basename(final_path)}")
            print(f"📦 Size: {format_size(os.path.getsize(final_path))}")
            print(f"🔗 URL:  {url}")
            print(f"{'='*60}")
        else:
            sys.exit(1)
        return

    # Mode 3: Upload newest file in downloads
    if args.newest:
        dl_dir = get_default_download_dir()
        newest = get_newest_file(dl_dir, recency_window=300)  # 5 min window
        if not newest:
            print(f"[ERROR] No recent files found in {dl_dir}", file=sys.stderr)
            sys.exit(1)

        url = upload_file(newest)
        if url:
            print(f"\n{'='*60}")
            print(f"✅ Upload successful!")
            print(f"📁 File: {os.path.basename(newest)}")
            print(f"📦 Size: {format_size(os.path.getsize(newest))}")
            print(f"🔗 URL:  {url}")
            print(f"{'='*60}")
        else:
            sys.exit(1)
        return

    # Default: watch default downloads directory
    dl_dir = get_default_download_dir()
    print(f"[INFO] No file specified. Watching default downloads: {dl_dir}")
    print(f"[INFO] Trigger a download in Gemini, and this script will detect and upload it.\n")

    new_file = wait_for_new_file(dl_dir)
    if not new_file:
        sys.exit(1)

    final_path = wait_for_download_complete_smart(new_file)
    if not final_path:
        sys.exit(1)

    url = upload_file(final_path)
    if url:
        print(f"\n{'='*60}")
        print(f"✅ Upload successful!")
        print(f"📁 File: {os.path.basename(final_path)}")
        print(f"📦 Size: {format_size(os.path.getsize(final_path))}")
        print(f"🔗 URL:  {url}")
        print(f"{'='*60}")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
