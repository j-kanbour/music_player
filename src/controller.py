import songs, playlists, pickle, os
from pygame import mixer
from collections import deque
import audio_metadata
from tkinter import filedialog

playListList = []
CompleteSongList = {} #contains all uid : song
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
currplaylist = None
uid = 0

"""
    Open/close app functions, works
"""

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

#saves all playListListts and songs to file
def closeMixer():
    try: 
        songList[0].resetstatus()
    except IndexError: pass

    
    with open('saved_data', 'wb') as file:
        pickle.dump(playListList, file)
        pickle.dump(CompleteSongList, file)
        pickle.dump(songList, file)
    
    #clear existing data
    playListList.clear()
    CompleteSongList.clear()
    songList.clear()
    file.close()

"""
    Song functions
"""
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
    
def deleteSong():
    global songList, CompleteSongList
    try:
        currsong = songList[0]
        songList.remove[0]
        CompleteSongList.remove(currsong)
        for p in playListList:
            p.removeSong(currsong)
    except IndexError: pass

def play():
    try: 
        songList[0].Load()
        songList[0].PlayPause()
    except IndexError: pass

def pause():
    try:
        songList[0].PlayPause()
    except IndexError: pass

def unpause():
    try:
        songList[0].PlayPause()
    except IndexError: pass

#load and play next song
def next():
    global songList
    try:
        songList[0].resetstatus()
        songList.rotate(-1)
        songList[0].Load()
        songList[0].PlayPause()
    except IndexError: pass

#load and play previous song
def previous():
    global songList
    try:
        songList[0].resetstatus()
        songList.rotate(1)
        songList[0].Load()
        songList[0].PlayPause()
    except IndexError: pass

"""
    PLaylist functions
"""

#make a new playlist
def newPlaylist(name):
    global playListList
    p = playlists.playlist(name)
    playListList.append(p)

#adds all songs in playlist to current songList
def loadPlaylist(pl):
    global songList
    songList.clear()
    songList = deque(playListList[pl].getSongs())
    
#adds all songs in library to current songList
def loadMainList():
    global songList
    songList.clear()
    for i in CompleteSongList.values():
        songList.append(i)

def deletePlaylist(pl):
    global playListList
    pl.deleteSongs()
    playListList.remove(pl)

def addtoPlaylist(pl):
    try:
        pl.addSong(songList[0])
    except IndexError: pass
    
def removefromPlaylist(pl):
    try:
        pl.removeSong(songList[0])
    except IndexError: pass

# def help():
#     print(
#             "quit --> closes music player\n\
#             \nSONG OPTIONS\n\
#             'add songs' --> allows you to add songs to main library\n\
#             'song list' --> displays songs in current play\n\
#             'play' --> plays current song\n\
#             'pause' --> pauses current song\n\
#             'next' --> plays next song\n\
#             'previous' --> plays previous song\n\
#             \nPLAYLIST OPTIONS\n\
#             'new playlist' --> creats a new playlist\n\
#             'add to playlist' --> allows you to add the current song to any playlist\n\
#             'view playlist' --> shows songs in selected playlist\n\
#             'load playlist' --> loads songs from selected playlist\n\
#             'load main' --> loads all songs in library\n\
#             'rename playlist' --> rename playlist\n\
#             'delete playlist' --> deletes playlist\n\
#             'search song' --> allows you to search for a song in the current playlist\n\
#             'sort songs' --> allows you to sort songs in the current playlsit by one of the following:\n\
#                        1 - alphabetical(A-Z)\n\
#                        2 - alphabetical(Z-A)\n\
#                        3 - length(max-min)\n\
#                        4 - length(min-max)\n\
#                        5 - genre(A-Z)\n\
#                        6 - genre(Z-A)\n\
#                        7 - artist(A-Z)\n\
#                        8 - artist(Z-A)\n")