import songs, playlists, json
from pygame import mixer
from collections import deque
import audio_metadata
from tkinter import filedialog

playLis = [] #index 0 = main library
CompleteSongList = {} #contains all uid : song
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
uid = 0

#load all saved playlists and songs
def openMixer():
    mixer.init()
    with open('saved_data') as fp:
        data = json.load(fp)
    #how to get read different from different lists 
    #i.e data[0] = playlists
    #    data[1] = songlist
    #    len(data[1]) = curr uid
    #    data[2] = songList
    for p in data:
        newPlaylist(p["name"],p["songList"])
    
    fp.close()

#saves all playlists and songs to JSON
def closeMixer():
    with open('saved_data', 'w') as file:
        temp = []
        for p in playLis:
            temp.append(p.__dict__)
        file.write(json.dumps(temp, indent=2))
    playLis.clear()
    CompleteSongList.clear()
    songList.clear()
    file.close()

def newPlaylist(name, songs = None):
    p = playlists.playlist(name)
    playLis.append(p)
    if songs != None:
        for s in songs:
            p.addSong(s)

#add song(s) to main library
def newSongs(self):
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Desktop/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for i in temp_song:
        metadata = audio_metadata.load(i)
        length = metadata['streaminfo']['duration']
        artist = metadata['tags']['artist'][0]
        title = metadata['tags']['title'][0]
        genre = metadata['tags']['genre'][0]
        s = songs.song(title, length, artist, genre, i)
        
        uid = uid + 1
        CompleteSongList[uid] = s 
        playLis[0].addSong(uid)

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
