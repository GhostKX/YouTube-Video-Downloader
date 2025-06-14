from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess

# 🔗 Paste your YouTube video URL here
url = "https://www.youtube.com/link"

try:
    print("\n🚀 Starting download...\n")

    # 🎬 Create a YouTube object with progress feedback
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"🎥 Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"📏 Length: {yt.length} seconds\n")

    # 📦 Get the best adaptive video stream (video-only, .mp4)
    print("🎞️ Fetching highest resolution video-only stream...")
    video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4') \
                             .order_by('resolution').desc().first()

    # ⬇️ Download the video stream
    print(f"\n⬇️ Downloading video: {yt.title}")
    video_path = video_stream.download(filename="video_only.mp4")
    print("✅ Download complete!\n")

    # 🧪 Check video codec to decide on re-encoding
    video_codec = video_stream.video_codec or ""
    print("🔍 Checking video codec compatibility...")
    print(f"🎞️ Detected codec: {video_codec}")

    if "avc1" in video_codec.lower():
        print("✅ Video is already H.264 (avc1) encoded — no re-encoding needed.")

        # Rename for consistency
        if os.path.exists("video_compatible.mp4"):
            os.remove("video_compatible.mp4")
        os.rename(video_path, "video_compatible.mp4")

    else:
        print("⚠️ Video is not H.264. Re-encoding for compatibility...")

        output_path = "video_compatible.mp4"

        # Re-encode using ffmpeg
        subprocess.run([
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "23",
            "-an",  # No audio
            "-movflags", "+faststart",
            "-vf", "scale='min(1920,iw)':-2",  # Ensure it doesn't exceed 1080p
            output_path
        ], check=True)
        print("✅ Video is successfully re-encoded.")

        # 🧹 Clean up original incompatible video
        os.remove(video_path)
        print("🧹 Removed original video.")

    print(f"\n🎉 Done! Final file: video_compatible.mp4\n")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
