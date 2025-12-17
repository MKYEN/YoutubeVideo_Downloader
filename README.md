# FFmpeg Installation for yt-dlp on Windows

This document describes how to install FFmpeg on Windows and how it is used together with yt-dlp to download the highest available quality from YouTube.

---

## Why FFmpeg Is Required

YouTube delivers high-quality content using separate video and audio streams (DASH).  
yt-dlp requires FFmpeg to merge these streams into a single playable media file.

Without FFmpeg, high-resolution downloads cannot be merged.

---

## Downloading FFmpeg

FFmpeg is not a Python package and cannot be installed using pip.

Download a Windows build from the official source:

https://www.gyan.dev/ffmpeg/builds/

Download the following archive from **Release builds**:

```
ffmpeg-release-essentials.zip
```

---

## Installing FFmpeg

Extract the downloaded archive.

Create the following directory:

```
C:\ffmpeg
```

Copy the extracted files so the final structure is exactly:

```
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe
C:\ffmpeg\bin\ffplay.exe
```

This location avoids permission issues and keeps FFmpeg independent from Python projects.

---

## Adding FFmpeg to Windows PATH

Add the FFmpeg `bin` directory to the system PATH.

Open **Environment Variables** (`Win + R` → `sysdm.cpl`)  
Go to **Advanced → Environment Variables**

Under **System variables → Path**, add:

```
C:\ffmpeg\bin
```

Close all terminals and open a new one.

---

## Verifying Installation

Verify that FFmpeg is available system-wide:

```
ffmpeg -version
```

If FFmpeg prints version and configuration details, installation is complete.

---

## Required FFmpeg Components

The official FFmpeg build already includes all required libraries.

The following executables must exist:

```
ffmpeg.exe
ffprobe.exe
ffplay.exe
```

yt-dlp uses FFmpeg via command line and does not require Python bindings.

---

## Python Script Using yt-dlp and FFmpeg

The following script downloads the **highest available quality** from YouTube.

```python
import yt_dlp

url = input("Enter video URL: ").strip()

ydl_opts = {
    "format": "bestvideo*+bestaudio/best",
    "merge_output_format": "mp4",
    "ffmpeg_location": r"C:\ffmpeg\bin",
    "nocheckcertificate": True,
    "postprocessor_args": {
        "ffmpeg": [
            "-movflags", "+faststart",
            "-fflags", "+genpts",
            "-avoid_negative_ts", "make_zero",
            "-vsync", "vfr"
        ]
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed with the highest available quality.")
```

---

## Code Explanation

The `format` option selects the best available video and audio streams provided by YouTube.  
If separate streams are unavailable, yt-dlp falls back to the best combined format.

`merge_output_format` defines MP4 as the output container for maximum compatibility.

`ffmpeg_location` explicitly tells yt-dlp where FFmpeg is installed, avoiding PATH dependency.

`nocheckcertificate` disables strict TLS validation required on some Windows systems.

The FFmpeg post-processing arguments improve synchronization and seek behavior by regenerating timestamps, preventing negative offsets, and optimizing MP4 indexing.

---

## Summary

FFmpeg must be installed manually and added to the system PATH.  
Once available, yt-dlp automatically uses FFmpeg to merge the highest-quality video and audio streams into a single MP4 file.
