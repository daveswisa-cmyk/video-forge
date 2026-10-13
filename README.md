# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://www.mycreative.group/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | LIVE https://www.youtube.com/watch?v=Mes2zHsSutE (2026-09-02) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | LIVE (unlisted) https://www.youtube.com/watch?v=LAkEfhBi37s (uploaded 2026-09-15) |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | jobs/iplaygames-video-03 | LIVE (unlisted) https://www.youtube.com/watch?v=Px5KCcNsb20 (uploaded 2026-09-15) |
| 04 | One tag, live jackpot: drop-in widgets | jobs/iplaygames-video-04 | RENDERED 2026-09-22 (1:33, 4.17 MB) https://www.mycreative.group/video/iplaygames-video-04.mp4 - AWAITING DAVID'S APPROVAL, 21 days overdue. Reminders 2026-09-29, escalated 2026-10-06 and 2026-10-13. Do not upload until he says so |
| 05 | Freespins, cashback, tournaments: the bonus engine | jobs/iplaygames-video-05 | RENDERED 2026-09-29 (1:40, 4.41 MB) https://www.mycreative.group/video/iplaygames-video-05.mp4 - AWAITING DAVID'S APPROVAL, 14 days overdue. Escalated 2026-10-06 and 2026-10-13. Do not upload until he says so |
| 06 | How to evaluate a casino game aggregator before you sign | - | PRODUCTION HELD 2026-10-06, held again 2026-10-13 - see "Production hold" below |
| 07 | From signed to live: four steps with an aggregator | - | planned |

After 07: propose new topics to David instead of repeating.

### Production hold (decision 2026-10-06)

The weekly run on 2026-10-06 did **not** produce video 06. Reason: 04 and 05 are both
rendered, deployed and waiting on David's approval (14 and 7 days), and nothing has
published to the channel since 2026-09-15. The constraint on the series is approval
throughput, not production throughput, so rendering a third unapproved video would have
added inventory and zero published reach - and risked rework, since feedback on 04/05
may change the format 06 inherits. Video 06 is also the most editorially sensitive in the
series (neutral evaluation checklist drawn from the /guides competitor-alternatives pages)
and wants David's direction before scripting.

Verified on 2026-10-06:
- YouTube Data API `search?forMine=true` returns exactly 3 videos (01, 02, 03). 04 and 05 are NOT uploaded.
- All four assets for 04 and 05 are present at HEAD in the Creative Forge Lovable project:
  `public/video/iplaygames-video-04.mp4`, `-04-thumb.jpg`, `-05.mp4`, `-05-thumb.jpg`.
- Raw HTTP checks against www.mycreative.group are blocked by the task sandbox's egress
  policy (403 at the proxy), so serving was verified at the project-file level instead.

### Production hold, week 2 (decision 2026-10-13)

The weekly run on 2026-10-13 again did **not** produce video 06. The hold reasoning above is
unchanged and has only got stronger: 04 is now 21 days unapproved, 05 is 14 days unapproved,
and the channel has published nothing for 4 weeks. Two finished videos sitting unpublished is
already more inventory than the series can absorb; a third would be waste, not progress.

Verified on 2026-10-13:
- YouTube Data API `search?forMine=true` returns exactly 3 videos (01, 02, 03). 04 and 05 are
  still NOT uploaded.
- `public/video/iplaygames-video-05-thumb.jpg` reads back at HEAD in the Creative Forge Lovable
  project, so the deployed assets are intact.
- No approval arrived through any channel this run could read: no reply in Gmail (searched
  iplaygames-video and video 04/05 since 2026-09-20), nothing in memory, no change on YouTube.
- Raw HTTP checks against www.mycreative.group are still blocked by the task sandbox (the
  permission prompt cannot be answered in an unattended run), so serving is again verified at
  the project-file level only.

**The real problem is the approval channel, not David.** Three weeks of silence on a one-word
reply is a signal that asking for approval inside a chat session nobody is sitting in does not
work. Escalating a fourth time the same way will not fix it. So this run asked David to choose
one of three standing arrangements instead:

1. **Auto-upload unlisted.** Finished renders go up as unlisted immediately - invisible to the
   public and to subscribers - and David reviews them on YouTube, flipping to public when he is
   happy. Reversible, and it decouples production from his inbox.
2. **Fortnightly cadence.** Keep approval-before-upload, halve production to match the rate he
   actually reviews at.
3. **Delegate approval** to someone else on the iPlayGames side, like the per-company approver
   rules already in place for Slikair (Tzach) and Savoy Drugstore (Hanin).

**Next run:** if David approved 04 and/or 05, upload oldest first, then produce 06. If he chose
one of the three arrangements above, implement it and record it here. If he is still silent, do
NOT render 06 and do NOT send a fifth identical escalation - treat the pipeline as paused,
report it as paused, and surface it in the group report as a stalled channel rather than a
pending task.

Render notes: run render.py detached (agent command limit 600 s); PLAYWRIGHT_BROWSERS_PATH=/nix/store/pp3i69v0m7vh8nicq8f4pbabc2awhm1g-playwright-browsers-with-overrides; do NOT `playwright install chromium`; /tmp is wiped between Creative Forge agent turns.

render.py builds the MP4 only. The 1280x720 thumbnail is built by render/thumb.py (added 2026-09-29): `python3 render/thumb.py <job>` screenshots jobs/<job>/thumb.html at 1920x1080 in Playwright, inlines the logo the same way render.py does, downscales with PIL and writes out/<job>-thumb.jpg. Run it after render.py, then copy both files to public/video/.

Serving note (2026-09-29): https://group-creative-service.lovable.app/video/... now returns 302 to https://www.mycreative.group/video/... (mycreative.group is the project's primary domain). Use the www.mycreative.group URL for YouTube uploads and for links sent to David.

Chapter timings can be reproduced exactly without re-rendering: run the Kokoro TTS over script.json with the same voice/speed/lang, pad each scene with 0.4 s lead + 0.6 s tail, add the scene's `hold`, and accumulate.

### Pending for video 04 (proposed YouTube metadata, not yet uploaded)
- Title: iPlayGames - One Tag, Live Jackpot: The Drop-In Jackpot Widget
- Chapters: 0:00 One tag / 0:08 The usual build / 0:25 Load the script, drop in the element / 0:41 The widget handles the rest / 1:01 Behind the tag: your jackpots / 1:20 Book a walkthrough
- Thumbnail: https://www.mycreative.group/video/iplaygames-video-04-thumb.jpg
- Upload settings: unlisted, category 28, default_language en, made_for_kids false, notify_subscribers false

### Pending for video 05 (proposed YouTube metadata, not yet uploaded)
- Title: iPlayGames - Freespins, Cashback, Tournaments: The Bonus Engine
- Chapters: 0:00 Freespins, cashback, tournaments / 0:11 Why promotions cost time / 0:30 Freespins: a campaign, not a project / 0:46 Cashback, loyalty and VIP tiers / 1:08 Tournaments and live leaderboards / 1:25 Book a walkthrough
- Scene starts (s1-s6): 0.00, 11.70, 30.03, 46.70, 68.20, 85.70 s; total 100.0 s
- Thumbnail: https://www.mycreative.group/video/iplaygames-video-05-thumb.jpg (1280x720, 67,985 bytes)
- Upload settings: unlisted, category 28, default_language en, made_for_kids false, notify_subscribers false
