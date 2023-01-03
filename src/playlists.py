class playlist:

    def __init__(self, name):
        self.name = name
        self.songList = [] #contains only song u ids

    def addSong(self, uid):
        self.songList.append(uid)
    
    def removeSong(self, uid):
        self.songList.remove(uid)
    
    def getSongs(self):
        return self.songList
    
    def rename(self, newName):
        if self.name == "main":
            print("cannot change main library name")
        else: self.name = newName
