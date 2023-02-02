import songs, playlists, pickle, os, sort, search
from pygame import mixer
from collections import deque
import audio_metadata
from tkinter import filedialog

playListList = []
CompleteSongList = {} #contains all uid : song
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
currplaylist = None
uid = 0

#load all saved playlists and songs
def openMixer():
    global playListList, CompleteSongList, uid, songList, currplaylist

    mixer.init()

    if os.path.exists("saved_data") == True:
        with open('saved_data', 'rb') as f:
            playListList = pickle.load(f)
            CompleteSongList = pickle.load(f)
            songList = pickle.load(f)
            currplaylist = None
        f.close()
        uid = len(CompleteSongList)
    else:
        help()

#saves all playListListts and songs to file
def closeMixer():
    songList[0].resetstatus()
    
    with open('saved_data', 'wb') as file:
        pickle.dump(playListList, file)
        pickle.dump(CompleteSongList, file)
        pickle.dump(songList, file)
    
    #clear existing data
    playListList.clear()
    CompleteSongList.clear()
    songList.clear()
    file.close()

#make a new playlist
def newPlaylist(name):
    global currplaylist

    p = playlists.playlist(name)
    playListList.append(p)
    currplaylist = p

#add song(s) to main library
def newSongs():
    global uid, CompleteSongList
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Desktop/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for i in temp_song:
        metadata = audio_metadata.load(i)
        try: length = metadata['streaminfo']['duration']
        except: length = 0
        
        try: artist = metadata['tags']['artist'][0]
        except: artist = "unknown"
        
        try: title = metadata['tags']['title'][0]
        except: title = "unknown"

        try: genre = metadata['tags']['genre'][0]
        except: genre = "unknown"

        s = songs.song(title, length, artist, genre, i)
        
        uid = uid + 1
        CompleteSongList[uid] = s 

#adds all songs in playlist to current songList
def loadPlaylist(pl):
    global songList, CompleteSongList
    songList.clear()
    for i in pl.getSongs():
        songList.append(CompleteSongList[i])
    
#adds all songs in library to current songList
def loadMainList():
    global currplaylist, CompleteSongList
    currplaylist = None

    songList.clear()
    for i in CompleteSongList.values():
        songList.append(i)

#load and play next song
def next():
    global songList
    songList[0].resetstatus()
    songList.rotate(-1)
    currSong = songList[0]
    currSong.Load()
    currSong.PlayPause()

#load and play previous song
def previous():
    global songList
    songList[0].resetstatus()
    songList.rotate(1)
    songList[0].Load()
    songList[0].PlayPause()

def help():
    print(
            "quit --> closes music player\n\
            \nSONG OPTIONS\n\
            'add songs' --> allows you to add songs to main library\n\
            'song list' --> displays songs in current play\n\
            'play' --> plays current song\n\
            'pause' --> pauses current song\n\
            'next' --> plays next song\n\
            'previous' --> plays previous song\n\
            \nPLAYLIST OPTIONS\n\
            'new playlist' --> creats a new playlist\n\
            'add to playlist' --> allows you to add the current song to any playlist\n\
            'playlist selelct' --> plays songs in playlist\n\
            'view playlist' --> shows songs in selected playlist\n\
            'load selected playlist' --> loads songs from selected playlist\n\
            'load main playlist' --> loads all songs in library\n\
            'rename playlist' --> rename playlist\n\
            'search song' --> allows you to search for a song in the current playlist\n\
            'sort songs' --> allows you to sort songs in the current playlsit by one of the following:\n\
                       1 - alphabetical(A-Z)\n\
                       2 - alphabetical(Z-A)\n\
                       3 - length(max-min)\n\
                       4 - length(min-max)\n\
                       5 - genre(A-Z)\n\
                       6 - genre(Z-A)\n\
                       7 - artist(A-Z)\n\
                       8 - artist(Z-A)\n")

def controller():
    global songList, currplaylist, songList

    openMixer()

    action = None
    while action != "quit":
        action = input("enter action (type 'help' for possible actions): ")
        #song actions
        match action:
            case "help":
                help()
            case "add songs":
                newSongs()
            case "song list":
                for i in range(len(songList)):
                    print(f"{i+1} {songList[i].getname()} by {songList[i].getartist()}\n")
            case "play":
                songList[0].Load()
                songList[0].PlayPause()
                print(f"playing: {songList[0].getname()}")
            case "pause":
                songList[0].PlayPause()
            case "next":
                print(f"playing: {songList[0].getname()}")
                next()
            case "previous":
                print(f"playing: {songList[0].getname()}")
                previous()
            case "new playlist":
                name = input("input playlist name: ")
                newPlaylist(name)
            case "playlist select":
                for i in range(len(playListList)):
                    print(f"{i+1} {playListList[i].getname()}\n")
                
                try: 
                    selected = int(input("select playlist number: "))
                    currplaylist = playListList[selected-1]
                except: 
                    print("enter valid number")
            case "load selected playlist":
                loadPlaylist(currplaylist)
            case "load main playlist":
                loadMainList()
            case "add to playlist":
                for i in range(len(playListList)):
                    print(f"{i+1} {playListList[i]}\n")
                selected = int(input("select playlist number: "))
                playListList[selected].addSong(songList[0])
            case "view playlist":
                currplaylist.observe()
            case "sort":
                opt = input("select sort option (see 'help' for options): ")
                sort(currplaylist, opt)
            case "search":
                opt = input(": ")
                search(currplaylist, opt)

    closeMixer()

controller()