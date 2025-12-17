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