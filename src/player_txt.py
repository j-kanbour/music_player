import songs, playlists, json
from pygame import mixer
from collections import deque

playLis = [] #index 0 = main library
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next

#load all saved playlists and songs
def openMixer():
    mixer.init()
    #load all songs and playlists from JSON
    #if json empty them create Main playlist

    #songlist = json saved songlist
    #playlists = json saved playlists
    
    #songlist[0].load()

#saves all playlists and songs to JSON
def closeMixer():
    with open('j', 'w') as file:
        temp = []
        for p in playLis:
            p.toJSON() #converts all songs in playlist to dictionaries
            temp.append(p.__dict__)
        file.write(json.dumps(temp, indent=3))
        file.write(json.dumps(songList))

def newPlaylist(name):
    p = playlists(name)
    playLis.append(p)

def delPlaylist():
    currPlaylist.removeAllSongs()
    playLis.remove(currPlaylist)
    currPlaylist = playLis[0]

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
    return playLis

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
