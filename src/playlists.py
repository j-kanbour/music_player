class playlist:

    def __init__(self, name):
        self.name = name
        self.songList = [] #contains only song u ids

    #add song to playlist
    def addSong(self, uid):
        self.songList.append(uid)
    
    #remove song from playlist 
    def removeSong(self, uid):
        self.songList.remove(uid)
    
    #get playlist song list
    def getSongs(self):
        return self.songList
    
    def observe(self):
        for i in range(len(self.songList)):
            print(f"{i+1} {self.songList[i]}\n")
    
    #rename playlist
    def rename(self, newName):
        if self.name == "main":
            print("cannot change main library name")
        else: self.name = newName
