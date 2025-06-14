from pytubefix import YouTube
from pytubefix.cli import on_progress


# 🔗 Insert your YouTube video URL here
url = "https://www.youtube.com/link"

try:
    print("\n🚀 Starting download process...\n")

    # 🎬 Create YouTube object with progress display
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"🎥 Video Title: {yt.title}")
    print(f"📺 Channel: {yt.author}")
    print(f"⏱️ Duration: {yt.length} seconds")

    # 🎯 Select highest resolution video stream
    print("\n📦 Fetching highest resolution stream...")
    ys = yt.streams.get_highest_resolution()

    # 📁 Download video to current working directory
    print("⬇️ Downloading video...")
    download_path = ys.download()
    print(f"✅ Download complete! File saved as:\n📂 {download_path}\n")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
