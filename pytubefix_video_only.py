from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import datetime

url="https://www.youtube.com/link"

print(datetime.datetime.now())
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution').desc().first()
print(f'Downloading video: {yt.title}')
video_path = video_stream.download(filename='video_only.mp4')
print('Download complete')


print('Checking re-encoding...')
print(f'Video codec: {video_stream.video_codec}')
if 'avc1' in video_stream.video_codec.lower():

    print("Video is already H.264 encoded - no re-encoding needed")
    if os.path.exists("video_compatible.mp4"):
        os.remove("video_compatible.mp4")
    os.rename(video_path, "video_compatible.mp4")

else:
    print("Re-encoding video to H.264 for compatibility...")
    output_path = "video_compatible.mp4"

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-crf", "23",  #
        "-an",
        "-movflags", "+faststart",
        "-vf", "scale='min(1920,iw)':-2",
        output_path
    ], check=True)

    # Removing the original file
    os.remove(video_path)

print(f'✅ Done: {yt.title}')
print(datetime.datetime.now())

