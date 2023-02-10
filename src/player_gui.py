import controller
from tkinter import *
import tkinter.font as font

selelcted = None

#creating the root window 
root=Tk()
root.title('Music app')
#initialize mixer 


#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#listbox.curselection returns index of selected item

def updatelist(displaylist):
    songs_list.delete(0,songs_list.size())
    if displaylist == controller.songList:
        for i in displaylist:
            songs_list.insert(END,i.getname())
    elif displaylist == controller.playListList:
        for i in displaylist:
            songs_list.insert(END,i.getname())

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#user input
def newPlay():  
    name_var=StringVar()

    top = Toplevel(root)
    top.geometry("400x250")
    top.title("Playlist")
    Label(top, text= "Enter playlist name").place(x=150,y=50)

    Entry(top, textvariable = name_var).place(x=100,y=100)

    Button(top,text="Enter", width=5, 
    command=lambda:[controller.newPlaylist(name_var.get()),top.destroy()]).place(x=150,y=150)

def select():
    global selected
    selected = songs_list.curselection()[0]
    

#TODO
#merge the play pause and unpause button into one

#play button
play_button=Button(root,text="Play",width =7,command=lambda:[controller.play(), updatelist(controller.songList)])
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=controller.pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=controller.unpause)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=2)

#previous button
previous_button=Button(root,text="Prev",width =7,command=lambda:[controller.previous(), updatelist(controller.songList)])
previous_button['font']=defined_font
previous_button.grid(row=1,column=3)

#nextbutton
next_button=Button(root,text="Next",width =7,command=lambda:[controller.next(), updatelist(controller.songList)])
next_button['font']=defined_font
next_button.grid(row=1,column=4)

#Select button
stop_button=Button(root,text="Select",width =7,command=lambda:[select(),controller.loadPlaylist(selected), updatelist(controller.songList)])
stop_button['font']=defined_font
stop_button.grid(row=1,column=5)

#menus 
menuebar=Menu(root)
root.config(menu=menuebar)

#songs Menu
song_menu=Menu(menuebar)
menuebar.add_cascade(label="Songs",menu=song_menu)
song_menu.add_command(label="Add songs",command=controller.newSongs)
song_menu.add_command(label="Delete song",command=controller.deleteSong)
song_menu.add_command(label="Load all songs", command=lambda:[controller.loadMainList(), updatelist(controller.songList)])

#playlist Menu
playlist_menu=Menu(menuebar)
menuebar.add_cascade(label="Playlists",menu=playlist_menu)
playlist_menu.add_command(label="New Playlist",command=newPlay)
#playlist_menu.add_command(label="Delete Playlist",command=controller.deletePlaylist)
playlist_menu.add_command(label="add song to playlist", command=controller.addtoPlaylist)
playlist_menu.add_command(label="remove song from playlist", command=controller.removefromPlaylist)
playlist_menu.add_command(label="load playlist", command=lambda:[updatelist(controller.playListList)])

controller.openMixer()
updatelist(controller.songList)
mainloop()
controller.closeMixer()