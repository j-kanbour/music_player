import player_txt

def test_jsonsaveload():
    player_txt.openMixer()
    player_txt.newSongs()
    print(player_txt.CompleteSongList)
    player_txt.closeMixer()
    print(player_txt.CompleteSongList)
    player_txt.openMixer()
    print(player_txt.CompleteSongList)

if __name__ == "__main__":
    test_jsonsaveload()
    print("Passed")
    