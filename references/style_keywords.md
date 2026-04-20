# Style / Template / Track Keyword Mapping

> This file defines how to match user prompt keywords to Gemini's style, template, and track options.
> Matching is **optional** — only select when confidence is HIGH or MEDIUM. Skip on LOW.

---

## Confidence Levels

| Level | Rule | Action |
|-------|------|--------|
| **HIGH** | Direct keyword match or very close synonym | ✅ Select the style |
| **MEDIUM** | Strong contextual synonym | ✅ Select the style |
| **LOW** | Vague, ambiguous, or weak association | ❌ Do NOT select — let Gemini choose |

---

## Image Styles

### Monochrome
| Confidence | Keywords |
|-----------|----------|
| HIGH | `monochrome`, `black and white`, `b&w`, `bw` |
| MEDIUM | `grayscale`, `noir`, `black-and-white`, `greyscale` |
| LOW | `dark`, `moody` (too vague) |

### Color block
| Confidence | Keywords |
|-----------|----------|
| HIGH | `color block`, `colorblock` |
| MEDIUM | `pop art`, `bold colors`, `flat color`, `block color` |
| LOW | `colorful`, `bright` (too generic) |

### Runway
| Confidence | Keywords |
|-----------|----------|
| HIGH | `runway`, `fashion runway` |
| MEDIUM | `fashion`, `editorial`, `vogue`, `haute couture` |
| LOW | `stylish`, `trendy` |

### Anyma's world
| Confidence | Keywords |
|-----------|----------|
| HIGH | `anyma`, `anyma's world` |
| MEDIUM | `futuristic abstract`, `digital surreal` |
| LOW | `abstract`, `digital art` (too broad) |

### Risograph
| Confidence | Keywords |
|-----------|----------|
| HIGH | `risograph`, `riso` |
| MEDIUM | `riso print`, `textured print`, `screen print`, `print style` |
| LOW | `printed`, `textured` |

### Technicolor
| Confidence | Keywords |
|-----------|----------|
| HIGH | `technicolor` |
| MEDIUM | `vintage color`, `retro film`, `old hollywood`, `classic film` |
| LOW | `vintage`, `retro` (too broad) |

### Gothic clay
| Confidence | Keywords |
|-----------|----------|
| HIGH | `gothic clay` |
| MEDIUM | `gothic`, `clay sculpture`, `dark clay`, `sculpted gothic` |
| LOW | `dark`, `horror`, `clay` (standalone too vague) |

### Dynamite
| Confidence | Keywords |
|-----------|----------|
| HIGH | `dynamite`, `dynamite style` |
| MEDIUM | `explosive`, `dynamic action`, `blast` |
| LOW | `action`, `energy` (too vague) |

### Salon
| Confidence | Keywords |
|-----------|----------|
| HIGH | `salon`, `salon style` |
| MEDIUM | `classical painting`, `oil painting`, `fine art`, `renaissance` |
| LOW | `elegant`, `fancy` |

### Sketch
| Confidence | Keywords |
|-----------|----------|
| HIGH | `sketch`, `pencil sketch`, `pencil drawing` |
| MEDIUM | `hand drawn`, `hand-drawn`, `line art`, `line drawing`, `charcoal`, `ink drawing` |
| LOW | `drawing` (too broad), `illustration` |

### Cinematic
| Confidence | Keywords |
|-----------|----------|
| HIGH | `cinematic`, `movie still` |
| MEDIUM | `film still`, `dramatic lighting`, `movie scene`, `cinema`, `film look` |
| LOW | `dramatic`, `scene` |

### Steampunk
| Confidence | Keywords |
|-----------|----------|
| HIGH | `steampunk` |
| MEDIUM | `victorian mechanical`, `gears and pipes`, `clockwork`, `brass machinery` |
| LOW | `victorian`, `mechanical`, `gears` (standalone) |

---

## Video Templates

### Civilization
| Confidence | Keywords |
|-----------|----------|
| HIGH | `civilization` |
| MEDIUM | `ancient civilization`, `historical epic`, `ancient world` |
| LOW | `history`, `ancient` |

### Metallic
| Confidence | Keywords |
|-----------|----------|
| HIGH | `metallic` |
| MEDIUM | `chrome`, `liquid metal`, `metal surface`, `shiny metal` |
| LOW | `metal`, `silver` |

### Memo
| Confidence | Keywords |
|-----------|----------|
| HIGH | `memo`, `memo style` |
| MEDIUM | `retro footage`, `old film`, `vhs`, `vintage video`, `home video` |
| LOW | `retro`, `old` |

### Glam
| Confidence | Keywords |
|-----------|----------|
| HIGH | `glam` |
| MEDIUM | `glamorous`, `sparkle`, `luxury`, `red carpet`, `dazzle` |
| LOW | `fancy`, `beautiful` |

### Crochet
| Confidence | Keywords |
|-----------|----------|
| HIGH | `crochet` |
| MEDIUM | `knitted`, `yarn`, `textile art`, `fabric animation`, `woven` |
| LOW | `fabric`, `soft` |

### Cyberpunk
| Confidence | Keywords |
|-----------|----------|
| HIGH | `cyberpunk` |
| MEDIUM | `cyber`, `neon city`, `futuristic neon`, `blade runner`, `dystopian neon` |
| LOW | `futuristic`, `neon` (standalone) |

### Video Game
| Confidence | Keywords |
|-----------|----------|
| HIGH | `video game`, `videogame` |
| MEDIUM | `game style`, `pixel art`, `8-bit video`, `retro game`, `game animation` |
| LOW | `game`, `pixel` (standalone) |

### Cosmos
| Confidence | Keywords |
|-----------|----------|
| HIGH | `cosmos` |
| MEDIUM | `space`, `galaxy`, `stars`, `universe`, `nebula`, `cosmic` |
| LOW | `sky`, `night` |

### Action Hero
| Confidence | Keywords |
|-----------|----------|
| HIGH | `action hero` |
| MEDIUM | `superhero`, `action movie`, `hero shot`, `epic hero` |
| LOW | `hero`, `action` (standalone) |

### Stardust
| Confidence | Keywords |
|-----------|----------|
| HIGH | `stardust` |
| MEDIUM | `magical dust`, `fairy dust`, `sparkle particles`, `glitter particles` |
| LOW | `sparkle`, `magic` |

### Jellytoon
| Confidence | Keywords |
|-----------|----------|
| HIGH | `jellytoon` |
| MEDIUM | `jelly cartoon`, `squishy cartoon`, `cute animation`, `blob cartoon` |
| LOW | `cartoon`, `animated` (too broad) |

### Racetrack
| Confidence | Keywords |
|-----------|----------|
| HIGH | `racetrack`, `race track` |
| MEDIUM | `racing`, `car race`, `speed`, `motorsport`, `formula` |
| LOW | `car`, `fast` |

---

## Music Tracks

> For music, also consider **best match** — if the user describes a mood/genre that maps clearly to one track, select it even without an exact keyword match.

### 90's rap
| Confidence | Keywords |
|-----------|----------|
| HIGH | `90s rap`, `90's rap`, `nineties rap` |
| MEDIUM | `hip hop`, `old school rap`, `boom bap`, `hip-hop`, `classic rap` |
| LOW | `rap` (too broad) |

### Latin pop
| Confidence | Keywords |
|-----------|----------|
| HIGH | `latin pop` |
| MEDIUM | `latin music`, `spanish pop`, `latino`, `tropical pop` |
| LOW | `latin`, `spanish` (could mean other genres) |

### Folk ballad
| Confidence | Keywords |
|-----------|----------|
| HIGH | `folk ballad`, `folk song` |
| MEDIUM | `folk`, `acoustic ballad`, `folk acoustic`, `campfire song`, `singer-songwriter` |
| LOW | `ballad`, `acoustic` (could be other genres) |

### 8-bit
| Confidence | Keywords |
|-----------|----------|
| HIGH | `8-bit`, `8bit`, `chiptune` |
| MEDIUM | `retro game music`, `pixel music`, `game soundtrack`, `nintendo style` |
| LOW | `retro`, `game` |

### Workout
| Confidence | Keywords |
|-----------|----------|
| HIGH | `workout`, `workout music` |
| MEDIUM | `gym`, `exercise`, `pump up`, `training music`, `fitness`, `high energy` |
| LOW | `energetic`, `fast` |

### Reggaeton
| Confidence | Keywords |
|-----------|----------|
| HIGH | `reggaeton` |
| MEDIUM | `perreo`, `dembow`, `latin beat`, `reggaetón`, `latin urban` |
| LOW | `latin`, `dance` |

### R&B romance
| Confidence | Keywords |
|-----------|----------|
| HIGH | `r&b romance`, `rnb romance` |
| MEDIUM | `r&b`, `rnb`, `slow jam`, `love song`, `romantic r&b`, `soul` |
| LOW | `romance`, `love` (too broad) |

### Kawaii metal
| Confidence | Keywords |
|-----------|----------|
| HIGH | `kawaii metal` |
| MEDIUM | `kawaii`, `j-metal`, `cute metal`, `babymetal style` |
| LOW | `metal`, `cute` |

### Cinematic
| Confidence | Keywords |
|-----------|----------|
| HIGH | `cinematic music`, `film score` |
| MEDIUM | `orchestral`, `epic music`, `movie soundtrack`, `trailer music`, `epic orchestral` |
| LOW | `epic`, `dramatic` |

### Emo
| Confidence | Keywords |
|-----------|----------|
| HIGH | `emo`, `emo rock` |
| MEDIUM | `emotional rock`, `angsty`, `my chemical romance style`, `emo punk` |
| LOW | `emotional`, `sad rock` |

### Afropop
| Confidence | Keywords |
|-----------|----------|
| HIGH | `afropop`, `afrobeats` |
| MEDIUM | `african pop`, `african music`, `afro`, `naija`, `afrobeat` |
| LOW | `african`, `world music` |

### Forest bath
| Confidence | Keywords |
|-----------|----------|
| HIGH | `forest bath`, `forest bathing` |
| MEDIUM | `nature sounds`, `ambient nature`, `zen`, `meditation music`, `peaceful forest`, `relaxation` |
| LOW | `peaceful`, `calm`, `ambient` (could be many things) |

### K-pop
| Confidence | Keywords |
|-----------|----------|
| HIGH | `kpop`, `k-pop`, `korean pop` |
| MEDIUM | `korean music`, `idol music`, `bts style`, `blackpink style` |
| LOW | `korean`, `pop` |

### Birthday roast
| Confidence | Keywords |
|-----------|----------|
| HIGH | `birthday roast`, `birthday song roast` |
| MEDIUM | `birthday`, `roast song`, `funny birthday`, `comedy birthday` |
| LOW | `funny`, `comedy` |

### Folk a cappella
| Confidence | Keywords |
|-----------|----------|
| HIGH | `folk a cappella`, `folk acapella` |
| MEDIUM | `a cappella`, `acapella`, `vocal only`, `unaccompanied vocal` |
| LOW | `vocal`, `singing` |

### Bad music
| Confidence | Keywords |
|-----------|----------|
| HIGH | `bad music`, `intentionally bad` |
| MEDIUM | `terrible music`, `worst music`, `joke music`, `troll music` |
| LOW | `funny music` |

---

## Matching Algorithm (for agent reference)

```
function matchStyle(userPrompt, styleTable):
    userPromptLower = lowercase(userPrompt)
    bestMatch = null
    bestConfidence = "LOW"
    
    for each style in styleTable:
        for each (confidence, keywords) in style.mappings:
            for each keyword in keywords:
                if keyword exists in userPromptLower:
                    if confidence == "HIGH":
                        return style  // immediate match
                    elif confidence == "MEDIUM" and bestConfidence != "HIGH":
                        bestMatch = style
                        bestConfidence = "MEDIUM"
    
    if bestConfidence == "MEDIUM":
        return bestMatch
    
    return null  // no confident match, skip style selection
```
