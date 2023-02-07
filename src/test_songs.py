import controller, os

def test_jsonsaveload():
    if os.path.exists("saved_data") == True:
        os.remove('saved_data')
    player_txt.openMixer()
    player_txt.newSongs()
    print(player_txt.CompleteSongList)

    player_txt.closeMixer()
    print(player_txt.CompleteSongList)

    player_txt.openMixer()
    print(player_txt.CompleteSongList)

def test_songsandplaylists():
    if os.path.exists("saved_data") == True:
        os.remove('saved_data')
    player_txt.openMixer()

    one = player_txt.newPlaylist("main")
    player_txt.newPlaylist("one")
    player_txt.newPlaylist("two")

    player_txt.newSongs()
    print(player_txt.CompleteSongList)
    print(player_txt.playListList)

    player_txt.closeMixer()
    print(player_txt.CompleteSongList)
    print(player_txt.playListList)
    
    player_txt.openMixer()
    print(player_txt.CompleteSongList)
    print(player_txt.playListList)

if __name__ == "__main__":
    #test_jsonsaveload()
    test_songsandplaylists()
    print("Passed")
    