import json
from youtube_dl import YoutubeDL
from pyglet.media import Source, Player, load


Menu = {
    '1':'Show all songs',
    '2':'Show detail of a song',
    '3':'Play a song',
    '4':'search and download songs',
    '5':'Exit'}

Song_list = {''}
listSongDowload = []
print ('Welcome to music app.')


for key, value in Menu.items():
    print(key,".", value)
while True:
    i = int(input('Please choose one of the option below.'))
    if i == 1:
        # Write File
        # with open('data_file.json', 'w') as outfile:  
            # json.dump(search_result, outfile)
        #REad File
        with open('data_file.json', encoding = 'utf-8') as dataGet:
            listDataGet = json.loads(dataGet.read())
        if listDataGet == []:
            print ('Try to download some music first.')
        else:
            for song in listDataGet:
                print(song['title'])
    elif i == 4:
        with open('data_file.json', encoding = 'utf-8') as dataGet:
            listDataGet = json.loads(dataGet.read())
        listSongDowload = listDataGet
        findSong = input("Find your song: ")
        options = {
            'default_search': 'ytsearch5'
        }
        ydl = YoutubeDL(options)
        search_result = ydl.extract_info(findSong, False)
        for index, song in enumerate(search_result['entries']):
            print(index+1," - ", song['title'])
        
        # Step:Download
        choose = int(input("Choose the number of the song want to download: "))
        linkSongYouChose = search_result['entries'][choose-1]['webpage_url']
        optionsDownload = {
            'outtmpl': '%(id)s', # lấy tên file đown về là id của video
                'postprocessors': [{
                'key': 'FFmpegExtractAudio', # Tách lấy audio
                'preferredcodec': 'mp3', # Format ưu tiên là mp3
                'preferredquality': '192', # Chất lượng bitrate
            }],
        }
        ydl2 = YoutubeDL(optionsDownload)
        infoDownload = ydl2.extract_info(linkSongYouChose, download = True)
        listSongDowload.append(infoDownload)
        with open('data_file.json', 'w') as outfile:  
            json.dump(listSongDowload, outfile)
    elif i == 5:
        break
    elif i == 2:
        with open('data_file.json', encoding = 'utf-8') as dataGet:
            listDataGet = json.loads(dataGet.read())
        for index, song in enumerate(listDataGet):
            print(index+1, " - ", song)
        chooseSong = int(input("Choose the song want to show details of: ")) -1
        print('ID', ":" ,listDataGet[chooseSong]['id'])
        print('title', ":" ,listDataGet[chooseSong]['title'])
        print('duration', ":" ,listDataGet[chooseSong]['duration'])
        print('webpage_url', ":" ,listDataGet[chooseSong]['webpage_url'])
    elif i == 3: 
        with open('data_file.json', encoding = 'utf-8') as dataGet:
            listDataGet = json.loads(dataGet.read())
        a = int(input('The number of the song you want to play'))
        nameSong = listDataGet[a-1]['id']+".mp3"
        player = Player()
        source = load(nameSong)
        player.queue(source)
        player.play()
        while True:    
            b = input('You can play, pause and stop music by input "play" ,"pause" and "stop"')
            if b == 'pause':
                player.pause()
            elif b == 'play':
                player.play()
            elif b == 'stop':
                player.pause()
                break