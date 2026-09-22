# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://group-creative-service.lovable.app/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | LIVE https://www.youtube.com/watch?v=Mes2zHsSutE (2026-09-02) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | LIVE (unlisted) https://www.youtube.com/watch?v=LAkEfhBi37s (uploaded 2026-09-15) |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | jobs/iplaygames-video-03 | LIVE (unlisted) https://www.youtube.com/watch?v=Px5KCcNsb20 (uploaded 2026-09-15) |
| 04 | One tag, live jackpot: drop-in widgets | jobs/iplaygames-video-04 | RENDERED 2026-09-22 (1:33, 4.17 MB) https://group-creative-service.lovable.app/video/iplaygames-video-04.mp4 — AWAITING DAVID'S APPROVAL, do not upload until he says so |
| 05 | Freespins, cashback, tournaments: the bonus engine | — | planned |
| 06 | How to evaluate a casino game aggregator before you sign | — | planned |
| 07 | From signed to live: four steps with an aggregator | — | planned |

After 07: propose new topics to David instead of repeating.

Render notes: run render.py detached (agent command limit 600 s); PLAYWRIGHT_BROWSERS_PATH=/nix/store/pp3i69v0m7vh8nicq8f4pbabc2awhm1g-playwright-browsers-with-overrides; do NOT `playwright install chromium`; /tmp is wiped between Creative Forge agent turns.

render.py builds the MP4 only. The 1280x720 thumbnail is a separate Playwright screenshot of jobs/<job>/thumb.html at 1920x1080, downscaled with PIL, saved as out/<job>-thumb.jpg.

Chapter timings can be reproduced exactly without re-rendering: run the Kokoro TTS over script.json with the same voice/speed/lang, pad each scene with 0.4 s lead + 0.6 s tail, add the scene's `hold`, and accumulate.

### Pending for video 04 (proposed YouTube metadata, not yet uploaded)
- Title: iPlayGames — One Tag, Live Jackpot: The Drop-In Jackpot Widget
- Chapters: 0:00 One tag · 0:08 The usual build · 0:25 Load the script, drop in the element · 0:41 The widget handles the rest · 1:01 Behind the tag: your jackpots · 1:20 Book a walkthrough
- Upload settings: unlisted, category 28, default_language en, made_for_kids false, notify_subscribers false
