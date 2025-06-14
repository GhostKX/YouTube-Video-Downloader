from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess

# 🔗 YouTube video link
url = "https://www.youtube.com/link"

try:
    # 🎬 Create a YouTube object with progress bar
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"🎥 Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"⏱️ Duration: {yt.length} seconds\n")

    # 📦 Get video stream (highest resolution, no audio)
    print("🎞️ Getting video stream...")
    video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4') \
                             .order_by('resolution').desc().first()

    # 🎧 Get audio stream (best available)
    print("🎧 Getting audio stream...")
    audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4') \
                             .order_by('abr').desc().first()

    # ⬇️ Download video and audio separately
    print("⬇️ Downloading video stream...")
    video_path = video_stream.download(filename='temp_video.mp4')

    print("⬇️ Downloading audio stream...")
    audio_path = audio_stream.download(filename='temp_audio.m4a')

    # 🧪 Check codecs and decide whether to re-encode
    print("\n🔍 Checking codecs...")
    video_codec = video_stream.video_codec or ""
    audio_codec = audio_stream.audio_codec or ""

    print(f"🎞️ Video codec: {video_codec}")
    print(f"🎧 Audio codec: {audio_codec}")

    if ("avc1" in video_codec.lower() or "h264" in video_codec.lower()) and "mp4a" in audio_codec.lower():
        print("✅ Codecs are compatible. No re-encoding needed.")
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            "final_video.mp4"
        ], check=True)
    else:
        print("⚠️ Incompatible codecs. Re-encoding video...")
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-preset", "superfast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            "final_video.mp4"
        ], check=True)
        print("✅ Video is successfully re-encoded.")

    print("\n✅ Video and audio merged successfully!")

except Exception as e:
    print(f"\n❌ An error occurred: {e}")

finally:
    # 🧹 Clean up temporary files
    print("\n🧹 Cleaning up temporary files...")
    if os.path.exists("temp_video.mp4"):
        os.remove("temp_video.mp4")
        print("🗑️ Removed: temp_video.mp4")
    if os.path.exists("temp_audio.m4a"):
        os.remove("temp_audio.m4a")
        print("🗑️ Removed: temp_audio.m4a")

    print("\n🎉 Done!")
