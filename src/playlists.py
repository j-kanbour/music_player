import songs, player_txt
from tkinter import filedialog
import eyed3

class playlist:

    songs = []

    def __init__(self, name):
        self.name = name

    #re work this
    #add song(s) to main library
    def addsongs(playlsit):
        #to open a file  
        tag = eyed3.Tag()
        temp_song=filedialog.askopenfilenames(initialdir="Desktop/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
        ##loop through every item in the list to insert in the listbox
        for i in temp_song:
            tag.link(i)
            print (tag.getArtist(), tag.getAlbum(), tag.getTitle())

    def addSong(self, song):
        self.songs.append(song)
    
    def removeSong(self, song):
        self.songs.remove(song)
    
    def removeAllSongs(self):
        if self.name == "main":
            #inform use that all songs will be deleted
            for playlist in player_txt.getplaylists():
                if playlist.name != "main":
                    playlist.removeAllSongs()
            self.songs.clear()
        else: self.songs.clear()
    
    def rename(self, newName):
        if self.name == "main":
            print("cannot change main library name")
        else: self.name = newName
    
