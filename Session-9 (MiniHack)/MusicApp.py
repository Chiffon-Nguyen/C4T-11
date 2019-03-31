from __future__ import unicode_literals
import youtube_dl
import json

displayOpts = {
    1: 'Show all the songs',
    2: 'Show detail of the song',
    3: 'Play a song',
    4: 'Search and download the song',
    5: 'Exit'
}
musicList = []
manageKey = int(input("Enter an option you want: "))
if manageKey == 4:
    print("____________")
    search = input("Enter a song you want to download: ")
    options = {
        'outtmpl': '%(id)s', # lấy tên file đown về là id của video
        'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        musicInfo = []
        result = ydl.extract_info("https://www.youtube.com/results?search_query=",search, 
        download = False)
        musicInfo.append(result)
    with open('ListMusic.json', 'a') as json_file:
        json.dump(musicInfo, json_file)


