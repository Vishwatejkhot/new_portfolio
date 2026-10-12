# Vishwatej Khot — Portfolio

Static site: `index.html` plus `assets/`. No build step.

Preview locally: `uv run main.py`, then open http://localhost:8000.

## Hero avatar
The hero has an animated, full-body SVG avatar in a suit (inline in `index.html`). It stands with hands clasped, smiles, blinks, follows the cursor and turns in 2.5D perspective. While talking it lip-syncs, raises its brows on emphasis and gestures with one hand.

- **Lip sync:** each clip in `assets/voice/` is decoded in the browser into a loudness envelope, and the mouth reads it at the current playback time. Captions come from the `CAPTIONS` object in the page script.
- **Autoplay:** the intro starts on page load. Browsers block sound until the visitor interacts, so it then plays muted with captions and a "Tap for sound" button; the first tap or key press anywhere turns the sound on. It pauses once the hero is scrolled out of view.
- **Needs http:** serve with `uv run main.py` or any host. Opened as a plain file, the clips can't be decoded, so the mouth falls back to a generic talking rhythm.

To use your own voice, record replacements with the same filenames and update the `CAPTIONS` timings.

## Assets
| File | What |
|---|---|
| `assets/profile_photo.jpeg` | Portrait in the About section |
| `assets/voice/*.mp3` | Avatar answers (AI voice: Microsoft "Prabhat", generated with edge-tts) |
| `assets/Vishwatej_Khot_CV.pdf` | CV linked from Contact |

Deploy: push to GitHub and enable Pages (root), or drag the folder into Netlify/Vercel.
