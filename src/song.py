from pygame import mixer
# from tkinter import *
# import tkinter.font as font
from tkinter import filedialog
import shutil, os

class song:
    def __init__(self, name, length, artist, genure, link, status):
        self.name = name
        self.length = length
        if (artist != None):
            self.artist = artist
        else: self.artist = "unknown"
        self.genure = genure
        self.link = link
        self.status = status
    
    def Load(self, link):
        mixer.music.load(self)

    def Play(self, status, link):
        if self.status != "playing":
            self.statuc = "playing"
            mixer.music.play() #meeds some while loop to play
            while True:
                if mixer.music.get_endevent() == 1:
                    self.statuc = "played"
                    break
    
    #to pause the song 
    def Pause():
        mixer.music.pause()

        


#add song(s) to main library
#use oo
def addsongs(playlsit):
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for i in temp_song:
        shutil.copy(i, f"src\{playlsit}")

# delete song from playlist
#use oo 
def deletesong(self, playlist):
    if os.path.exists(self.link):
        os.remove(song)
    else:
        print("The file does not exist")
    

#to stop the  song 
def Stop(songs_list):
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous(songs_list):
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/DataFlair/python-mp3-music-player/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)

def Next(songs_list):
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song 
    temp=songs_list.get(next_one)
    temp=f'C:/Users/DataFlair/python-mp3-music-player/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)