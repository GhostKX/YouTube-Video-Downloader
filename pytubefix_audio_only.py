import os
import subprocess
import datetime
from pytubefix import YouTube
from pytubefix.cli import on_progress

# 🔗 Your YouTube video URL
url = "https://www.youtube.com/link"

try:
    # 🎬 Create a YouTube object with progress tracking
    print("🔍 Fetching video info...")
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"🎥 Title: {yt.title}")

    # 🎧 Get the best quality audio-only stream (adaptive + mp4 container)
    print("🎧 Selecting best available audio stream...")
    audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4') \
        .order_by('abr') \
        .desc() \
        .first()

    # ⬇️ Download the audio stream as temp .m4a
    print("⬇️ Downloading audio stream...")
    temp_audio_file = "temp_audio.m4a"
    audio_path = audio_stream.download(filename=temp_audio_file)

    # 🧹 Clean .m4a re-encoding step (optional if needed)
    fixed_audio_path = "final_audio.m4a"
    print("🎛️ Converting to clean M4A...")
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", audio_path,
        "-c:a", "aac",
        fixed_audio_path
    ], check=True)

    # 🎵 Convert to high-quality MP3 using libmp3lame
    final_audio_path = "final_audio.mp3"
    print("🎶 Converting M4A to MP3...")
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", fixed_audio_path,
        "-vn",  # No video
        "-c:a", "libmp3lame",
        "-q:a", "1",  # High quality
        final_audio_path
    ], check=True)

    # 🧹 Clean up temp files
    os.remove(audio_path)
    os.remove(fixed_audio_path)

    print(f"\n✅ Finished! Final MP3 saved as: {final_audio_path}")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
