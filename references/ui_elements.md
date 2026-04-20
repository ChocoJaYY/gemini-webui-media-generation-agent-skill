# Gemini UI Elements Reference

> Last verified: April 2026 | URL: https://gemini.google.com/app

## Important Notes

- **UIDs are dynamic** — they change between page loads and menu interactions. Never hardcode UIDs.
- **Use text-based selectors** as the primary strategy: look for elements by their visible text content, aria-labels, or roles.
- **Fallback to CSS selectors** if text matching fails.
- **Always take a fresh snapshot** before interacting with any element.

---

## Core Input Area

### Prompt Input
| Property | Value |
|----------|-------|
| **Element Type** | `div` (contenteditable) |
| **aria-label** | `"Enter a prompt for Gemini"` |
| **Placeholder text** | Varies by mode: "Ask Gemini", "Describe the image you want to create", "Describe the video you want to create", "Describe your track" |
| **Location** | Bottom center of page |
| **CSS Fallback** | `div.ql-editor[contenteditable="true"]`, `div[aria-label*="prompt"]` |
| **Notes** | This is a rich text div, NOT an `<input>` or `<textarea>`. Use click-to-focus then keyboard typing. |

### Send / Submit Button
| Property | Value |
|----------|-------|
| **Element Type** | `button` |
| **Icon** | Arrow/send icon (→ or ▶) |
| **aria-label** | `"Send message"` or similar |
| **Location** | Right side of prompt input area |
| **State** | Disabled when prompt is empty; enabled when text is entered |
| **Alternative** | Press `Enter` key to submit (preferred method) |

### Attachment / Upload Button
| Property | Value |
|----------|-------|
| **Element Type** | `button` |
| **Icon** | `+` (plus) icon |
| **Location** | Left side of prompt input area, before Tools button |
| **Notes** | Opens file attachment dialog |

---

## Tools System

### Tools Button
| Property | Value |
|----------|-------|
| **Element Type** | `button` |
| **Text Content** | `"Tools"` |
| **Icon** | Adjustment sliders icon (☰ variant) |
| **aria-label** | `"Tools"` |
| **Location** | Bottom input bar, after the `+` button |
| **CSS Fallback** | `button[aria-label="Tools"]` |
| **Behavior** | Click opens a dropdown/popover menu |

### Tools Dropdown Menu Items
When the Tools button is clicked, these menu items appear:

| Menu Item | Text | Icon | Notes |
|-----------|------|------|-------|
| **Create image** | `"Create image"` | 🖼 (image icon) | May have "New" badge |
| **Canvas** | `"Canvas"` | 📋 (canvas icon) | For document editing |
| **Deep research** | `"Deep research"` | 🔍 (research icon) | Long-form research reports |
| **Create video** | `"Create video"` | 🎬 (video icon) | Video generation |
| **Create music** | `"Create music"` | 🎵 (music icon) | Music generation |
| **Guided learning** | `"Guided learning"` | 📚 (learning icon) | Learning mode |

**Selection strategy:** Find the menu item by its exact text content (e.g., look for element containing text "Create image").

### Active Tool Tag / Chip
When a tool is selected, it appears as a tag in the prompt input bar:
| Property | Value |
|----------|-------|
| **Format** | `"[icon] Create image ×"` or `"♫ Create music ×"` etc. |
| **Deselect Button** | `×` button to the right of the tag text |
| **Location** | In the bottom bar, between Tools button and model selector |
| **How to detect** | Look for text like "Create image", "Create video", "Create music" followed by "×" in the input bar area |

---

## Model Selector

### Mode Picker Button
| Property | Value |
|----------|-------|
| **Element Type** | `button` |
| **aria-label** | `"Open mode picker"` |
| **Text Content** | Current model name: `"Fast"`, `"Thinking"`, or `"Pro"` |
| **Location** | Right side of the prompt input bar, before microphone |
| **Icon** | Dropdown arrow `∨` after the model name |
| **CSS Fallback** | `button[aria-label="Open mode picker"]` |

### Model Options (in dropdown)
When the mode picker button is clicked:

| Option | Text | Description | Available Free? |
|--------|------|------------|-----------------|
| **Fast** | `"Fast"` | `"Answers quickly"` | ✅ Yes |
| **Thinking** | `"Thinking"` | `"Solves complex problems"` | ✅ Yes |
| **Pro** | `"Pro"` | `"Advanced math and code with 3.1 Pro"` | ❌ No (premium only) |

**Selection strategy:**
1. Click the mode picker button.
2. In the dropdown, find the element with text matching the desired model ("Fast" or "Thinking").
3. Click it.
4. Dropdown closes automatically.

### Detecting Current Model
- Read the text content of the mode picker button.
- If it says "Fast" → currently using Fast/Nano Banana 2.
- If it says "Thinking" → currently using Thinking/Nano Banana Pro.

---

## Style / Template / Track Grids

These grids appear above the prompt input after selecting a creation tool.

### Common Grid Structure
- Each option is a **card** containing:
  - A preview **image/thumbnail**
  - A **text label** at the bottom of the card
  - Optional **play button** (▶) overlay for music tracks
- Cards are arranged in a **3-column grid layout**
- Grid may require **scrolling** to see all options

### Image Style Grid
| Header Text | `"Pick a style for your image"` |
|---|---|
| **Visible without scrolling** | Monochrome, Color block, Runway, Anyma's world, Risograph, Technicolor, Gothic clay, Dynamite, Salon, Sketch, Cinematic, Steampunk |
| **Selection indicator** | Selected card gets highlighted border/glow |
| **How to select** | Click the card with text matching desired style |

### Video Template Grid
| Header Text | `"Pick a template to create a video"` |
|---|---|
| **Visible without scrolling** | Civilization, Metallic, Memo, Glam, Crochet, Cyberpunk |
| **Needs scrolling** | Video Game, Cosmos, Action Hero, Stardust, Jellytoon, Racetrack |
| **How to select** | Click the card with text matching desired template |

### Music Track Grid
| Header Text | `"Pick a track to remix"` |
|---|---|
| **Visible without scrolling** | 90's rap, Latin pop, Folk ballad, 8-bit, Workout, Reggaeton, R&B romance, Kawaii metal, Cinematic |
| **Needs scrolling** | Emo, Afropop, Forest bath, K-pop, Birthday roast, Folk a cappella, Bad music |
| **How to select** | Click the card with text matching desired track |

---

## Post-Generation Elements

### Generated Image
| Property | Value |
|----------|-------|
| **Container** | Image card in chat response area |
| **Download** | Look for download icon (⬇) on hover or in card actions |
| **Share** | May have share button nearby |
| **Expand** | Click image to view full size |

### Generated Video
| Property | Value |
|----------|-------|
| **Container** | Video player element in chat response area |
| **Controls** | Play/pause, volume, fullscreen, download |
| **Download** | Download button below or within video player controls |

### Generated Music/Audio
| Property | Value |
|----------|-------|
| **Container** | Audio player element in chat response area |
| **Controls** | Play/pause, seek bar, volume |
| **Download** | Download icon near player controls, may download as MP3 or video |

### Download Button (General)
| Property | Value |
|----------|-------|
| **Icon** | ⬇ (down arrow) or download icon |
| **aria-label** | May contain "download", "save", or "export" |
| **Location** | On/near the generated media element |
| **CSS Fallback** | `button[aria-label*="ownload"]`, `a[download]` |

---

## Navigation Elements

### New Chat Button
| Property | Value |
|----------|-------|
| **Element** | Button with pencil/edit icon |
| **Location** | Top-left area / sidebar |
| **aria-label** | May contain "New chat" or "new conversation" |

### Sidebar Toggle (Hamburger Menu)
| Property | Value |
|----------|-------|
| **Element** | `button` with ☰ icon |
| **Location** | Top-left corner |
| **aria-label** | `"Main menu"` or similar |

### Welcome Banner Dismiss
| Property | Value |
|----------|-------|
| **Element** | `×` close button |
| **Text nearby** | "Welcome to Gemini, your personal AI assistant" |
| **Location** | Bottom portion of page, above input area |

---

## Loading / Progress Indicators

| Indicator | What it means |
|-----------|--------------|
| **Spinning dots / animation** | Generation in progress |
| **"Thinking..."** text | Model is processing |
| **Progress bar** | Generation progress (may appear for video) |
| **Pulsing/shimmer effect** | Content is loading |
| **Absence of loading + media visible** | Generation complete |

---

## Selector Priority Order

When finding an element, try selectors in this order:
1. **Text content** — Find by visible text (most reliable across UI updates)
2. **aria-label** — Find by accessibility label
3. **Role + context** — Find by element role combined with nearby text
4. **CSS selector** — Last resort, most fragile

Always take a fresh snapshot before each interaction to get current UIDs.
