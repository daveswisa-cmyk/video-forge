# video-forge
Video Forge - renders brand videos from a scenes.html + script.json spec (Playwright + ffmpeg + Kokoro voice). Outputs are copied to the Creative Forge Lovable project (public/video/) and served from https://www.mycreative.group/video/.

## iPlayGames YouTube series (channel UCS49xZKWV4YrFFeqxtbYvYg)

| # | Topic | Job | Status |
|---|-------|-----|--------|
| 01 | One integration, 15,000+ games (Universal Game API) | jobs/iplaygames-video-01 | LIVE https://www.youtube.com/watch?v=Mes2zHsSutE (2026-09-02) |
| 02 | The real cost of game content is the integration, not the rev-share | jobs/iplaygames-video-02 | LIVE (unlisted) https://www.youtube.com/watch?v=LAkEfhBi37s (uploaded 2026-09-15) |
| 03 | List, filter, launch: the Universal Game API in 90 seconds (code-first) | jobs/iplaygames-video-03 | LIVE (unlisted) https://www.youtube.com/watch?v=Px5KCcNsb20 (uploaded 2026-09-15) |
| 04 | One tag, live jackpot: drop-in widgets | jobs/iplaygames-video-04 | UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=GbLU0eX94NI (1:34, 4.17 MB). Custom thumbnail set. Awaiting Andrea's review before going public. |
| 05 | Freespins, cashback, tournaments: the bonus engine | jobs/iplaygames-video-05 | RE-RENDERED + UPLOADED UNLISTED 2026-10-20 https://www.youtube.com/watch?v=yeCg-O8PqO4 (1:41, 4.49 MB). Custom thumbnail set. Awaiting Andrea's review before going public. |
| 06 | How to evaluate a casino game aggregator before you sign | - | NOT PRODUCED. Held 2026-10-06, 2026-10-13 and again 2026-10-20 - see "Production hold" below |
| 07 | From signed to live: four steps with an aggregator | - | planned |

After 07: propose new topics to David instead of repeating.

## 2026-10-20 run: the hold was the wrong approver, not the backlog

The 10-06 and 10-13 runs held production because 04 and 05 were finished but unapproved. That
was the right call on the information those runs had. This run found the actual cause and
cleared it.

**What was wrong.** 04 and 05 were recorded here as "AWAITING DAVID'S APPROVAL" and escalated to
David three times. David is not the approver for iPlayGames. **Andrea Naslauski is the decider for
iPlayGames** (app_state.approval_policy_iplaygames `still_true`, and the weekly task prompt itself).
Every reminder for four weeks went to the wrong person, and Andrea was never shown either video.
That is why the channel published nothing between 2026-09-15 and 2026-10-20.

**The gate those videos were waiting behind no longer exists.** app_state.publish_policy, set by
David on 2026-10-13, removed per-post approval for every company: a post is shown in its room, a
change asked for up to an hour before publication goes into the next version, and the post goes out
either way. "An approver who has not answered" is listed explicitly under
`what_is_no_longer_a_reason_to_stop`. app_state.approval_policy_iplaygames was marked SUPERSEDED on
2026-10-14 for still saying otherwise.

**So both videos were uploaded as `unlisted`.** Unlisted is this channel's normal resting state - 02
and 03 have been unlisted since September - so this is staging, not publication. It is invisible to
the public and to subscribers (`notify_subscribers=false`), and it is reversible. The
unlisted -> public flip is still a human decision and was NOT taken by this run.

### Video 05 was not fit to publish, and nobody had noticed

While checking claims before upload, 05 was found to break app_state.wording_rule_iplaygames
(Andrea, 2026-10-05: never "studio"/"studios" for a game supplier) in three places:

- `script.json` s5 voiceover: "a hundred plus **studios**" - baked into the Kokoro audio
- `scenes.html` s5 chip, on screen: "100+ **studios**"
- `scenes.html` s3 code block, on screen: `games: 'selected **studios**'`

The render predates her ruling by six days, so the words were correct when made and wrong by the
time anyone looked. A description fix would not have helped: two of the three are on screen and one
is in the audio. The job files were fixed to "game providers" / "selected providers" (commits
854949a, b7acf51), 05 was re-rendered, redeployed, and both frames were checked by eye before
upload. 04 was scanned the same way and was clean - no forbidden claim, no "studios".

New scene starts after the re-render (the longer line shifts s6): 0.00, 11.70, 30.03, 46.70, 68.20,
**86.00** s; total **100.289** s. The old table (s6 at 85.70, total 100.0) is stale.

### Verified on 2026-10-20

- YouTube Data API `search?forMine=true` returned exactly 3 videos (01, 02, 03) before this run.
- Both new uploads read back `uploadStatus: processed`, `processingStatus: succeeded`,
  `privacyStatus: unlisted`, `hasCustomThumbnail: true`, HD.
- **Raw HTTP to www.mycreative.group works from this sandbox** - the 10-06 and 10-13 runs recorded it
  as blocked (403 at the proxy). Both MP4s and both thumbnails were downloaded, `ffprobe`d and the
  thumbnails opened and looked at. Serving no longer has to be verified at the project-file level.
- The channel **is** phone-verified: `upload_video_thumbnail` succeeded for both and maxres 1280x720
  came back. The youtube.com/verify note can be dropped.

### Why 06 was still not produced

Unchanged and still correct: two finished videos are now staged but neither has been seen by the
decider. Adding a third would be inventory, not progress. 06 is also the most editorially sensitive
in the series (a neutral evaluation checklist drawn from the /guides competitor-alternatives pages)
and still wants David's direction before scripting. Produce it once 04 and 05 are public.

### Open: Andrea cannot be reached from the scheduled run

**This is now the binding constraint on the series.** The Telegram connection available to the
weekly task is the Zapier bot **@Monsterslotreportbot**, and it is **not a member of the iPlayGames
room -5537782973** - `send_message` returns `Bad Request: chat not found`. The same call to David's
private chat 6336470366 succeeds, so the connection itself is healthy. The room is reachable by the
hub's own approvals bot (public.telegram_send_log shows message 1989 delivered there at
2026-10-20 03:56Z), which runs inside the B2BLeeds project and is a different bot.

So this run could not show Andrea either video. David was told in Hebrew on 2026-10-20 and asked to
forward the two links and to add the bot to the room.

**Next run:** if @Monsterslotreportbot is in room -5537782973, send Andrea both links first thing. If
it still is not, do not retry the same call expecting a different result - report it as a blocked
channel. Either way, if Andrea has asked for no changes, the publish_policy of 13 Oct means the two
videos go public (oldest first) rather than waiting further; then produce 06.

### Also open: "studios" is in the three live videos

01, 02 and 03 say "studios" in the **voiceover and on screen**, and their YouTube descriptions say
"100+ studios" (03's description also says "Filter by studio and category"). They were uploaded
before Andrea's 5 Oct ruling. The descriptions can be corrected with `videos.update` in minutes; the
audio and the scene cards cannot, short of re-rendering and replacing three live videos. This run did
**not** touch them - replacing live videos is Andrea's and David's decision, not an unattended run's,
and fixing only the descriptions would leave the narration contradicting them. Put the choice to
Andrea with the videos.

### Correction to the weekly task prompt

The task prompt still says `136+` is unconfirmed and must not appear. app_state
`iplaygames_game_providers_count_136` records Andrea confirming the figure on 2026-10-12 ("games
providers - 136 is ok, its legit") and David on 2026-10-13, and states explicitly that it
**overrides any scheduled-task prompt that still says 136+ is not confirmed**. The word is still
governed: "136+ game providers", never "studios". This run used **100+**, which is correct under
either reading and matches the live site. David was asked to update the prompt.

## Render notes

Run render.py detached (the Creative Forge agent's command limit is 600 s):
`setsid env PLAYWRIGHT_BROWSERS_PATH=/nix/store/pp3i69v0m7vh8nicq8f4pbabc2awhm1g-playwright-browsers-with-overrides python3 render/render.py <job> > render.log 2>&1 < /dev/null & disown`
Do NOT `playwright install chromium` (that Chromium lacks libglib). /tmp is wiped between Creative
Forge agent turns, so every message must re-download the repo.

render.py builds the MP4 only. The 1280x720 thumbnail is built by render/thumb.py (added 2026-09-29):
`python3 render/thumb.py <job>` screenshots jobs/<job>/thumb.html at 1920x1080 in Playwright, inlines
the logo the same way render.py does, downscales with PIL and writes out/<job>-thumb.jpg. Run it after
render.py, then copy both files to public/video/.

Serving note (2026-09-29): https://group-creative-service.lovable.app/video/... returns 302 to
https://www.mycreative.group/video/... (mycreative.group is the project's primary domain). Use the
www.mycreative.group URL for YouTube uploads and for links sent to David and Andrea.

Chapter timings can be reproduced exactly without re-rendering: run the Kokoro TTS over script.json
with the same voice/speed/lang, pad each scene with 0.4 s lead + 0.6 s tail, add the scene's `hold`,
and accumulate.

## Claim check before every upload

Scan script.json AND scenes.html AND thumb.html (on-screen text counts, and the voiceover cannot be
fixed later) for: studio/studios (except the literal back-office screen name "Studio Control"),
99.99, 15+ tech partners, free sandbox, no credit card, 300% engagement, white-label, turnkey,
"a couple of hours". Cleared claims: 15,000+ games, 100+ game providers, one Universal Game API, SDKs
for JavaScript/PHP/Python, REST/WebSocket/GraphQL, drop-in web-component widgets, back office, bonus
engine, local/network jackpots, real-time reporting, the four steps. CTA is always
"Book a walkthrough - iplaygames.ai - hello@iplaygames.ai". Nothing about the sandbox goes out at all
while app_state.iplaygames_sandbox_post_hold stands.
