from __future__ import unicode_literals
import youtube_dl
import pyglet
import ast
import json
import os


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def display_songlist() :
    arr_fromfolder = []
    
    with open('music_list.txt',"r",encoding='utf-8-sig') as f:
        for data in f:
            check = str(data)
            if len(check) >= 3:
                test_json = ast.literal_eval(data.strip())
                arr_fromfolder.append(test_json)
            # print parsed  
    #file data = isempty  
    if len(arr_fromfolder) == 0 :
        print("data file is empty !!")
        return
    for i in range(len(arr_fromfolder)) : 
        print(str(i)+". "+arr_fromfolder[i]["title"]) 
    
def show_detail_asong() :
    arr_fromfolder = []

    with open('music_list.txt',"r",encoding='utf-8-sig') as f:
        for data in f:
            check = str(data)
            if len(check) >= 3:
                test_json = ast.literal_eval(data.strip())
                arr_fromfolder.append(test_json)
            # print parsed    
   
    #file data = isempty  
    if len(arr_fromfolder) == 0 :
        print("data file is empty !!")
        return
        
    for i in range(len(arr_fromfolder)) : 
        print(str(i)+". "+arr_fromfolder[i]["title"])

    print("_________________")
    song_number = input("Enter song number from 0 -->  "+str(len(arr_fromfolder)-1)+ ": ")
    if song_number.isdigit() :
        if 0 <= int(song_number) < len(arr_fromfolder) :
            for i in range(len(arr_fromfolder)) :
                if i == int(song_number) : 
                    print("ID : ",arr_fromfolder[i]["id"])
                    print("TITLE : ",arr_fromfolder[i]["title"])
                    print("CREATOR : ",arr_fromfolder[i]["creator"])
                    print("DURATION : ",arr_fromfolder[i]["duration"])
        else : 
            print("you inputed false ! number from 0 -->"+str(len(arr_fromfolder)-1))            
    else : 
        print("you inputed false ! input must is number  ")    
        
def play_asong() :
    arr_fromfolder = []
    f = open('music_list.txt', "r",encoding='utf-8-sig')
    for line in f:
        test_json =  ast.literal_eval(line)
        arr_fromfolder.append(test_json)

    for i in range(len(arr_fromfolder)) : 
        print(str(i)+". "+arr_fromfolder[i]["title"]) 
   
    print("_________________")
    print("choose a song you want play : ")
    song_number = input("Enter song number from 0 -->  "+str(len(arr_fromfolder)-1)+ ": ")
    if song_number.isdigit() :
        if 0 <= int(song_number) < len(arr_fromfolder) :
            for i in range(len(arr_fromfolder)) :
                if i == int(song_number) : 
                    music = pyglet.resource.media(str(arr_fromfolder[i]["title"])+".mp3")
                    music.play()
                   
                    options = input("if you want stop -->  input 'Stop' : ")  
                    if options == 'Stop' :
                        return
                    # pyglet.app.run()
                    
        else : 
            print("you inputed false ! number from 0 -->"+str(len(arr_fromfolder)-1))            
    else : 
        print("you inputed false ! input must is number ")  


# python app_music.py
array_music_dictionary = []
def search_dowload_asong() :
    if len(array_music_dictionary) == 0 :#lay du lieu tu file
        f = open('music_list.txt', "r",encoding='utf-8-sig')
        for line in f:
             array_music_dictionary.append(line)

    print("_________________")
    search = input("Enter seach a song : ")
    array_music = []
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s','format': '137/best','logger': MyLogger(),'progress_hooks': [my_hook],})

    with ydl:
        result = ydl.extract_info(
            'https://www.youtube.com/results?search_query='+search,
            download=False # We just want to extract the info
        ) 

    # array_music = []
    if 'entries' in result:
        # Can be a playlist or a list of videos
        for i in range(5) :
            video0 = result['entries'][i]
            array_music.append(video0)
    else:
        # Just a video
        video = result
    
    for i in range(len(array_music)):
        print(str(i) + ' : ' + array_music[i]['title']) 
    print("_________________")
    print("Do you want dowload a song")
    print("neu ban ko muon dowlaod bai hat nhap : No")
    print("neu ban muon dowlaod bai hat nhap : Yes")
    print("_________________")
    value_input =  input("nhap options : ")
    
    if value_input == "No" :
        return

    elif value_input == "Yes" : 
        stt_song =  int(input("nhap stt bai hat ban muon dowload : "))
        # if(stt_song.isde)
        for i in range(len(array_music)) : 
            if i == stt_song :
                id = array_music[i]["id"]
                title = array_music[i]["title"]
                creator = array_music[i]["creator"]
                duration = array_music[i]["duration"]

        music_dictionary = {
            "id" : id,
            "title" : title,
            "creator" : creator,
            "duration" : duration,
        }  
        # array_music_dictionary = []
        array_music_dictionary.append(music_dictionary)

        # f = open("music_list.txt", "a")#them vao cuoi file
        # f = open("music_list.txt", "w")#ghi de len file

        with open('music_list.txt', 'w',encoding='utf-8') as f:
            for item in array_music_dictionary:
                f.write("%s\n" % item)  
        ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v='+id])


    else : 
        print("you need input 'Yes' or 'No' !!")

check = True
print("Hello this is Tk music app")
print("Pick one of a options :")

#check file music_list.txt in folder
exists = os.path.isfile('music_list.txt')
if exists == False:
    f = open("music_list.txt", "x")
    
while check : 
    print("1. Show All song ")
    print("2. Show detail os a song ")
    print("3. Play a song ")
    print("4. Search and dowload songs")
    print("5. Exit")

    while check :
        print("_________________")
        manipulation = int(input("choose options : "))
        
        while check : 
            if manipulation == 1 : 
                display_songlist()
                break
            if manipulation == 2 :  
                show_detail_asong()
                break 
            if manipulation == 3 :
                play_asong()
                break
            if manipulation == 4 :
                search_dowload_asong()
                break
            if manipulation == 5 :                      
                check = False


music = pyglet.resource.media("tenbaihat.mp3")
music.play()