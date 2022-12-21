from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#add many songs to the playlist of python mp3 player
def addsongs(songs_list):
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        s=s.replace("C:/Users/DataFlair/python-mp3-music-player/","")
        songs_list.insert(END,s)
     
def deletesong(songs_list):
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
    
    
def Play(songs_list):
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/lenovo/Desktop/DataFlair/Notepad/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

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