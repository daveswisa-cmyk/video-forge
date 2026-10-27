# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://www.mycreative.group/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | LIVE https://www.youtube.com/watch?v=Mes2zHsSutE (2026-09-02) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | LIVE (unlisted) https://www.youtube.com/watch?v=LAkEfhBi37s (uploaded 2026-09-15) |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | jobs/iplaygames-video-03 | LIVE (unlisted) https://www.youtube.com/watch?v=Px5KCcNsb20 (uploaded 2026-09-15) |
| 04 | One tag, live jackpot: drop-in widgets | jobs/iplaygames-video-04 | UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=GbLU0eX94NI (1:34, 4.17 MB). Custom thumbnail set. SHOWN TO ANDREA BY EMAIL 2026-10-27. |
| 05 | Freespins, cashback, tournaments: the bonus engine | jobs/iplaygames-video-05 | RE-RENDERED + UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=yeCg-O8PqO4 (1:41, 4.49 MB). Custom thumbnail set. SHOWN TO ANDREA BY EMAIL 2026-10-27. |
| 06 | How to evaluate a casino game aggregator before you sign | jobs/iplaygames-video-06 | RENDERED 2026-10-27, 1:56.7, 4,859,344 bytes, 1920x1080 h264 + aac, 3500 frames @30fps. Thumbnail 1280x720, 66,351 bytes. Live at https://www.mycreative.group/video/iplaygames-video-06.mp4 . NOT UPLOADED TO YOUTUBE - with Andrea. |
| 07 | From signed to live: four steps with an aggregator | - | planned |

After 07: propose new topics to David instead of repeating.

Scene starts for 06 (30 fps): 0.000, 10.600, 33.133, 56.567, 79.333, 100.000 s; total 116.667 s.

## 2026-10-27 run: the series now has a registry row, and Andrea was finally reached

**The four-week stall had two causes, and both are now addressed.**

**Cause 1: the notice channel is broken.** Re-tested this run and it is unchanged: the Zapier Telegram
connection is the bot **@Monsterslotreportbot**, it is **not a member of iPlayGames room -5537782973**, and
`send_message` returns `Bad Request: chat not found`. The same call to David's private chat 6336470366
succeeds. The room is reachable only by the hub's own approvals bot, which runs inside the B2BLeeds project
and is a different bot (public.telegram_send_log shows message 2159 delivered there at 2026-10-27 03:54Z).
Per the 10-20 note this was NOT retried a second time.

**What was done instead of retrying.** Andrea has a registered approver mailbox - `andrea@iplaygames.ai`,
public.approvers, mailbox `zoho_iplaygames`. She was emailed from marketing@iplaygames.ai: 04 and 05 with
their links (Zoho messageId 1793086341796155300), and then 06 with the public MP4 URL, the full script and
the proposed title, description with chapters and tags (messageId 1793087458166155100). David was asked in
Hebrew, in 6336470366, to add the bot to the room - a ten-second fix that unblocks the lane permanently.

**Cause 2: the series had no campaign_registry row.** It ran from 2026-09-02 with no row at all, which is
exactly the failure the registry exists to prevent: no owner, no named approver and no `next_action_at`
anywhere outside this README, so for four weeks the reminders went to David - who is not the approver -
and nobody noticed. Row created 2026-10-27: `c644c6e6-2478-49b7-8504-5872cc5ad0de`, company iPlayGames,
campaign_group `iplaygames-youtube-series-2026`, owner Claude, manager_approver Andrea, state
pending_manager, next_action_at 2026-11-03. Note `channel` is `other`, not `youtube`, only because
`campaign_registry_channel_check` has no youtube value - do not read that as an unknown channel.

### 04, 05 and 06 stay unlisted, deliberately

app_state.publish_policy (David, 2026-10-13) removed the per-post approval gate, and an approver who has not
answered is explicitly listed under `what_is_no_longer_a_reason_to_stop`. But the policy kept one
precondition: a post is **shown** in its room before it goes out. Andrea had never been shown these, so
flipping them public would have skipped the one step the policy still requires - it would have been
publishing without notice, not publishing after silence. Now that the notice has gone out, her silence does
not hold them: once she has had a fair chance to look, 04 and 05 go public oldest first, then 06.

### Open with Andrea: "studios" is in the three live videos

Unchanged from 10-20 and now actually put to her. 01, 02 and 03 say "studios" in the **voiceover and on
screen**, and their YouTube descriptions say "100+ studios". They were uploaded before her 5 Oct ruling.
Descriptions are a `videos.update` away; the audio and the scene cards are not, short of re-rendering and
replacing three live videos. This run did **not** touch them - that is her call, and fixing only the
descriptions would leave the narration contradicting them.

### Why 06 was produced this week after three holds

The 10-06, 10-13 and 10-20 runs held production on the grounds that adding a third unseen video is inventory,
not progress. That was right while the decider could not be reached. This run reached her, so the argument
expired. The editorial-sensitivity concern was also weaker than it looked: 06 is drawn entirely from
`/guides/hub88-alternatives`, which is already live and already cleared, so scripting it restates published
copy rather than taking a new position. It names no competitor and quotes no number. The one thing that did
need care is that the source page carries **free sandbox / no credit card** language that is forbidden in our
marketing copy and held outright by app_state.iplaygames_sandbox_post_hold - so the guide's "sandbox before
signature" criterion was dropped and seven of the eight were used.

## Render notes

**The PLAYWRIGHT_BROWSERS_PATH in the weekly task prompt and in earlier versions of this README is STALE and
now fails.** `/nix/store/pp3i69v0m7vh8nicq8f4pbabc2awhm1g-playwright-browsers-with-overrides` no longer has
the build Playwright asks for, and the launch dies with `Executable doesn't exist at
.../chromium_headless_shell-1194/chrome-linux/headless_shell`.

Working recipe as of 2026-10-27 - build a shim in a writable path and point Playwright at it:

```
mkdir -p /tmp/pwb/chromium_headless_shell-1194 /tmp/pwb/chromium-1194
ln -sfn /nix/store/nw961dvpvik5m19kbay4cg27wxgl3sdv-playwright-chromium-headless-shell/chrome-linux /tmp/pwb/chromium_headless_shell-1194/chrome-linux
ln -sfn /nix/store/nw961dvpvik5m19kbay4cg27wxgl3sdv-playwright-chromium-headless-shell/chrome-linux /tmp/pwb/chromium-1194/chrome-linux
```

If that store path is gone too, find the real one rather than guessing:
`find /nix/store -maxdepth 4 \( -name headless_shell -o -name chrome \) -type f | head -20`

Then run render.py detached (the Creative Forge agent's command limit is 600 s):
```
cd /tmp/forge && setsid env PLAYWRIGHT_BROWSERS_PATH=/tmp/pwb python3 render/render.py <job> > render.log 2>&1 < /dev/null & disown
```

Do NOT `playwright install chromium` (that Chromium lacks libglib, and there is no browser download anyway).

**`pip3 install -q kokoro-onnx soundfile numpy pillow playwright` is required every time** and must be in the
message. render.py imports numpy, soundfile, kokoro_onnx, PIL and playwright, and a message that omits the
pip step fails at `ModuleNotFoundError: No module named 'soundfile'` after the voiceover step. Verify with
`python3 -c "import numpy, soundfile, kokoro_onnx, PIL, playwright; print('deps ok')"` before launching.

/tmp is wiped between Creative Forge agent turns, so every message must re-download the repo, the models and
the shim, and **the detached render must finish inside the same turn** - tell the agent explicitly not to end
its turn while the render is running, and to issue repeated poll commands.

render.py builds the MP4 only. The 1280x720 thumbnail is built by render/thumb.py (added 2026-09-29):
`python3 render/thumb.py <job>` screenshots jobs/<job>/thumb.html at 1920x1080 in Playwright, inlines the logo
the same way render.py does, downscales with PIL and writes out/<job>-thumb.jpg. Run it after render.py, then
copy both files to public/video/.

Serving note (2026-09-29): https://group-creative-service.lovable.app/video/... returns 302 to
https://www.mycreative.group/video/... (mycreative.group is the project's primary domain). Use the
www.mycreative.group URL for YouTube uploads and for links sent to David and Andrea.

**Speaking rate: the voice runs at about 130 wpm, not 157.** Measured on 06 against the Kokoro output
(`vo s5 24.34` for 50 words, `vo s6 17.17` for 39). Budget roughly `words / 130 * 60` seconds of speech, plus
1.0 s padding per scene (0.4 lead + 0.6 tail) plus each scene's `hold`. At 2:15 max that is about **270 words
total**. The first draft of 06 came to 280 words and would have run 2:22; it was trimmed to 253 and landed at
1:56.7.

Chapter timings can be reproduced exactly without re-rendering: run the Kokoro TTS over script.json with the
same voice/speed/lang, pad each scene with 0.4 s lead + 0.6 s tail, add the scene's `hold`, and accumulate.

## Claim check before every upload

Scan script.json AND scenes.html AND thumb.html (on-screen text counts, and the voiceover cannot be fixed
later) for: studio/studios (except the literal back-office screen name "Studio Control"), 99.99, 15+ tech
partners, free sandbox, no credit card, 300% engagement, white-label, turnkey, "a couple of hours". Cleared
claims: 15,000+ games, 100+ game providers, one Universal Game API, SDKs for JavaScript/PHP/Python,
REST/WebSocket/GraphQL, drop-in web-component widgets, back office, bonus engine, local/network jackpots,
real-time reporting, the four steps. CTA is always "Book a walkthrough - iplaygames.ai - hello@iplaygames.ai".
Nothing about the sandbox goes out at all while app_state.iplaygames_sandbox_post_hold stands.

On the figure: the weekly task prompt still says `136+` is unconfirmed, but app_state
`iplaygames_game_providers_count_136` records Andrea confirming it on 2026-10-12 ("games providers - 136 is
ok, its legit") and David on 2026-10-13, and states explicitly that it **overrides any scheduled-task prompt
that still says 136+ is not confirmed**. The word is still governed: "136+ game providers", never "studios".
This run used **100+**, which is correct under either reading and matches the live site.

Also verify by eye, not only by grep: pull frames out of the finished MP4 with ffmpeg and look at them, and
open the thumbnail. Done for 06 this run (frames at 6, 25, 48, 70, 92 and 110 s).
