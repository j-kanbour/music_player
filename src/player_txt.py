import songs, playlists, json, os
from pygame import mixer
from collections import deque
import audio_metadata
from tkinter import filedialog

playLis = []
CompleteSongList = {} #contains all uid : song
songList = deque() #a looping quqeue where first element is curr song, last is previous and next is next
uid = 0

#load all saved playlists and songs
def openMixer():
    global playLis
    global CompleteSongList
    global uid
    global songList

    mixer.init()

    if os.path.exists("saved_data") == False:
        with open('saved_data') as f:
            json_string = f.read()
        f.close()

        playLis = json.loads(json_string[0])
        print(playLis)

        # CompleteSongList = data[1]
        # uid = len(data[1])
        # songList = deque(data[2])

#saves all playlists and songs to JSON
def closeMixer():
    with open('saved_data', 'w') as file:
        save = []
        temp = []
        for p in playLis:
            temp.append(p.__dict__)
        save.append(temp) # save[0] = playlists

        # for s in CompleteSongList.values:
        #     temp.append(s.__dict__)
        # save.append(temp)    #save[1] = CompleteSongList
        save.append([list(songList)]) #save[2] = songList
        file.write(json.dumps(save, indent=2))
    
    #clear existing data
    playLis.clear()
    CompleteSongList.clear()
    songList.clear()
    file.close()

def newPlaylist(name):
    p = playlists.playlist(name)
    playLis.append(p)

#add song(s) to main library
def newSongs():
    global uid
    global CompleteSongList
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
