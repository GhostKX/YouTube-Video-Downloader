from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess
import datetime

url="https://www.youtube.com/link"

print(datetime.datetime.now())
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)


print('Getting the video stream...')
video_stream = yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution').desc().first()

print('Getting the audio stream...')
audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').order_by('abr').desc().first()

print('Downloading video stream...')
video_path = video_stream.download(filename='temp_video.mp4')
print('Downloading audio stream...')
audio_path = audio_stream.download(filename='temp_audio.m4a')


print('Checking the codecs...')
try:
    if 'avc1' in video_stream.video_codec.lower() and 'mp4a' in audio_stream.audio_codec.lower():
        print(f'Video codec: {video_stream.video_codec} and Audio codec: {audio_stream.audio_codec}')
        print('No re-encoding needed')
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            "final_video_4.mp4"
        ])
    else:
        print(f'Video codec: {video_stream.video_codec} and Audio codec: {audio_stream.audio_codec}')
        print('Re-encoding video stream...')
        subprocess.run([
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            "final_video_4.mp4"
        ], check=True)


    print('✅ Done')
    print(datetime.datetime.now())

    print('Removing temporary video file...')
    os.remove(video_path)
    print('Removing temporary audio file...')
    os.remove(audio_path)
except Exception as e:
    print(e)
finally:
    print('Cleaning up temporary video file...')
    if os.path.exists(video_path): os.remove(video_path)
    if os.path.exists(audio_path): os.remove(audio_path)



