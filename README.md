<p align="center">
  <img src="https://assets.chocojayy.me/hermesemini_Generated_Image_4iv2zl4iv2zl4iv2.avif" alt="Logo" width="1920" height="600">
</p>

<h1 align="center">Gemini WebUI Controller Skill For Hermes Agent / Openclaw</h1>

<p align="center">
  <strong>A Hermes Agent Skill for full browser automation of Google Gemini</strong>
</p>

<p align="center">
  <a href="#features"><img src="https://img.shields.io/badge/Images-Nano_Banana_2_%2F_Pro-blue?style=flat-square" alt="Images"></a>
  <a href="#features"><img src="https://img.shields.io/badge/Video-Veo_3-purple?style=flat-square" alt="Video"></a>
  <a href="#features"><img src="https://img.shields.io/badge/Music-Lyria-orange?style=flat-square" alt="Music"></a>
  <a href="#features"><img src="https://img.shields.io/badge/Research-Deep_Research-green?style=flat-square" alt="Research"></a>
  <br>
  <a href="#anti-bot-system"><img src="https://img.shields.io/badge/Anti--Bot-Humanoid_Behavior-red?style=flat-square" alt="Anti-Bot"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Standard-agentskills.io-black?style=flat-square" alt="AgentSkills"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"></a>
</p>

---

## What is this?

**Gemini Web Controller** is a [Hermes Agent](https://github.com/NousResearch/hermes-agent) Skill that gives your AI agent complete control over the [Google Gemini](https://gemini.google.com/app) web interface through browser automation. Exclusively for people who dont like to pay for API and leverage the use of Google AI Plus, Pto and Ultra.  

Point your agent at a creative task — generate images, create videos, compose music, or run deep research — and this skill handles the entire workflow: model selection, tool activation, style picking, prompt entry, waiting for generation, downloading the media, and sharing it back via a temporary URL.

All interactions use **human-like behavior patterns** (bezier mouse curves, realistic typing speed, random pauses) to avoid bot detection.

---

## Features

### 🖼️ Image Generation
- Auto-selects **Fast** (Nano Banana 2) or **Thinking** (Nano Banana Pro) based on quality needs
- **12 style options** with intelligent keyword matching (Cinematic, Steampunk, Sketch, Monochrome, etc.)
- Style selection is **optional** — only activates when the prompt confidently matches a style

### 🎬 Video Creation
- Always uses **Thinking** model (required for video generation via Veo)
- **12 template options** (Cyberpunk, Cosmos, Action Hero, Jellytoon, etc.)
- Template matching is optional, confidence-based

### 🎵 Music Generation
- **Fast** model for quick ~30s tracks, **Thinking** for high-quality ~3min tracks
- **16 genre/track options** (90's rap, K-pop, Cinematic, Folk ballad, 8-bit, etc.)
- Best-match logic for genre selection when context is clear

### 🔬 Deep Research
- Activates Gemini's deep research mode for comprehensive multi-source reports
- Handles long generation times (up to 15 minutes)

### 📥 Download & Share
- Waits for **full download completion** (handles Chrome's `.crdownload` pattern)
- Cascading upload to temp file hosts: `0x0.st` → `file.io` → `tmpfiles.org`
- Returns a shareable URL to the user

---

## Anti-Bot System

Every browser interaction is designed to appear human:

| Technique | Implementation |
|-----------|---------------|
| **Mouse Movement** | Bezier-curve paths with slight overshoot and correction — no teleporting |
| **Typing Speed** | 80–180ms per character, random pauses every 5–12 chars |
| **Typo Simulation** | 1-in-30 chance of typing a wrong char, backspacing, and correcting |
| **Click Behavior** | Random 200–800ms delay before click, natural mouse-down → pause → mouse-up |
| **Scrolling** | Variable speed with small overshoots |
| **Idle Pauses** | Random 500–2000ms gaps between distinct actions |

---

## Architecture

```
gemini-control-skill/
│
├── SKILL.md                        # Core skill — procedural instructions
│                                    # (11 sections, full workflow coverage)
│
├── references/
│   ├── ui_elements.md              # UI element catalog with selectors,
│   │                                # ARIA labels, CSS fallbacks
│   └── style_keywords.md           # Keyword → style/template mapping
│                                    # with HIGH/MEDIUM/LOW confidence
│
├── scripts/
│   └── download_and_share.py       # Download monitor + temp file uploader
│
└── README.md
```

### How It Works

```
User Request
     │
     ▼
┌─────────────────────┐
│  1. Navigate to      │
│     gemini.google.com│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  2. Select Model     │──── Fast (Nano Banana 2)
│     (auto-detect)    │──── Thinking (Nano Banana Pro)
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  3. Select Tool      │──── Create Image / Video / Music / Deep Research
│     (from Tools menu)│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  4. Style/Template   │──── Optional: only if prompt matches with confidence
│     (if confident)   │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  5. Type Prompt      │──── Humanoid typing (80-180ms/char)
│     (anti-bot)       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  6. Submit & Wait    │──── Polls every 3-5s for completion
│                      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  7. Download Media   │──── Waits for full download (size stabilization)
│                      │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  8. Upload & Share   │──── 0x0.st → file.io → tmpfiles.org (cascade)
│                      │
└─────────┴───────────┘
          │
          ▼
     Shareable URL
     returned to user
```

---

## Installation

### For Hermes Agent

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/gemini-control-skill.git

# Copy to Hermes skills directory
cp -r gemini-control-skill ~/.hermes/skills/browser-automation/gemini-control
```

Or install directly via Hermes CLI:
```bash
hermes skills install ./gemini-control-skill
```

### Manual Setup

1. Clone this repository
2. Ensure Python 3.10+ is installed (for the download helper script)
3. Ensure `curl` is available in PATH (used for file uploads)
4. Make sure you're **logged into Google** in the browser that your agent controls

---

## Usage

### With Hermes Agent

Once installed, use it naturally in conversation:

```
You: Generate a cinematic image of a dragon flying over mountains
You: Create a cyberpunk video of a neon city at night  
You: Make a 3-minute folk ballad about the ocean
You: Do deep research on quantum computing breakthroughs in 2025
```

The agent reads `SKILL.md`, follows the procedural instructions, and handles everything automatically.

### Download Helper Script (Standalone)

The download & share script can also be used independently:

```bash
# Upload a specific file
python scripts/download_and_share.py path/to/file.png

# Watch Downloads folder for new files and auto-upload
python scripts/download_and_share.py --watch

# Upload the most recent file in Downloads
python scripts/download_and_share.py --newest
```

---

## Model Reference

| UI Label | Engine | Capabilities | Free Account |
|----------|--------|-------------|:------------:|
| **Fast** | Nano Banana 2 | Quick image gen, short music (~30s), general chat | ✅ |
| **Thinking** | Nano Banana Pro | High-quality images, video (required), long music (~3min) | ✅ |
| **Pro** | Gemini 2.0 Pro | Advanced math & code | ❌ (premium) |

### Auto-Selection Rules

| Task | Model Selected | Reason |
|------|:-------------:|--------|
| Image (default) | Fast | Quick generation |
| Image + "high quality" | Thinking | Better quality output |
| Video | **Always Thinking** | Required for video generation |
| Music (default) | Fast | Quick ~30s tracks |
| Music + "long"/"3 min" | Thinking | Extended ~3min, higher quality |
| Deep Research | Current | Thinking recommended |

---

## Style & Template Catalog

<details>
<summary><strong>🖼️ Image Styles (12)</strong></summary>

| Style | Example Keywords |
|-------|-----------------|
| Monochrome | `black and white`, `noir`, `grayscale` |
| Color block | `pop art`, `bold colors`, `flat color` |
| Runway | `fashion`, `editorial`, `haute couture` |
| Anyma's world | `anyma`, `futuristic abstract` |
| Risograph | `riso`, `screen print`, `textured print` |
| Technicolor | `vintage color`, `retro film`, `old hollywood` |
| Gothic clay | `gothic`, `clay sculpture`, `dark clay` |
| Dynamite | `explosive`, `dynamic action` |
| Salon | `oil painting`, `fine art`, `renaissance` |
| Sketch | `pencil`, `hand drawn`, `line art` |
| Cinematic | `movie still`, `film still`, `dramatic lighting` |
| Steampunk | `victorian mechanical`, `clockwork`, `brass` |

</details>

<details>
<summary><strong>🎬 Video Templates (12)</strong></summary>

| Template | Example Keywords |
|----------|-----------------|
| Civilization | `ancient`, `historical epic` |
| Metallic | `chrome`, `liquid metal` |
| Memo | `retro footage`, `vhs`, `old film` |
| Glam | `glamorous`, `sparkle`, `luxury` |
| Crochet | `knitted`, `yarn`, `textile art` |
| Cyberpunk | `neon city`, `blade runner`, `dystopian` |
| Video Game | `pixel art`, `8-bit`, `retro game` |
| Cosmos | `space`, `galaxy`, `nebula` |
| Action Hero | `superhero`, `action movie` |
| Stardust | `magical dust`, `fairy dust` |
| Jellytoon | `jelly cartoon`, `cute animation` |
| Racetrack | `racing`, `motorsport`, `speed` |

</details>

<details>
<summary><strong>🎵 Music Tracks (16)</strong></summary>

| Track | Example Keywords |
|-------|-----------------|
| 90's rap | `hip hop`, `boom bap`, `old school rap` |
| Latin pop | `latin music`, `spanish pop` |
| Folk ballad | `folk`, `acoustic ballad`, `campfire` |
| 8-bit | `chiptune`, `retro game music` |
| Workout | `gym`, `exercise`, `pump up` |
| Reggaeton | `perreo`, `dembow`, `latin urban` |
| R&B romance | `slow jam`, `love song`, `soul` |
| Kawaii metal | `j-metal`, `cute metal` |
| Cinematic | `film score`, `orchestral`, `epic` |
| Emo | `emotional rock`, `angsty` |
| Afropop | `afrobeats`, `african pop` |
| Forest bath | `nature`, `zen`, `meditation` |
| K-pop | `korean pop`, `idol music` |
| Birthday roast | `funny birthday`, `comedy` |
| Folk a cappella | `vocal only`, `unaccompanied` |
| Bad music | `intentionally bad`, `troll music` |

</details>

---

## Keyword Matching Logic

Style/template selection is **optional and confidence-based** — the skill never forces a bad match.

```
Scan user prompt for keywords
         │
         ▼
   ┌───────────┐
   │  HIGH     │──── Direct match (e.g., "steampunk") ──→ ✅ Select
   │ confidence│
   └─────┬─────┘
         │ no
         ▼
   ┌───────────┐
   │  MEDIUM   │──── Strong synonym (e.g., "pencil drawing" → Sketch) ──→ ✅ Select
   │ confidence│
   └─────┬─────┘
         │ no
         ▼
   ┌───────────┐
   │  LOW      │──── Vague/ambiguous (e.g., "dark", "colorful") ──→ ❌ Skip
   │ confidence│
   └───────────┘
```

Full keyword mapping tables are in [`references/style_keywords.md`](references/style_keywords.md).

---

## Requirements

- **Hermes Agent** (or any agent that supports the agentskills.io standard)
- **Browser** with Chrome DevTools Protocol (CDP) access
- **Python 3.10+** (for the download helper script)
- **curl** (for file uploads)
- **Google Account** logged in on the browser

---

## Limitations

- ⚠️ **Pro model** is not available on free Google accounts
- ⚠️ The Gemini UI may update — if elements are not found, the skill falls back to text-based selectors and provides error recovery steps
- ⚠️ CAPTCHAs cannot be solved automatically — the skill will stop and ask the user to intervene
- ⚠️ Content policy blocks are reported to the user, not bypassed

---

## Contributing

Contributions are welcome! Some areas that could use improvement:

- [ ] Add more style/template keyword synonyms
- [ ] Support for Gemini's canvas/document mode
- [ ] Support for image editing (re-generate, modify existing images)
- [ ] Add guided learning workflow
- [ ] Multi-language keyword mapping
- [ ] Browser session persistence between invocations
- [ ] Support for Google Workspace accounts

### How to Contribute

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Test with Hermes agent or manual browser automation
5. Submit a Pull Request

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <sub>Built with ❤️ for the Hermes Agent ecosystem</sub>
  <br>
  <sub>Follows the <a href="https://agentskills.io">agentskills.io</a> open standard</sub>
</p>
