import controller
from tkinter import *
import tkinter.font as font

#creating the root window 
root=Tk()
root.title('Music app')
#initialize mixer 
controller.openMixer()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",width =7,command=controller.play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=controller.pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=print("heh"))
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=controller.unpause)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",width =7,command=controller.previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,command=controller.next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menus 
menuebar=Menu(root)
root.config(menu=menuebar)

#songs Menu
song_menu=Menu(menuebar)
menuebar.add_cascade(label="Songs",menu=song_menu)
song_menu.add_command(label="Add songs",command=controller.newSongs)
song_menu.add_command(label="Delete song",command=controller.deleteSong)
song_menu.add_command(label="Load all songs", command=controller.loadMainList)

#playlist Menu
playlist_menu=Menu(menuebar)
menuebar.add_cascade(label="Playlists",menu=playlist_menu)
playlist_menu.add_command(label="New PLaylist",command=controller.newPlaylist)
playlist_menu.add_command(label="Delete Playlist",command=controller.deletePlaylist)
playlist_menu.add_command(label="add song to playlist", command=controller.addtoPlaylist)
playlist_menu.add_command(label="remove song from playlist", command=controller.removefromPlaylist)

mainloop()
controller.closeMixer()