import songs, audio_metadata
from tkinter import filedialog

class playlist:
    def __init__(self, name):
        self.name = name
        self.songList = []

    #add song(s) to main library
    def addsongs(self):
        #to open a file  
        temp_song=filedialog.askopenfilenames(initialdir="Desktop/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
        ##loop through every item in the list to insert in the listbox
        for i in temp_song:
            metadata = audio_metadata.load(i)
            length = metadata['streaminfo']['duration']
            artist = metadata['tags']['artist'][0]
            title = metadata['tags']['title'][0]
            genre = metadata['tags']['genre'][0]
            s = songs(title, length, artist, genre, i)
            self.addSong(s)

    def addSong(self, songs):
        self.songList.append(songs)
    
    def removeSong(self, song):
        self.songList.remove(song)
    
    def getSongs(self):
        return self.songList
    
    def rename(self, newName):
        if self.name == "main":
            print("cannot change main library name")
        else: self.name = newName

    def toJSON(self):
        #converts list of all song objects to dictionaries
        e = 0
        for i in self.songList:
            self.songList[e] = i.__dict__
            e = e + 1