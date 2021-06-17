import tkinter as tk
import time
import os
import webbrowser
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


def gtpge():
    webbrowser.open("https://github.com/Baaron1/TextTale")


def exitcmd():
    print("Sorry to see you go")
    time.sleep(2)
    exit()


def opndmo():
    os.startfile("demo.py")
    exit()


opentt = Button(root, text="Start Game", command=cmd1)
opentt.pack()


demobtn = Button(root, text="Play the Demo", command=opndmo)
demobtn.pack()


opencred = Button(root, text="View Credits", command=credbtn)
opencred.pack()


gitpage = Button(root, text="View the GitHub page", command=gtpge)
gitpage.pack()


exitbutton = Button(root, text="Exit", command=exitcmd)
exitbutton.pack()


devmode = input()
if devmode == "developer mode" or devmode == "Developer mode" or devmode == "Developer Mode":
    print("You are now accessing developer mode")
    q1 = input("What is your command?: ")
    if q1 == "fake":
        print("Oh, so you really do know. You must really be the creator. \n Welcome back")
        time.sleep(2)
        print("Is there something you would like to access or are you just messing around?")
        time.sleep(1)
        q11 = input(": ")
        if q11 == "yes":
            print("Well too bad you have been showing off to much recently")
            time.sleep(10)
            exit()
        else:
            exit()
    else:
        print("Wait a minute...")
        time.sleep(2)
        print("That is not the password!!!!")
        time.sleep(2)
        print("INTRUDER!!!")
        time.sleep(10)
        exit()
else:
    print("Sorry I do not recognise that as a command")


root.mainloop()