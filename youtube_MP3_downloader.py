import youtube_dl
import sys
import os
import time

save_path = '/'.join(os.getcwd().split('/')[:3])+'\Music'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': save_path + '/%(title)s.%(ext)s',
}

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


if __name__ == "__main__":
    path = input('Set .txt path >> ')
    url = open(path)
    url = url.readlines()
    for i in url:
        download(url)
    input('Press enter to leave: ')
    

#C:\Users\Giuliano\OneDrive\Escritorio\links.txt
