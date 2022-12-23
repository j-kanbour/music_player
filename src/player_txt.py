import song
from pygame import mixer

playlists = []

#load song
#play song
#pause song
action = input("select action: ")
match action:
    case "play":
        song.play()