import tkinter as tk
import time
import os
from tkinter import PhotoImage, Tk
from tkinter.ttk import *


root = tk.Tk()
root.title("TextTale")
root.geometry("1280x720")


def cmd1():
    os.startfile("TextTale.py")
    exit()


def credbtn():
    os.startfile("credits.py")
    exit()


opentt = Button(root, text="Start Game", command=cmd1)
opentt.pack()


opencred = Button(root, text="View Credits", command=credbtn)
opencred.pack()


root.mainloop()