from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import os
from pygame import mixer
import cv2
import imutils as iu
import pyglet
from pyglet.window import key
from tkinter import ttk
from ttkthemes import themed_tk as tk

window = tk.ThemedTk()
window.get_themes()
window.set_theme('plastik')
window.title('MIV')
window.iconbitmap('icon.ico')
mixer.init()
emptylist = []


# menubar functions
def open_fun():
    status_bar['text'] = 'Open files to listbox'
    add_button_fun()


def instructions_fun():
    status_bar['text'] = 'Open Instructions'
    mb.showinfo('Instructions', 'First of all open your files '
                                'you want to perform and add '
                                'it in your listbox.After that cilck any one '
                                'of the file in your listbox and press the buttons '
                                'accordingly.For example if it is an mp3 file '
                                'first you just click the file in your listbox '
                                'and click the play button under the music section.'
                                'Likewise perform other files respectively')


def note_fun():
    status_bar['text'] = 'Open note'
    mb.showinfo('Note', 'For music : MIV only supports mp3 file.               '
                        '                                       '
                        'For image : It supports jpg,png and jpeg.'
                        '                                                      '
                        'For video : It only supports mp4 file'
                        ' and do not play very short videos in MIV. Press '
                        'space button to pause the video'
                        ' and if you want minimize or close your '
                        'video window then make sure you need to'
                        ' pause the video after that minimize or'
                        ' closed it.')


def about_fun():
    status_bar['text'] = 'Open about'
    mb.showinfo('about MIV', 'MIV is a simple and '
                             'effective software.It performs three operations.'
                             'Where you can play music and view image and watch '
                             'movie within the same software')


def contact_fun():
    status_bar['text'] = 'Open contact'
    mb.showinfo('contact', 'Founder : Mowneeshkumar E'
                           '                                                  '
                           '                  mailto : something@gmail.com')


# listbox functions
def add_button_fun():
    status_bar['text'] = 'Add files to listbox'
    index = 0
    global filepath
    global filename
    filepath = fd.askopenfilename()
    filename = os.path.basename(filepath)
    listbox.insert(index, filename)
    emptylist.insert(index, filepath)
    index += 1


def del_button_fun():
    status_bar['text'] = 'Delete files from listbox'
    delete = listbox.curselection()
    listbox.delete(delete)


# music functions
def playmusic_fun():
    try:
        status_bar['text'] = 'playing music'
        song_selection = listbox.curselection()
        song_selection = int(song_selection[0])
        play_song = emptylist[song_selection]
        mixer.music.load(play_song)
        mixer.music.play()
    except:
        mb.showerror('Error playing music', 'First of all open your songs and add it in your '
                                            'listbox after that click any one song and click '
                                            'the play button')


def stopmusic_fun():
    status_bar['text'] = 'Music stoped'
    mixer.music.stop()


paused = True


def pausemusic_fun():
    global paused

    if paused == True:
        status_bar['text'] = 'Music paused'
        mixer.music.pause()
        paused = False
    elif paused == False:
        status_bar['text'] = 'Music unpaused'
        mixer.music.unpause()
        paused = True


muted = True


def mutemusic_fun():
    global muted
    if muted == True:
        status_bar['text'] = 'Music muted'
        mixer.music.set_volume(0)
        scale_button.set(0)
        unmute_button.config(image=mute_button_image)
        muted = False
    elif muted == False:
        status_bar['text'] = 'Music unmuted'
        mixer.music.set_volume(0.5)
        scale_button.set(50)
        unmute_button.config(image=unmute_button_image)
        muted = True


def scalevolume_fun(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


# image function
def image_fun():
    try:
        stopmusic_fun()
        status_bar['text'] = 'Showing image'
        image_selection = listbox.curselection()
        image_selection = int(image_selection[0])
        view_image = emptylist[image_selection]
        image = cv2.imread(view_image, 1)
        resized_image = iu.resize(image, 400)
        cv2.imshow('Image Viewer', resized_image)
        cv2.waitKey(0)
    except:
        mb.showerror('Error viewing image', 'First of all open your images and add it in your '
                                            'listbox after that click any one image and click '
                                            'the view button')


def video_fun():
    stopmusic_fun()
    status_bar['text'] = 'Playing video'
    video_selection = listbox.curselection()
    video_selection = video_selection[0]
    play_video = emptylist[video_selection]
    icon = pyglet.image.load('video button.png')
    vidpath=play_video
    video_load = pyglet.media.load(vidpath)
    fmt = video_load.video_format
    videoplayer=pyglet.media.Player()
    videoplayer.queue(video_load)
    videoplayer.play()
    root = pyglet.window.Window(width=fmt.width, height=fmt.height)
    root.set_icon(icon)
    root.set_caption('Video Player')

    @root.event
    def on_draw():
        videoplayer.get_texture().blit(0, 0)

    @root.event
    def on_key_press(symbol, modifiers):
        if symbol == key.SPACE:
            if videoplayer.playing:
                videoplayer.pause()
            else:
                videoplayer.play()

    pyglet.app.run()


# create menubar
menubar = Menu(window)
window.config(menu=menubar)
# for file menu
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=open_fun)
submenu.add_command(label='Exit', command=window.destroy)
# for help menu
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=submenu)
submenu.add_command(label='Instructions', command=instructions_fun)
submenu.add_command(label='Note', command=note_fun)
submenu.add_command(label='About', command=about_fun)
submenu.add_command(label='Contact', command=contact_fun)
# status bar
status_bar = ttk.Label(window, text='Welcome to MIV', relief=SUNKEN)
status_bar.pack(side=BOTTOM, fill=X)
# initial four frames
first_frame = Frame(window)
first_frame.pack(side=LEFT, padx=110)
second_frame = Frame(window)
second_frame.pack(side=LEFT, padx=110)
thrid_frame = Frame(window)
thrid_frame.pack(side=LEFT, padx=110)
fourth_frame = Frame(window)
fourth_frame.pack(side=LEFT, padx=110)
# first frame functionalities
top_frame = Frame(first_frame)
top_frame.pack(pady=10)
middle_frame = Frame(first_frame)
middle_frame.pack(pady=10)
bottom_frame = Frame(first_frame)
bottom_frame.pack(pady=10)
listbox_section = ttk.Label(top_frame, text='Listbox Section',relief=SUNKEN)
listbox_section.grid(row=0, column=0)
listbox = Listbox(middle_frame)
listbox.grid(row=0, column=0)
add_button = ttk.Button(bottom_frame, text='add', command=add_button_fun)
add_button.grid(row=0, column=0)
del_button = ttk.Button(bottom_frame, text='del', command=del_button_fun)
del_button.grid(row=0, column=1)
# second frame functionalities
top_frame = Frame(second_frame)
top_frame.pack(pady=10)
middle_frame = Frame(second_frame)
middle_frame.pack(pady=10)
bottom_frame = Frame(second_frame)
bottom_frame.pack(pady=10)
music_section = ttk.Label(top_frame, text='Music Section', relief=SUNKEN)
music_section.grid(row=0, column=0)
# play button
play_button_image = PhotoImage(file='play.png')
play_button = ttk.Button(middle_frame, image=play_button_image, command=playmusic_fun)
play_button.grid(row=0, column=0)
# stop button
stop_button_image = PhotoImage(file='stop.png')
stop_button = ttk.Button(middle_frame, image=stop_button_image, command=stopmusic_fun)
stop_button.grid(row=0, column=1)
# pause button
pause_button_image = PhotoImage(file='pause.png')
pause_button = ttk.Button(middle_frame, image=pause_button_image, command=pausemusic_fun)
pause_button.grid(row=0, column=2)
# mute button
mute_button_image = PhotoImage(file='mute.png')
unmute_button_image = PhotoImage(file='unmute.png')
unmute_button = ttk.Button(bottom_frame, image=unmute_button_image, command=mutemusic_fun)
unmute_button.grid(row=2, column=0)
# scale
scale_button = ttk.Scale(bottom_frame, from_=0, to_=100, orient=HORIZONTAL, command=scalevolume_fun)
scale_button.grid(row=2, column=1)
scale_button.set(50)
# thrid frame functionalities
top_frame = Frame(thrid_frame)
top_frame.pack(pady=10)
middle_frame = Frame(thrid_frame)
middle_frame.pack(pady=10)
image_section = ttk.Label(top_frame, text='Image Section', relief=SUNKEN)
image_section.grid(row=0, column=0)
# view button
view_button_image = PhotoImage(file='image button.png')
view_button = ttk.Button(middle_frame, image=view_button_image, command=image_fun)
view_button.grid(row=0, column=0)
# fourth frame functionalities
top_frame = Frame(fourth_frame)
top_frame.pack(pady=10)
middle_frame = Frame(fourth_frame)
middle_frame.pack(pady=10)
video_section = ttk.Label(top_frame, text='Video Section', relief=SUNKEN)
video_section.grid(row=0, column=0)
# play button
video_play_button_image = PhotoImage(file='video button.png')
video_play_button = ttk.Button(middle_frame, image=video_play_button_image, command=video_fun)
video_play_button.grid(row=0, column=0)
window.mainloop()
