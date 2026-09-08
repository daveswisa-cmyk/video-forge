# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://group-creative-service.lovable.app/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | LIVE https://www.youtube.com/watch?v=Mes2zHsSutE (2026-09-02) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | RENDERED 2026-09-08 (1:39), awaiting David's approval to upload. MP4: https://group-creative-service.lovable.app/video/iplaygames-video-02.mp4 |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | — | planned |
| 04 | One tag, live jackpot: drop-in widgets | — | planned |
| 05 | Freespins, cashback, tournaments: the bonus engine | — | planned |
| 06 | How to evaluate a casino game aggregator before you sign | — | planned |
| 07 | From signed to live: four steps with an aggregator | — | planned |

After 07: propose new topics to David instead of repeating.

Render notes: run render.py detached (agent command limit 600 s); PLAYWRIGHT_BROWSERS_PATH=/nix/store/pp3i69v0m7vh8nicq8f4pbabc2awhm1g-playwright-browsers-with-overrides; do NOT `playwright install chromium`; /tmp is wiped between Creative Forge agent turns.
