from ClassMusicsPlayer import MusicPlayer
from tkinter import *
import pygame
import os
root = Tk() # In order to create an empty window
# Passing Root to MusicPlayer Class
path = 'Assignment\SongList'
MusicPlayer(root, path)

#display the window
root.mainloop()
