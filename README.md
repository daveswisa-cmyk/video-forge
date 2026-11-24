# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://www.mycreative.group/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | UPLOADED UNLISTED 2026-09-02 https://www.youtube.com/watch?v=Mes2zHsSutE (earlier rows here called this one LIVE/public; it is unlisted, checked 2026-11-10) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | UPLOADED UNLISTED https://www.youtube.com/watch?v=LAkEfhBi37s (uploaded 2026-09-15) |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | jobs/iplaygames-video-03 | UPLOADED UNLISTED https://www.youtube.com/watch?v=Px5KCcNsb20 (uploaded 2026-09-15) |
| 04 | One tag, live jackpot: drop-in widgets | jobs/iplaygames-video-04 | UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=GbLU0eX94NI (1:34, 4.17 MB). Custom thumbnail set. SHOWN TO ANDREA BY EMAIL 2026-10-27. |
| 05 | Freespins, cashback, tournaments: the bonus engine | jobs/iplaygames-video-05 | RE-RENDERED + UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=yeCg-O8PqO4 (1:41, 4.49 MB). Custom thumbnail set. SHOWN TO ANDREA BY EMAIL 2026-10-27. |
| 06 | How to evaluate a casino game aggregator before you sign | jobs/iplaygames-video-06 | UPLOADED UNLISTED 2026-11-03 https://www.youtube.com/watch?v=KYxW98HXRIs (1:56.7). Shown to Andrea in room -5537782973; she replied "Video seems ok" at 2026-11-03 07:30:39Z. |
| 07 | From signed to live: four steps with an aggregator | jobs/iplaygames-video-07 | UPLOADED UNLISTED 2026-11-10 https://www.youtube.com/watch?v=dUXo33gaR3k (1:53.8, 4,398,983 bytes, 1920x1080 h264 + aac, 3414 frames @30fps). Custom thumbnail set. Shown to Andrea in room -5537782973, message 2748. |

**STATUS CORRECTION 2026-11-24 - the Status column above is stale for 04-07. Read this line first.**
04 `GbLU0eX94NI`, 05 `yeCg-O8PqO4`, 06 `KYxW98HXRIs` and 07 `dUXo33gaR3k` are **PUBLIC** since 2026-11-24 07:12Z,
on Andrea's written approval. 01 `Mes2zHsSutE`, 02 `LAkEfhBi37s` and 03 `Px5KCcNsb20` are still **unlisted** and
stay that way until someone re-renders them - they say "studios" in the voiceover, on the scene cards and in
their YouTube descriptions. See the 2026-11-24 run section below.



After 07: propose new topics to David instead of repeating.

Scene starts for 06 (30 fps): 0.000, 10.600, 33.133, 56.567, 79.333, 100.000 s; total 116.667 s.

## 2026-11-24 run: Andrea had already said yes, a week ago. 04-07 are now public

**The approval was sitting in the database the whole time.** The 11-17 run asked her one yes/no in message 2875
at 07:10:10Z and ended. She replied **"yes"** at **2026-11-17 07:11:47Z** - 97 seconds later - as a direct reply
to 2875 (`telegram_updates` update_id 428973181, `outcome` recorded_fallback+request:240). The run was already
over, nothing read the table afterwards, and the registry row kept saying "Waiting on her answer" for seven days
while the answer was two minutes old. **Check `telegram_updates` for replies to our own last message BEFORE
deciding there is nothing to do** - that single query is what unblocked ten weeks of work this run.

**What was done.** `videos.update` with `part=status` on the four approved ids, one at a time, preserving
`license`, `embeddable`, `publicStatsViewable` and `selfDeclaredMadeForKids` in each body (videos.update clears
mutable fields you omit inside the parts you name - do not send a bare privacyStatus). Then re-read
`videos?part=status` for all seven as a separate verification call:

| # | id | before | after |
|---|-----|--------|-------|
| 01 | Mes2zHsSutE | unlisted | unlisted (held) |
| 02 | LAkEfhBi37s | unlisted | unlisted (held) |
| 03 | Px5KCcNsb20 | unlisted | unlisted (held) |
| 04 | GbLU0eX94NI | unlisted | **public** |
| 05 | yeCg-O8PqO4 | unlisted | **public** |
| 06 | KYxW98HXRIs | unlisted | **public** |
| 07 | dUXo33gaR3k | unlisted | **public** |

**Descriptions were checked before flipping, not after.** All four of 04-07 say "100+ game providers" and carry
no held claim, so they clear `wording_rule_iplaygames` as they stand. 01, 02 and 03 say "100+ studios" in their
descriptions, "studios" in the narration and on the scene cards, and 03 even has a chapter titled "Filter by
studio and category". Descriptions alone are a `videos.update` away, but fixing only those would leave the
narration contradicting them, so all three stay unlisted until they are re-rendered. Offered to Andrea; her call.

**No video 08, and this time that is the end state rather than a hold.** The series is complete through 07 and
the brief says propose new topics after 07. The 11-17 run reached the same conclusion but left the lane with
nothing to do next; this run closed it out by putting the choice to David with the work prepared:
distribution of the four now-public videos (embed on the matching iplaygames.ai pages, post on LinkedIn page
139353974, build a playlist and channel art) against three untouched topics (back-office reports and analytics;
a second neutral guide video from `/guides/softswiss-alternatives`; Game Management + Media Library).
**Recommended distribution**, on the evidence: ten weeks of production bought 7 views in total, so reach is the
binding constraint and an eighth video does not touch it. Registry row c644c6e6 now points at David,
`next_action_at` 2026-11-27.

**Messages sent.** Andrea in room -5537782973 via the hub send path, message **3054**, `telegram_send_log` row
1103, 07:11:44Z, 200 OK - told the four are public and that the three older ones can be redone if she wants.
Kept well under the 400-character group cap. David in 6336470366, message 123, 07:12:35Z, via the Zapier
Telegram bot, which works for his private chat.

**Unchanged and still worth ten seconds of David's time:** @Monsterslotreportbot is still not a member of room
-5537782973. Not retried this run - the hub send path is the working route and there is no reason to keep
re-testing a known failure. Asked again, framed as non-blocking.



## 2026-11-17 run: no video 08. The series is finished and the problem is distribution, not supply

**Nothing was produced this week, on purpose.** The brief says the series runs 02 to 07 in order and that
after 07 the next step is to propose new topics to David, not to repeat. 07 was uploaded on 2026-11-10, so
the production queue is empty and there is no "next number" to make. Checking the channel before writing a
script is what caught this; the `jobs/` folder alone would have shown the same thing.

**What ten weeks of weekly production has actually produced.** Checked against
`videos?part=status,statistics` on 2026-11-17: all seven videos are `privacyStatus: unlisted`, and the total
view count across the whole series is **7** - 01:1, 02:0, 03:1, 04:2, 05:3, 06:0, 07:0. An unlisted video is
reachable only by direct link, so the channel has no audience and the videos cannot be found, shared, or
indexed. Producing an eighth video into that state would add inventory, not reach. **The bottleneck is not
content. It is that nothing is public.**

**Why nothing was flipped public by this run.** Every video was uploaded unlisted because the task prompt
says `privacy_status unlisted`, so unlisted was the instruction, not an oversight or a stalled approval.
Changing it is therefore a new decision rather than the completion of an old one, and
`app_state.publish_policy` does not cover it: that policy governs a post going out at its scheduled time,
and these have no scheduled publication. The decision belongs to Andrea, who decides every iPlayGames post.

**Andrea answered the 07 notice, and it was not an approval.** Message 2748 (the 07 notice, 2026-11-10) got a
reply in room -5537782973 on 2026-11-15 10:24:54Z: *"I am not sure what should I do with those videos?"* -
plus, on message 2752, *"can we add images to those posts?"* and *"and why there are ctas if its not
clickable."* (the last two are about LinkedIn creatives, not the videos). Earlier runs treated "Video seems
ok" (06, 2026-11-03) as sufficient, but nothing in the thread has ever asked her the one question that
matters. The notices sent her links and scripts and never said the videos were invisible or that a yes/no was
needed. That is a drafting failure on our side, not hesitation on hers.

**What was sent this run.** A short message in her room asking exactly one yes/no: can 04, 05, 06 and 07 be
made public. 01, 02 and 03 were deliberately excluded - they say "studios" in the voiceover and on the scene
cards, from before her 5 October ruling (`app_state.wording_rule_iplaygames`), and the audio cannot be fixed
without re-rendering and replacing live videos. Sent via the hub's own send path from the B2BLeeds project
(`POST /api/public/hooks/telegram-send`), HTTP 200, Telegram message 2875, `telegram_send_log` row 974,
2026-11-17 07:10:10Z. Registry row c644c6e6 updated the same run: `next_action_at` 2026-11-20,
`next_action_owner` Andrea.

**Two things worth carrying forward.**
1. The Zapier Telegram bot @Monsterslotreportbot is *still* not a member of room -5537782973 - `send_message`
   returned `Bad Request: chat not found` again this run (tested once, not retried). The hub send path is the
   working route. David was asked to add the bot on 2026-10-27 and it has not happened; it is a ten-second fix
   worth asking for again, but it is not blocking anything.
2. **Group rooms are capped at 400 characters** (rule of 2026-11-14). The first draft of this run's message
   was 873 characters and the send path refused it with `422 too_long`, logging to `telegram_blocked_sends`.
   The only override is `allow_long: "post_text"`, which is for a post's own text and was *not* used - the cap
   exists to stop workers flooding rooms. Write notices to Andrea at 400 characters or fewer, or they do not
   send.


## 2026-11-10 run: the series is complete through 07, and the room was never actually unreachable

**What the 2026-11-03 run left behind.** It uploaded 06 unlisted (KYxW98HXRIs), wrote jobs/iplaygames-video-07 and rendered
it to https://www.mycreative.group/video/iplaygames-video-07.mp4 - and then updated neither this README nor the
campaign_registry row. So the repo said 06 was unrendered and 07 was "planned" when both were done, and row
c644c6e6 sat 7 days past its next_action_at. Write the record in the same run as the work, or the next run starts
from a false picture and risks redoing finished work.

**The notice channel: correct the diagnosis carried since 2026-10-20.** The Zapier Telegram bot
@Monsterslotreportbot is still not a member of room -5537782973 and `send_message` still returns
`Bad Request: chat not found` (tested once this run, not retried). That is a fact about THAT BOT, not about the room.
The room is busy: the hub approvals bot posts into it daily and Andrea replied in it on 3, 4, 5, 6 and 8 November.
The working route, used this run, is the hub's own send path - from the B2BLeeds Lovable project
(9d49e503-833d-4fe1-8b80-a34682fc222b), `POST /api/public/hooks/telegram-send` with the approvals cron token the
project already holds, which logs itself into `public.telegram_send_log`. Message 2748, 2026-11-10 07:13:09Z.
**Use this route. Do not email Andrea as a workaround and do not record the room as unreachable.**

**The open decision, and why nothing was made public this run.** All seven videos are unlisted - checked against
`videos?part=status` on 2026-11-10, including 01, which both this README and the registry row wrongly called public.
So ten weeks of weekly production has produced a channel with no publicly visible video and no audience. That is the
thing worth deciding, and it is Andrea's: asked in her room whether 04, 05, 06 and 07 can go public, noting that 01,
02 and 03 still say "studios" in the narration and on the scene cards (app_state wording_rule_iplaygames) and would
need re-rendering before they could. Privacy was never part of this lane's brief - every video was uploaded unlisted
because the task prompt says unlisted - so flipping them is a new decision and not one to take unasked.

**Claim check for 07.** script.json, scenes.html and thumb.html scanned; the only hit is "Studio Control", the literal
back-office screen name, which is allowed. 15,000+ games and 100+ game providers. No sandbox reference
(app_state iplaygames_sandbox_post_hold). CTA iplaygames.ai / hello@iplaygames.ai. Frames at 5, 22, 45, 68, 90 and
110 s plus the thumbnail looked at by eye: clean brand cards, no photograph, logo and type correct.

Scene starts for 07 (measured off the finished MP4 at 4 fps): 0.00, 11.00, 37.00, 58.75, 78.00, 100.75 s; total 113.8 s.
Script was 244 words, which at the measured ~130 wpm predicted ~2:05 and landed at 1:53.8.

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
