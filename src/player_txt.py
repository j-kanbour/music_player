import songs, playlists, pickle, os
from pygame import mixer
from collections import deque
import audio_metadata
from tkinter import filedialog

playListList = []
CompleteSongList = {} #contains all uid : song
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
uid = 0

#load all saved playlists and songs
def openMixer():
    global playListList, CompleteSongList, uid, songList

    mixer.init()

    if os.path.exists("saved_data") == True:
        with open('saved_data', 'rb') as f:
            playListList = pickle.load(f)
            CompleteSongList = pickle.load(f)
            songList = pickle.load(f)
        f.close()
        uid = len(CompleteSongList)

    else:
        #provide instructions for first time users
        pass

#saves all playListListts and songs to file
def closeMixer():
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
    p = playlists.playlist(name)
    playListList.append(p)

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
    songList.clear()
    for i in CompleteSongList.values:
        songList.append(i)

#load an dplay next song
def next():
    global songList
    currSong.status = "n/a"
    songList.rotate(-1)
    currSong = songList[0]
    currSong.Load()
    currSong.PlayPause()

#load and play previous song
def previous():
    global songList
    currSong.status = "n/a"
    songList.rotate(1)
    currSong = songList[0]
    currSong.Load()
    currSong.PlayPause()

def controller():
    global songList

    openMixer()

    action = None
    while action != "quit":
        action = input("enter action (type 'help' for possible actions): ")
        #song actions
        if action == "help":
            print(
            "SONG OPTIONS\n\
            'add songs' --> allows you to add songs to main library\n\
            'play' --> plays current song\n\
            'pause' --> pauses current song\n\
            'next' --> plays next song\n\
            'previous' --> plays previous song\n\
            \nPLAYLIST OPTIONS\n\
            'new playlist' --> creats a new playlist\n\
            'add to playlist' --> allows you to add the current song to any playlist\n\
            'load playlist' --> plays songs in playlist\n\
            'rename playlist' --> rename playlist\n\
            'search song' --> allows you to search for a song in the current playlist\n\
            'sort songs' --> allows you to sort songs in the current playlsit by one of the following:\n\
                       - alphabetical(A-Z)\n\
                       - alphabetical(Z-A)\n\
                       - length(max-min)\n\
                       - length(min-max)\n\
                       - genre(A-Z)\n\
                       - genre(Z-A)\n\
                       - artist(A-Z)\n\
                       - artist(Z-A)\n\
            ")rch song' --> allows you to search for a song in the current playlist\n\
            ")
        if action == "play":
            songList[0].load()
            songList[0].PlayPause()
        elif action == "pause":
            songList[0].PlayPause()
        elif action == "next":
            next()
        elif action == "previous":
            previous()

        if action == "new playlsit":
            name = input("input playlist name: ")
            newPlaylist(name)
            #prompt for name
