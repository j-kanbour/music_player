import song, playlist
from pygame import mixer

playlists = []
songList = [] #a looping quqeue where first element is curr song, last is previous and next is next

def openMixer():
    mixer.init()
    #load all songs and playlists from JSON
    #if json empty them create Main playlist

def newPlaylist(name):
    p = playlist(name)
    playlists.append(p)
    #append json

def delPlaylist(p):
    p.removeAllSongs()
    playlists.remove(p)

def closeMixer():
    pass
    #append JSON
        #current song
        #current song list
        #all playlists
            #all songs


def main():
    openMixer()
    #load curr song
    #prep curr song list
    pass
