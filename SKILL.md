---
name: gemini-web-controller
description: >
  Full browser automation skill for Google Gemini (gemini.google.com/app).
  Handles image generation (Nano Banana 2 / Pro), video creation (Veo),
  music generation (Lyria), and deep research — with humanoid anti-bot
  behavior, optional style/template selection, and automatic media download
  + temp file sharing.
version: 1.0.0
author: SP JaYY
platforms: [windows, macos, linux]
tags: [browser, gemini, image-gen, video, music, automation]
---

# Gemini Web Interface Controller

You are controlling the Google Gemini web interface at `https://gemini.google.com/app` through a browser. Follow these instructions precisely. The user is already logged into their Google account.

---

## 0. CRITICAL — Humanoid Behavior Rules

**ALL interactions MUST appear human to avoid bot detection.** Violating these rules will cause the session to be flagged.

### Mouse Movement
- **NEVER** teleport the cursor instantly to a target element.
- Move the mouse in a natural **bezier curve** path from its current position to the target.
- Add slight random **overshoot** (2-5px past the target, then correct).
- Vary movement speed: faster for long distances, slower as you approach the target.

### Typing
- Type each character with a **random delay of 80–180ms** between keystrokes.
- Every 5–12 characters, insert a **brief pause** of 300–600ms (simulating thinking).
- Occasionally (1 in 30 chars), type a wrong character, wait 200ms, press Backspace, wait 150ms, then type the correct one.
- Never paste text directly from clipboard into the prompt input.

### Clicking
- After the mouse arrives at the target, wait a **random 200–800ms** before clicking.
- Use a natural mouse-down → pause (50-120ms) → mouse-up pattern, not an instant click.

### Scrolling
- Scroll with **variable speed** — not a fixed number of pixels.
- Add small **overshoots** when scrolling to a target, then correct.

### Between Actions
- Insert **random idle pauses** of 500–2000ms between distinct actions (e.g., after selecting a tool, before typing).
- Never execute a rapid-fire sequence of actions without pauses.

---

## 1. Navigation & Initialization

### 1.1 Open Gemini
1. Navigate to `https://gemini.google.com/app`
2. Wait for the page to fully load — look for the text "Ask Gemini" or the prompt input area.
3. If you see a "Welcome to Gemini" banner, dismiss it by clicking the `×` close button.

### 1.2 Verify Login State
- The page should show a user avatar/initial in the top-right corner.
- If you see a "Sign in" button instead, STOP and notify the user: "Not logged in to Google. Please log in first."

### 1.3 Start a Fresh Chat
- If there's an existing conversation on screen, click the **"New chat"** button (pencil/edit icon in the top-left sidebar area) to start fresh.
- Wait 500-1000ms for the new chat to initialize.

---

## 2. Model Selection

The model selector is located on the **right side** of the input area, showing the current model name with a dropdown arrow (e.g., "Thinking ∨").

### Available Models
| UI Label | Internal Engine | Notes |
|----------|----------------|-------|
| **Fast** | Nano Banana 2 | Quick responses, basic image gen, music ≤30s |
| **Thinking** | Nano Banana Pro | High-quality image gen, required for video, music up to 3min |
| **Pro** | Gemini 2.0 Pro | NOT available on free accounts — do not select |

### How to Switch Models
1. Take a snapshot to identify the current model label.
2. Look for a button with text "Fast", "Thinking", or containing the word — this is the **mode picker button** (aria-label: `Open mode picker`).
3. If the desired model is already selected, skip switching.
4. Click the mode picker button (with humanoid mouse movement + delay).
5. A dropdown/popover appears with options: **Fast**, **Thinking**, **Pro**.
6. Each option shows:
   - **Fast** — "Answers quickly"
   - **Thinking** — "Solves complex problems"  
   - **Pro** — "Advanced math and code with 3.1 Pro"
7. Click the desired model option (with humanoid behavior).
8. Wait 500ms for the UI to update.
9. Verify the model picker button now shows the new model name.

### Model Decision Rules

```
FOR IMAGE GENERATION:
  → If user says "high quality", "detailed", "pro quality", "best quality"
      → Select THINKING (Nano Banana Pro)
  → Otherwise
      → Select FAST (Nano Banana 2) — default

FOR VIDEO CREATION:
  → ALWAYS select THINKING — no exceptions

FOR MUSIC GENERATION:
  → If user says "long", "full song", "extended", "3 minutes", "high quality"
      → Select THINKING (~3 min output, higher quality)
  → Otherwise
      → Select FAST (~30s max output)

FOR DEEP RESEARCH:
  → Keep whatever model is currently selected (Thinking recommended)
```

---

## 3. Tool / Mode Selection

### 3.1 Opening the Tools Menu
1. Find the **"Tools"** button — located in the bottom input bar area, has an icon with adjustment sliders.
   - Look for: button with text "Tools" or aria-label "Tools"
2. Click it (humanoid behavior).
3. A dropdown menu appears with these options:
   - **Create image** (may show "New" badge)
   - **Canvas**
   - **Deep research**
   - **Create video**
   - **Create music**
   - **Guided learning**
   - Plus experimental features section at the bottom

### 3.2 Selecting a Tool
1. From the dropdown, click the appropriate option based on user's intent.
2. After clicking, the dropdown closes and the selected tool appears as a **tag/chip** in the input area (e.g., "🖼 Create image ×").
3. The prompt placeholder text changes:
   - Image: "Describe the image you want to create"
   - Video: "Describe the video you want to create"  
   - Music: "Describe your track"
   - Deep research: standard prompt
4. Wait 500-1000ms for the UI to fully update.

### 3.3 Clearing a Previously Selected Tool
If a tool is already active and you need to switch:
1. Look for the **"×" (deselect)** button next to the active tool tag in the input area.
2. Click it to deselect the current tool.
3. Wait 500ms.
4. Then open Tools menu and select the new tool.

---

## 4. Style / Template / Track Selection

> ⚠️ **THIS STEP IS OPTIONAL.** Only select a style/template/track if you are **confident** the user's prompt explicitly asks for it. Do NOT force a match. When in doubt, skip this step entirely and let Gemini choose the default.

### 4.1 When a Tool is Selected — Style Grid Appears

After selecting "Create image", "Create video", or "Create music", a **grid of visual cards** appears above the prompt input:

#### Image Styles — "Pick a style for your image"
| Style Name | Keywords that trigger selection |
|-----------|-------------------------------|
| Monochrome | "monochrome", "black and white", "b&w", "grayscale", "noir" |
| Color block | "color block", "pop art", "flat color", "bold colors" |
| Runway | "runway", "fashion", "editorial" |
| Anyma's world | "anyma", "digital art", "futuristic abstract" |
| Risograph | "risograph", "riso", "print style", "textured print" |
| Technicolor | "technicolor", "vintage color", "retro film" |
| Gothic clay | "gothic", "clay", "sculpted", "dark clay" |
| Dynamite | "dynamite", "explosive", "action", "dynamic" |
| Salon | "salon", "elegant", "classical painting" |
| Sketch | "sketch", "pencil", "drawing", "hand-drawn", "line art" |
| Cinematic | "cinematic", "movie still", "film", "dramatic lighting" |
| Steampunk | "steampunk", "victorian", "mechanical", "gears" |

#### Video Templates — "Pick a template to create a video"
| Template Name | Keywords that trigger selection |
|--------------|-------------------------------|
| Civilization | "civilization", "ancient", "historical", "epic" |
| Metallic | "metallic", "chrome", "metal", "shiny" |
| Memo | "memo", "retro", "vintage", "old footage", "vhs" |
| Glam | "glam", "glamorous", "sparkle", "luxury" |
| Crochet | "crochet", "knit", "fabric", "textile", "yarn" |
| Cyberpunk | "cyberpunk", "cyber", "neon", "futuristic city" |
| Video Game | "video game", "game", "pixel", "8-bit", "retro game" |
| Cosmos | "cosmos", "space", "galaxy", "stars", "universe" |
| Action Hero | "action hero", "superhero", "action movie" |
| Stardust | "stardust", "magical", "fairy dust", "sparkles" |
| Jellytoon | "jellytoon", "cartoon", "animated", "jelly" |
| Racetrack | "racetrack", "racing", "cars", "speed" |

#### Music Tracks — "Pick a track to remix"
| Track Name | Keywords that trigger selection |
|-----------|-------------------------------|
| 90's rap | "90s rap", "hip hop", "old school rap", "boom bap" |
| Latin pop | "latin", "latin pop", "reggaeton pop", "spanish" |
| Folk ballad | "folk", "ballad", "acoustic", "folk song" |
| 8-bit | "8-bit", "chiptune", "retro game", "pixel music" |
| Workout | "workout", "gym", "exercise", "energetic", "pump up" |
| Reggaeton | "reggaeton", "perreo", "latin beat", "dembow" |
| R&B romance | "r&b", "rnb", "romance", "slow jam", "love song" |
| Kawaii metal | "kawaii", "kawaii metal", "j-metal", "cute metal" |
| Cinematic | "cinematic", "film score", "orchestral", "epic music" |
| Emo | "emo", "emo rock", "emotional", "angsty" |
| Afropop | "afropop", "afrobeats", "african pop" |
| Forest bath | "forest", "nature", "ambient", "peaceful", "zen", "meditation" |
| K-pop | "kpop", "k-pop", "korean pop" |
| Birthday roast | "birthday", "roast", "funny", "comedy" |
| Folk a cappella | "a cappella", "acapella", "vocal only" |
| Bad music | "bad music", "intentionally bad", "joke" |

### 4.2 How to Select a Style/Template/Track
1. Scan the user's prompt for any keywords from the tables above.
2. **Confidence check:**
   - **HIGH confidence** (direct keyword match) → select it
   - **MEDIUM confidence** (strong synonym) → select it
   - **LOW confidence** (vague or ambiguous) → DO NOT select, skip this step
3. If selecting: find the card with the matching text label in the style grid.
4. Click the card (humanoid mouse movement).
5. The card will appear highlighted/selected.
6. Wait 300-500ms.

### 4.3 Scrolling to Find Styles
- The style grid may require scrolling to see all options.
- If the target style is not visible, scroll down within the style grid area (smooth humanoid scrolling).
- Some tracks (like K-pop, Birthday roast, Folk a cappella, Bad music) are at the bottom and will need scrolling.

---

## 5. Prompt Entry

### 5.1 Focus the Input
1. Find the prompt input area:
   - It's a `contenteditable` div, NOT a standard `<input>`.
   - Look for: `div[aria-label="Enter a prompt for Gemini"]` or placeholder text "Ask Gemini" / "Describe the image you want to create" / "Describe the video you want to create" / "Describe your track"
2. Click on the input area (humanoid behavior) to focus it.
3. Wait 200-400ms.

### 5.2 Type the Prompt
1. Type the user's prompt text using **humanoid typing behavior** (see Section 0):
   - 80-180ms between characters
   - Occasional pauses every 5-12 chars
   - Rare typo-and-correct sequences
2. **IMPORTANT:** Do NOT strip style keywords from the prompt. Send the full prompt as-is. The style selection is separate from the prompt text.
3. After typing is complete, wait 300-500ms.

---

## 6. Submit & Wait for Generation

### 6.1 Submit the Prompt
1. Press the **Enter** key to submit the prompt.
   - Alternative: Click the **send button** (arrow icon) if visible.
2. The prompt will be sent and the UI will show a loading/generation state.

### 6.2 Wait for Generation to Complete

Different modes have different generation times:

| Mode | Typical Wait | Max Wait |
|------|-------------|----------|
| Image | 10-30 seconds | 2 minutes |
| Video | 30-120 seconds | 5 minutes |
| Music | 15-60 seconds | 3 minutes |
| Deep Research | 2-10 minutes | 15 minutes |

**How to detect completion:**
1. **Look for loading indicators** — spinning animations, "Generating...", progress bars, thinking dots.
2. **Poll every 3-5 seconds** by taking a snapshot and checking for:
   - Generated image(s) appearing in the chat
   - A video player/thumbnail appearing
   - A music audio player appearing
   - A deep research report with text appearing
3. **Completion signals:**
   - For images: image cards with download/share buttons appear
   - For video: video player with play button appears
   - For music: audio player with play/download buttons appears
   - For deep research: full text report with bullet points appears
4. If generation seems stuck beyond the max wait time, notify the user: "Generation appears to be taking longer than expected. Still waiting..."

### 6.3 Handle Generation Errors
- If you see "Something went wrong" or error messages, report them to the user.
- If rate-limited ("You've reached the limit"), inform the user and suggest waiting.
- If content was blocked ("I can't generate that"), inform the user about the content policy.

---

## 7. Download Generated Media

### 7.1 Locate the Download Button
After generation completes:

1. **For Images:**
   - Look for a **download icon** (⬇ or similar) on the generated image card.
   - May also be accessible via a "..." (more options) menu on the image.
   - Right-click context menu may also have "Save image as..."

2. **For Video:**
   - Look for a **download button** below the video player.
   - May appear after clicking on the video or hovering over it.

3. **For Music:**
   - Look for a **download icon** near the audio player controls.
   - May export as MP3 or video file.

### 7.2 Click Download
1. Click the download button (humanoid behavior).
2. If a "Save As" dialog appears, accept the default filename and location.
3. **CRITICAL: Wait for the download to fully complete.**
   - Monitor the browser's download state.
   - Check if the file exists in the download directory and its size has stabilized (not growing).
   - Poll every 2 seconds: check file size, wait, check again. If sizes match, download is done.
   - Typical download times:
     - Images: 1-5 seconds
     - Video: 5-30 seconds
     - Music: 2-10 seconds

### 7.3 Verify Download
1. Confirm the file exists at the download location.
2. Confirm the file is not zero-bytes.
3. Note the full file path for the sharing step.

---

## 8. Share Downloaded Media

After the file is fully downloaded, share it with the user via a temporary file hosting service.

### 8.1 Upload to Temp File Host
Use the `scripts/download_and_share.py` helper script:

```bash
python scripts/download_and_share.py "<full_path_to_downloaded_file>"
```

This script will:
1. Find the most recently downloaded file (or use the specified path)
2. Upload it to `0x0.st` (no API key needed)
3. Print the shareable URL

### 8.2 Alternative — Manual Upload
If the script is unavailable, you can upload directly:

```bash
curl -F "file=@<filepath>" https://0x0.st
```

### 8.3 Report to User
Return the shareable URL to the user:
```
✅ Generation complete!
📁 File: <filename>
🔗 Download: <shareable_url>
⏰ Link expires based on file size (smaller files stay longer)
```

---

## 9. Error Handling & Recovery

### Common Issues

| Issue | Detection | Recovery |
|-------|----------|----------|
| **Not logged in** | "Sign in" button visible | Stop, ask user to log in |
| **CAPTCHA** | CAPTCHA challenge appears | Stop, ask user to solve manually |
| **Rate limited** | "You've reached the limit" message | Wait 1-5 minutes, retry |
| **Content blocked** | "I can't generate that" | Report to user, suggest prompt change |
| **Generation timeout** | No result after max wait | Retry once, then report failure |
| **Download failed** | 0-byte file or no file found | Retry download, check permissions |
| **Upload failed** | No URL returned from 0x0.st | Try alternative: `file.io` or `tmpfiles.org` |
| **Element not found** | Expected UI element missing | Take screenshot, try alternative selectors |
| **Model unavailable** | Pro model greyed out on free account | Fall back to Thinking or Fast |
| **Tool unavailable** | Tool not in menu or greyed out | Report to user, suggest alternative |

### Recovery Procedure
1. Take a screenshot to capture the current state.
2. If the error is recoverable, attempt the alternative approach.
3. If not recoverable, report the error with the screenshot and suggest next steps.

---

## 10. Complete Workflow Examples

### Example 1: Generate a Cinematic Image
User says: "Create a cinematic image of a dragon flying over a mountain"
1. Navigate to gemini.google.com/app ← (if not already there)
2. Model: **Fast** (no explicit quality request) ← check current model
3. Tools → **Create image**
4. Style grid appears → keyword "cinematic" → HIGH confidence → select **Cinematic**
5. Type prompt: "a dragon flying over a mountain" (humanoid)
6. Press Enter
7. Wait for image to generate (~10-30s)
8. Click download → wait for full download
9. Upload to 0x0.st → return URL

### Example 2: Generate a Cyberpunk Video
User says: "Make a cyberpunk video of a neon city at night"
1. Navigate / verify Gemini
2. Model: **Thinking** (ALWAYS for video)
3. Tools → **Create video**
4. Template grid → keyword "cyberpunk" → HIGH confidence → select **Cyberpunk**
5. Type prompt: "a neon city at night" (humanoid)
6. Press Enter
7. Wait for video to generate (~30-120s)
8. Click download → wait for full download
9. Upload → return URL

### Example 3: Generate a Long Folk Song
User says: "Create a 3-minute folk ballad about the sea"
1. Navigate / verify Gemini
2. Model: **Thinking** ("3-minute" → long form)
3. Tools → **Create music**
4. Track grid → keyword "folk ballad" → HIGH confidence → select **Folk ballad**
5. Type prompt: "a folk ballad about the sea" (humanoid)
6. Press Enter
7. Wait for music to generate (~15-60s)
8. Click download → wait for full download
9. Upload → return URL

### Example 4: Quick Music (No Style Match)
User says: "Make me a track about summer vibes"
1. Navigate / verify Gemini
2. Model: **Fast** (no explicit long/quality request)
3. Tools → **Create music**
4. Track grid → "summer vibes" → LOW confidence (no direct match) → **SKIP style selection**
5. Type prompt: "summer vibes" (humanoid)
6. Press Enter
7. Wait → download → upload → return URL

### Example 5: Deep Research
User says: "Do deep research on quantum computing breakthroughs in 2025"
1. Navigate / verify Gemini
2. Model: keep current (Thinking recommended)
3. Tools → **Deep research**
4. No style grid for deep research
5. Type prompt (humanoid)
6. Press Enter
7. Wait for report (~2-10 minutes, can be long)
8. Report text will appear in the chat — return the text content to user

---

## 11. Reference Files

- `references/ui_elements.md` — Detailed UI element selectors and fallbacks
- `references/style_keywords.md` — Complete keyword → style mapping with confidence levels
- `scripts/download_and_share.py` — Download monitor + file upload helper
