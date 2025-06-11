import os
import subprocess
import datetime
from pytubefix import YouTube
from pytubefix.cli import on_progress

url="https://www.youtube.com/link"

print(datetime.datetime.now())
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

audio_stream = yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').order_by('abr').desc().first()
audio_path = audio_stream.download(filename='temp_audio.m4a')

fixed_audio_path = "final_audio.m4a"
subprocess.run([
    "ffmpeg",
    "-y",
    '-i', audio_path,
    "-c:a", "aac",
    fixed_audio_path])

final_audio_path = "final_audio.mp3"
subprocess.run([
    "ffmpeg", "-y",
    "-i", fixed_audio_path,
    "-vn",
    "-c:a", "libmp3lame",
    "-q:a", "1",
    final_audio_path
])
print(datetime.datetime.now())

os.remove(audio_path)
os.remove(fixed_audio_path)

print(f"Finished! Final MP3 saved as: {final_audio_path}")
