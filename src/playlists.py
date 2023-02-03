class playlist:

    def __init__(self, name):
        self.name = name
        self.songList = [] #contains songs

    #add song to playlist
    def addSong(self, s):
        self.songList.append(s)
    
    #remove song from playlist 
    def removeSong(self, s):
        self.songList.remove(s)
    
    #get playlist song list
    def getSongs(self):
        return self.songList
    
    def observe(self):
        print(f"\nPlaylist: {self.name}")
        for i in range(len(self.songList)):
            print(f"{i+1} {self.songList[i].getname()} by {self.songList[i].getartist()}\n")
    
    def getname(self):
        return self.name
    
    #rename playlist
    def rename(self, newName):
        self.name = newName
