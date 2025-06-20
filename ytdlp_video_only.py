import yt_dlp
import subprocess


# 🔗 Ask the user for the YouTube video URL
url = input("🎥 Enter YouTube video URL: ").strip()

output_path = 'video_only.mp4'
fixed_path = 'video_only_fixed.mp4'

# ⚙️ yt_dlp configuration
ydl_opts = {
    'format': 'bestvideo[ext=mp4][vcodec^=avc1]',        # 🎞️ H.264 (AVC1) video in MP4
    'outtmpl': f'{output_path}',                         # 💾 Output file name
    'noplaylist': True,                                  # 🚫 Only download one video
    'quiet': False,                                      # 📢 Show progress output
}

try:
    print("⬇️ Downloading H.264 MP4 video...\n")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        download_path = ydl.download([url])

    # Remux video to fix timestamps, without re-encoding
    cmd = [
        "ffmpeg",
        "-i", output_path,
        "-c", "copy",
        "-fflags", "+genpts",
        fixed_path,
        "-y"
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("\n✅ Download completed successfully!")
    print("📂 Saved as: video_only_fixed.mp4")

except Exception as e:
    print(f"\n❌ An error occurred:\n{e}")
