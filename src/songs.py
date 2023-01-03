from pygame import mixer

class song:

    def __init__(self, title, length, artist, genure, link):
        self.title = title
        self.length = round(length, 2)
        self.artist = artist
        self.genure = genure
        self.link = link
        self.status = "not playing"
    
    def Load(self):
        mixer.music.load(self)
        self.status = "loaded"

    def PlayPause(self):
        if self.status == "loaded":
            self.status = "playing"
            mixer.music.play() #meeds some while loop to play
            # while True:
            #     if mixer.music.get_endevent() == 1:
            #         self.status = "paused"
            #         next()
        elif self.status == "paused":
            mixer.music.unpause()
            self.status = "playing"
        elif self.status == "playing":
            mixer.music.pause()
            self.status = "paused"