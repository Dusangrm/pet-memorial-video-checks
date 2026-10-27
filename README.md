# Pet memorial video checks

A small offline Python helper for checking a permitted photo-to-video output before sharing it. I build and maintain [Day of the Dead Pet AI](https://dayofthedeadpet-ai.com/). This repository is an independent output-inspection aid; it does not generate video or upload photos.

## Run

Install Python 3 and FFmpeg from their official distributions. Then:

```sh
python3 inspect_clip.py your-pet-video.mp4
```

If FFmpeg is outside PATH, set FFMPEG_PATH to the installed executable. The tool prints JSON containing width, height, measured duration and whether an audio stream exists. A native 720p vertical example is 720 by 1280; ten-second requests may have a slightly longer actual container duration.

## Review beyond metadata

Check markings, muzzle, eyes, ears, paws, ground contact and the entire final pose. A model's success status and a valid MP4 do not establish likeness, good anatomy or appropriate remembrance imagery. Do not use this as a face or identity detector. It does not certify rights, licensing or safety.

For a framed portrait instead of a walking animal, see [Pet Ofrenda AI](https://dayofthedeadpet-ai.com/pet-ofrenda-ai/). The separate [Rainbow Bridge Pet AI guide](https://dayofthedeadpet-ai.com/rainbow-bridge-pet-ai/) explains a quiet garden scene. Instructions and fictional examples are public; personalized generation on the linked site is paid.

## Data and scope

No network requests, credentials, customer photos or customer videos are bundled. Only the named local file is inspected by FFmpeg. No customer data should be attached to repository issues. AI assisted the code and documentation; it was executed against our own fictional golden-retriever sample (720x1280, 10.08 seconds, audio present).

Related adult-portrait project: [Marigold Bridge AI](https://marigoldbridgeai.com/). This helper does not promise reproduction of a viral clip and has no affiliation with Disney or Pixar.
