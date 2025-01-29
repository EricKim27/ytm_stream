import yt_dlp
import subprocess
from pytubefix import Playlist, YouTube
import time
import datetime
ydl_option = {
    'format': 'bestaudio/best',
    'quiet': True,
    'extract_audio': True,
    'audioquality': 0,  # Best quality audio
    "cookiefile": "cookies.txt",
}

def play_audio(url: str):
    with yt_dlp.YoutubeDL(ydl_option) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']
        title = info['title']
        duration = str(datetime.timedelta(seconds=int(info['duration'])))
        print(f"{title}")
        ffmpeg_cmd = [
            'ffplay',
            '-i', audio_url,  # Input is the audio URL
            '-loglevel', 'quiet',  # Suppress logs
            '-nodisp',  # No display (audio-only)
            '-autoexit',  # Close after playback
            '-reconnect', 
            '1', 
            '-reconnect_streamed', 
            '1', 
            '-reconnect_delay_max', 
            '5'
        ]
        process = subprocess.Popen(ffmpeg_cmd)
        start_time = time.time()

        while process.poll() is None:
            elapsed = time.time() - start_time
            print(f"\r{str(datetime.timedelta(seconds=int(elapsed)))} | {duration}", end="")
            time.sleep(1)

        

class playlist:
    def __init__(self, url:str):
        self.plist = Playlist(url)
        self._stop = False
    def stop(self):
        self._stop = True

    def play_items(self):
        for vurl in self.plist.video_urls:
            if self._stop:
                print("Playback stopped.")
                break
            play_audio(vurl)