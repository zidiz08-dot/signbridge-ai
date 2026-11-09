# SignBridge AI

Arabic gesture-to-speech and speech-to-text student innovation prototype.

## Run
Serve `index.html` from HTTPS (GitHub Pages works). Camera requires HTTPS or localhost.

## Training
1. Start camera and wait for MediaPipe hand landmarks.
2. Select a word and record 5–10 distinct examples of its hand pose.
3. Repeat for other words; demonstrate recognition, sentence building and Arabic speech.
4. Export JSON training samples for reuse on another machine.

**Important:** This is a custom static-hand-gesture classifier, not a certified Arabic sign-language translator. It does not understand full sign languages, facial grammar, or moving signs. Recognition quality depends on training and lighting. MediaPipe library and WASM are fetched from public CDNs, and may be unavailable on restricted networks. Speech recognition may use the browser vendor's external service.