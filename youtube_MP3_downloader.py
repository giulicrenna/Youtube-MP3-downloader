import youtube_dl
import os
import time

print("Youtube downloader by Giuliano Crenna\n\n")

current_path = os.getcwd()
save_path = os.path.join(current_path, 'music')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': save_path + '/%(title)s.%(ext)s',
}

def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download((url,))

def converter():
    f = []
    for (dirpath, dirnames, filenames) in os.walk(save_path):
        f.extend(filenames)
        break
    for file in f:
        try:
            file = str(file)
            if file.endswith('.m4a'):
                new_name = os.path.join(save_path ,file.removesuffix('.m4a') + '.mp3')
                old_name = os.path.join(save_path, file)
                try:
                    os.rename(old_name, new_name)
                except:
                    pass 
                os.remove(old_name)
            if file.endswith('.webm'):
                new_name = os.path.join(save_path ,file.removesuffix('.webm') + '.mp3')
                old_name = os.path.join(save_path, file)
                try:
                    os.rename(old_name, new_name)
                except:
                    pass  
                os.remove(old_name)         
        except Exception as e:
            print(e)
            pass     
    print("Convertion DONE!")

if __name__ == "__main__":
    print("--MENU--\n\n1) To download a single song or a playlist\n2) To download multiple songs\n")
    opcion = input("Digite la opción >> ")
    if opcion == "1":
        while True:
            try:
                converter()
                cancion = input("Youtube link>> ")
                download(cancion)
            except:
                print("Exception while downloading the song")
                time.sleep(1)
                pass
    if opcion== "2":
        path = input('Set .txt path >> ')
        url = open(path)
        url = url.readlines()
        for i in url:
            try:
                download(i)
                converter()
            except:
                print("Exception while downloading the song")
                time.sleep(1)
                pass
        input('Press enter to leave: ')
    else:
        print("\n\nIncorrect choice")
            

