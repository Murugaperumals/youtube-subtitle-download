# YouTube Subtitle Download

A simple Python script to download subtitles from YouTube videos.

## Requirements

- Python 3.8+
- yt-dlp

Install yt-dlp:

```bash
pip install -U yt-dlp
```

## Usage

Download English subtitles only:

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download "https://www.youtube.com/watch?v=VIDEO_ID"
```

Example:

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download "https://www.youtube.com/watch?v=Y9hB-XRL5DU"
```

The subtitle file will be saved as:

```
VIDEO_NAME.en.vtt
```

## Convert VTT to TXT

Open the `.vtt` file with any text editor or use a Python script to remove timestamps.
