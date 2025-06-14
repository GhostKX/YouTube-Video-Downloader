import yt_dlp

# 🔗 Ask the user for the YouTube video URL
url = input("🎥 Enter YouTube video URL: ").strip()


# ⚙️ yt_dlp configuration
ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]',        # 🎞️ H.264 (AVC1) video in MP4
    'outtmpl': 'video_only.mp4',                         # 💾 Output file name
    'noplaylist': True,                                  # 🚫 Only download one video
    'quiet': False,                                      # 📢 Show progress output
}

try:
    print("⬇️ Downloading H.264 MP4 video...\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Download completed successfully!")
    print("📂 Saved as: test.mp4")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
