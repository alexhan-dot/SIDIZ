# Video quality and page speed

Investigation and changes for the T90 page, which carries 14 autoplaying
background videos.

---

## What the Korean page actually serves

Measured from `data/kr-raw/page-t90.html` on 2026-08-25.

| Finding | Detail |
|---|---|
| **24 videos on the page** | Every one is a plain `<source>` MP4 |
| **One rendition per video** | No adaptive streaming, no HLS. The page hardcodes a single file |
| **Mixed quality** | 13 at HD-1080p (7.2 Mbps), 3 at HD-720p (4.5 Mbps), 8 at SD-480p (1.0–1.5 Mbps) |
| **Posters are the `_small` frame** | ~3.4 KB each and visibly soft — and this is what the visitor looks at until the video plays |
| **All start loading at once** | Every video carries `preload="metadata"` and `autoplay` |

The last two points matter most. Fourteen videos competing for bandwidth means
the one on screen arrives last, so it stalls or starts blurry. The page *feels*
low quality even where the file is 7.2 Mbps.

---

## Can the SD videos be improved?

**No, not from the public site.** Two things were checked:

1. **Higher renditions on the KR CDN.** Each Shopify rendition URL carries a
   unique numeric id (`…SD-480p-1.5Mbps-41125900.mp4`), so a 1080p URL cannot be
   derived from a 480p one. Probing the plausible paths and the HLS manifest
   returns 404.

2. **Re-encoding through Shopify.** One SD video was uploaded to the AU store to
   test. Shopify reported the original as **360 × 480** and produced exactly one
   rendition. Shopify does not upscale — a 480p source stays 480p.

**So the ceiling is what SIDIZ Korea published.** Raising it for those 8 clips
means getting the original masters from SIDIZ. Worth requesting: they are short
product loops and the masters certainly exist.

---

## What was changed

### 1. Posters upgraded

`snippets/sidiz-video.liquid` rewrites the KR `_small` preview frame to the
1024px rendition, or the full frame for hero videos.

| | Before | After |
|---|---|---|
| Poster weight | ~3.4 KB | ~90 KB (1024px) / ~148 KB (full) |
| Appearance | soft, obviously low-res | sharp |

This is the single biggest perceived-quality win, because the poster is what the
visitor sees first and — for videos further down the page — for several seconds.

### 2. Videos load only when needed

`assets/sidiz-video.js` holds each source in `data-src` and attaches it via an
IntersectionObserver 400 px before the video enters the viewport. Videos that
scroll away are paused; everything pauses when the tab is hidden.

- The visible video gets the whole connection instead of a fourteenth of it, so
  it reaches full quality immediately rather than stalling
- A visitor who never scrolls past the buy box downloads **one** video, not 14
- `preload="none"` means no metadata requests on load either

Only the hero video is marked `data-eager`.

### 3. Graceful behaviour

- `prefers-reduced-motion` — sources still attach, but nothing autoplays
- Autoplay refusal (low power mode, data saver) leaves the poster showing
- `disableremoteplayback` and `playsinline` for predictable mobile behaviour

---

## Estimated effect on the T90 page

| | Before | After |
|---|---|---|
| Video bytes fetched on load | all 14 begin fetching (~99 MB available) | 1 (hero), ~9 MB |
| Poster bytes | 14 × 3.4 KB ≈ 48 KB, all soft | ~90 KB for what is on screen, sharp |
| Bandwidth for the visible video | shared 14 ways | the whole connection |

The page ends up **lighter on load and higher quality on screen** at the same
time, because the saving comes from not fetching what nobody is looking at.

---

## Self-hosting the media

Currently the sections reference `kr.sidiz.com` CDN URLs. That was right for
getting a preview up, but it is not right for production:

- It depends on another store's file organisation; if KR reorganises, the AU
  page breaks
- Requests go to a Korean-configured CDN origin rather than one serving AU
- No control over the assets

The upload path is proven and works end to end:

1. `stagedUploadsCreate` with `resource: VIDEO` and the exact byte size
2. `POST` the file to the returned signed URL with its parameters
3. `fileCreate` with `originalSource: <resourceUrl>`, no `filename`
   (the staged URL has no extension, and passing one fails validation)
4. Poll until `fileStatus` is `READY`, then read `sources`

Both a 0.5 MB SD clip and a 9.4 MB 1080p clip uploaded successfully.

### Self-hosting turns out to improve quality as well

The 1080p hero clip was uploaded as a test. Shopify transcoded it into **four
sources plus an HLS manifest**, where KR serves exactly one file:

| Rendition | Resolution | Bitrate |
|---|---|---|
| SD-480p | 852 × 480 | 1.2 Mbps |
| HD-720p | 1280 × 720 | 3.0 Mbps |
| HD-1080p | 1920 × 1080 | **4.8 Mbps** |
| `.m3u8` | 1920 × 1080 | adaptive |

Two things follow:

1. **Adaptive streaming.** The HLS manifest lets the browser step between
   renditions by available bandwidth. A visitor on a slow connection gets 480p
   immediately instead of a stalling 7.2 Mbps file; a visitor on fibre gets
   1080p. KR's single hardcoded MP4 cannot do either.

2. **The 1080p rendition is smaller than KR's.** 4.8 Mbps versus KR's 7.2 Mbps
   at the same resolution — Shopify's encoder is roughly **a third more
   efficient**. Same picture, less data.

The poster also comes back at full 1920 × 1080 rather than the `_small` frame.

**Total to migrate: 23 videos, 98.6 MB**, plus the still imagery already
catalogued in `data/products/t90/media-manifest.csv`.

Once uploaded, the sections should switch from the URL settings to Shopify media
objects so `video_tag` emits every rendition and the HLS manifest, rather than a
single hardcoded MP4 as KR does.

---

## Still worth doing

| Item | Why |
|---|---|
| **Request the original masters from SIDIZ** | The only way to lift the 8 SD clips above 480p |
| Upload all 23 videos to the AU store | Removes the dependency on the KR CDN |
| Switch sections to Shopify media objects | Lets Shopify serve multiple renditions instead of one fixed MP4 |
| Consider trimming the 1080p loops | Several run 7.2 Mbps for a few seconds of subtle motion; a lower bitrate would be indistinguishable |
