from __future__ import unicode_literals
import youtube_dl
import json
import pyglet

yourName = str(input("Enter your name: "))
print("Hello", yourName, "this is a music app. \nThere are functions I can help you")
displayOpts = {
    1: 'Show all the songs',
    2: 'Show detail of the song',
    3: 'Play a song',
    4: 'Search and download the song',
    5: 'Exit'
}
for k,v in displayOpts.items():
    print(str(k) + ". " + v)

MusicList = []
music_download = []
chooseOpt = int(input("Enter option: "))
print("____________")
if chooseOpt == 4:
    with open('data_file.json', encoding = "utf-8") as f:
        data = json.load(f)
    music_download = data

    search = input("Enter a song you want to download: ")
    options = {
        'default_search': 'ytsearch5',
        'outtmpl': '%(id)s', # lấy tên file đown về là id của video
        'postprocessors': [{
        'key': 'FFmpegExtractAudio', # Tách lấy audio
        'preferredcodec': 'mp3', # Format ưu tiên là mp3
        'preferredquality': '192', # Chất lượng bitrate
        }],
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        result = ydl.extract_info("https://www.youtube.com/results?search_query="+ search, 
        download = False)
    # with open('Search.json', 'a') as json_file:
    #     json.dump(result, json_file)
    musicInfo = []
    if "entries" in result:
        for i in range(5):
            videoN = result["entries"][i]["title"]
            musicInfo.append(videoN)
            print(str(i + 1) + ". " + musicInfo[i])
    downloadNum = int(input("Enter a number to download: "))
    LinkSongYouChose = result['entries'][downloadNum-1]['webpage_url']
    ydl2 = YoutubeDL(options)
    infoDownload = ydl2.extract_info(LinkSongYouChose, download = True)
    music_download.append(infoDownload)
    with open('data_file.json', 'w') as outfile:  
        json.dump(listSongDowload, outfile)

if chooseOpt == 1:
    with open("data_file.json","r") as listmusic:
        ShowAllSong = listmusic.read(f"{MusicList}")
    ShowAllSong = listmusic
    print(ShowAllSong)
    
if chooseOpt == 2:
    checkDetail = int(input("Enter a song to check detail: "))

if chooseOpt == 3: 
    MusictoPlay = []
    f = open('ListMusic.txt', "r",encoding='utf-8-sig')

    for i in range(len(MusicList)) : 
        print(str(i + 1)+ ". "+ MusicList[i]["title"]) 

    print("Choose a song you want play : ")
    song_number = input("Enter song number from 1 -->  " + str(len(MusictoPlay))+ ": ")
    song_number -= 1
    if song_number.isdigit() :
        if 0 <= int(song_number) < len(MusictoPlay) :
            for i in range(len(MusictoPlay)) :
                if i == int(song_number) : 
                    music = pyglet.resource.media(str(MusictoPlay[i]["title"])+".mp3")
                    music.play()
        else: 
            print("Wrong input! Number must be from 0 -->"+str(len(MusictoPlay)-1))            
    else : 
        print("Wrong input! It must be a number ")  
    





