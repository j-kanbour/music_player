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

    def deleteSongs(self):
        self.songList.clear()
    
    #get playlist song list
    def getSongs(self):
        return self.songList
    
    def getname(self):
        return self.name
