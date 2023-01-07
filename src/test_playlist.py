import player_txt, os

def test_jsonsaveload():
    if os.path.exists("saved_data") == True:
        os.remove('saved_data')

    player_txt.newPlaylist("main")
    player_txt.newPlaylist("one")
    player_txt.newPlaylist("two")

    player_txt.playListList[0].addSong(1)
    player_txt.playListList[0].addSong(2)

    assert len(player_txt.playListList) == 3
    assert player_txt.playListList[0].name == "main"
    assert player_txt.playListList[0].songList == [1,2]

    assert player_txt.playListList[1].name == "one"
    assert player_txt.playListList[1].songList == []

    assert player_txt.playListList[2].name == "two"
    assert player_txt.playListList[2].songList == []

    player_txt.closeMixer()
    assert len(player_txt.playListList) == 0

    player_txt.openMixer()
    assert len(player_txt.playListList) == 3
    assert player_txt.playListList[0].name == "main"
    assert player_txt.playListList[0].songList == [1,2]

    assert player_txt.playListList[1].name == "one"
    assert player_txt.playListList[1].songList == []

    assert player_txt.playListList[2].name == "two"
    assert player_txt.playListList[2].songList == []
    
if __name__ == "__main__":
    test_jsonsaveload()
    print("Passed")