import songs, playlists
from pygame import mixer
from collections import deque

playlists = [] #index 0 = main library
global currPlaylist
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
global currSong

def openMixer():
    mixer.init()
    #load all songs and playlists from JSON
    #if json empty them create Main playlist

    #songlist = json saved songlist
    #playlists = json saved playlists
    
    #songlist[0].load()

def closeMixer():
    pass
    #append JSON
    #JSON.dumps
        #current song
        #current song list
        #all playlists
            #all songs

def newPlaylist(name):
    p = playlists(name)
    playlists.append(p)

def delPlaylist():
    currPlaylist.removeAllSongs()
    playlists.remove(currPlaylist)
    currPlaylist = playlists[0]

def next():
    currSong.status = "n/a"
    songList.rotate(-1)
    currSong = songList[0]
    currSong.load()
    currSong.play()

def previous():
    currSong.status = "n/a"
    songList.rotate(1)
    currSong = songList[0]
    currSong.load()
    currSong.play()

def getSongList():
    return songList

def getplaylists():
    return playlists

def main():
    openMixer()
    action = "null"
    #load curr song
    #prep curr song list
    #song actions
    if action == "play":
        currSong.load()
        currSong.PlayPause()
    if action == "pause":
        currSong.PlayPause()
    if action == "next":
        next()
    if action == "previous":
        previous()
    #playlist actions 
