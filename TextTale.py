import pickle
import os
import sys
import time
import random


totallove = 1
child = str(input("name the fallen child:"))
time.sleep(1)
print("this is your name "  +  str(child))
time.sleep(1)
print("You’ve fallen into the underground. Do you want to go to the next room or explore this one")
time.sleep(5)
fallen = input("Choose one: 'explore' or 'move on'")
if fallen == "explore":
    print("you look around a little. you find flowers beneath you nothing else")
    time.sleep(4)
    print("you move on because there is nothing else")
    time.sleep(2)
if fallen == "move on":
    time.sleep(2)
print("you see a smiling flower. You approach it.")
time.sleep(2)
print("The flower says: 'howdy! I'm flowey, flowey the flower.'")
time.sleep(3)
print("Hmm...")
time.sleep(4)
print("You're new to the UNDERGROUND, aren’tcha")
time.sleep(4)
print("Golly you must be so confused.")
time.sleep(4)
print("Someone ought to teach you how things work around here!")
time.sleep(3)
print("I guess little old me will have to do.")
time.sleep(2)
print("Ready? Here we go!")
time.sleep(2)
print("See that heart? That is your SOUL, the very culmination of your being!")
time.sleep(4)
print("Your soul starts off weak but can grow strong if you gain a lot of LV.")
time.sleep(4)
print("What’s LV stand for? Why, LOVE of course!")
time.sleep(3)
print("You want some LOVE, don’t you?")
time.sleep(2)
print("Don’t worry, I’ll share some with you!")
time.sleep(3)
print("Down here, LOVE is shared through...")
time.sleep(3)
print("Little white… ‘friendliness pellets.’")
time.sleep(3)
print("Are you ready?")
time.sleep(2)
print("Get as many as you can!")
pellet = input("'collect' or 'move out of way'")
if pellet == "move out of way":
    print("Hey buddy, you missed them")
    print("Let’s try again, okay?")
pellet = input("dodge or collect")
if pellet == "dodge":
    print("Is this a joke? Are you braindead? RUN. INTO. THE. BULLETS!!!")
    time.sleep(4)
    print("You know what’s going on here, don’t you?")
    print("You just wanted to see me suffer")
if pellet == "collect":
    time.sleep(3)
print("You idiot in this world it is kill or be killed.")
time.sleep(2)
print("You are surrounded by the flower’s bullets")
time.sleep(3)
print("Suddenly the flower is hit with a fireball")
time.sleep(1)
print("A goat appears?")
time.sleep(1)
print("The goat: What a terrible creature, torturing such a poor, innocent youth... Ah, do not be afraid, my child. I am Toriel, caretaker of the Ruins... I pass through this place every day to see if anyone has fallen down.")
time.sleep(4)
print("Toriel: You must have fallen down... do not worry I will take care of you.")
time.sleep(1)
print("Toriel: Please follow me this way")
time.sleep(1)
print("You follow Toriel into the next room")
time.sleep(1)
print("Toriel: Allow me to educate you on the workings of the ruins... \n The ruins are full of puzles and you must solve them to advance to the next room")
time.sleep(2)
print("Toriel walks across a series of buttons")
time.sleep(1)
print("After completing the process a door opens...")
time.sleep(1)
print("You follow Toriel to the next room")
time.sleep(1)
print("Toriel: Listen child... I am going to ask you to do something very challenging... \n I need you to walk to the end of this room... by yourself.")
time.sleep(1)
print("Toriel runs down the hall")
time.sleep(1)
print("You follow her")
time.sleep(3)
print("You continue to follow her")
time.sleep(5)
print("...")
time.sleep(5)
print("You are almost to the end of the hallway")
time.sleep(1)
print("You see a pillar... look behind it? (yes or no)")
lookbehindpillar = input(":")
if lookbehindpillar == "yes":
    time.sleep(1)
    print("You look behind the pillar and see Toriel")
    time.sleep(1)
    print("Toriel: ...")
    time.sleep(2)
if lookbehindpillar == "no":
    time.sleep(1)
print("You reach the end of the hallway")
time.sleep(1)
print("Toriel comes out from behind the pillar")
time.sleep(1)
print("Toriel: It is okay child do not worry I did not leave you I am sorry if I frightend you...")
time.sleep(1)
print("Toriel: I have to run an erand. \n Please remain in this room until I get back... it is dangerous to continue.")
time.sleep(1)
obeytorielandleaveroom = input("continue or do not")
if obeytorielandleaveroom == "do not":
    print("You wait for around 10 minutes...")
    time.sleep(5)
    print("You get bored and continue")
if obeytorielandleaveroom == "continue":
    time.sleep(1)
print("You leave the room and encounter a froggit")
time.sleep(2)
print("compliment or fight...")
firstfroggitcomporfight = input("")
if firstfroggitcomporfight == "fight":
    time.sleep(1)
    print("You killed the froggit...")
    time.sleep(2)
    print("You gained LOVE!")
    totallove = totallove + 1
    print(f"Your love is now at {totallove}")
    time.sleep(1)
if firstfroggitcomporfight == "compliment":
    time.sleep(1)
    print("The froggit does not understand but is flattered anyway... \n You spare the froggit")
    time.sleep(1)
print("You move on")
time.sleep(1)
print("You are now in a room with two doors. Go up or down")
firstroomupordownmostercandy = input("(up or down):")
if firstroomupordownmostercandy == "up":
    print("You go up and see a dish. It is labeled Free Candy Take One")
    takethecandyyorn = input("Take a peice of candy?(yes or no)")
    if takethecandyyorn == "yes":
        print("You take a peice of candy... it tastes like a gym sock...")
        time.sleep(1)
print("You go back to the main room and head down the hall")
time.sleep(2)
print("In the next room there is a rock and a big waited button and the exit is covered with spikes")
time.sleep(2)
print("Do you want to push the rock on to the pad")
pushsinglerockontopad = input("(yes or no)")
time.sleep(2)
if pushsinglerockontopad == "no":
    print("You do not push the rock on to the pad however you cannot progress past the spikes")
    time.sleep(2)
    print("You realize you have to push the rock")
time.sleep(2)
print("You push the rock onto the pad... \n The spikes drop into the floor")
time.sleep(2)
print("You progress to the next room")
time.sleep(2)
print("You see three rocks with three similar pads and more spikes")
time.sleep(2)
print("You move the rocks onto the pads")
time.sleep(1)
print("The spikes fall into the ground")
time.sleep(1)
print("There are a pile of leaves on the floor")
time.sleep(2)
print("There is a ghost laying on top of them")
time.sleep(2)
print('The ghost is saying "z" outload repeatedly')
time.sleep(2)
print("Move it with force?")
movenabstablookwithforceyesorno = input("yes or no")
if movenabstablookwithforceyesorno == "no":
    print("The ghost keeps saying 'z' outloud repeatedly... \n You have no choice but to move it with force")
    time.sleep(1)
time.sleep(1)
print("Here comes Nabstablook")
time.sleep(1)
whattodonabfirst = input("Attack or Cheer")
time.sleep(1)
if whattodonabfirst == "Cheer":
    print("Nabstablook: heh...")
    time.sleep(1)
    print("Nabstablook attacks!")
    time.sleep(1)
    print("You take 1 damage!")
    time.sleep(1)
    print("You tell nabstablook a joke...")
    time.sleep(1)
    print("Nabstablook: heh heh...")
    time.sleep(2)
    print("Nabstablook wants to show you something...")
    print("Let me try...")
    time.sleep(2)
    print("Nabstablook makes itself a hat")
    time.sleep(2)
    print("Nabstablook: Do you like it? I call it dapperblook.")
    time.sleep(2)
    print("You say you like it")
    time.sleep(2)
    print("Nabstablook: Gee. I usually come to the ruins because no one is around but today I met someone nice!")
    time.sleep(2)
    print("I will get out of your way now...")
    time.sleep(2)
if whattodonabfirst == "Attack":
    print("Nabstablook:... You know you can't kill me right? I'm like... A ghost and all.")
    time.sleep(2)
    print("Nabstablook: This is awkward I will just get out of your way")
    time.sleep(2)
print("You walk past the leaves nabstablook was on")
time.sleep(2)
print("You encounter a whimsun!")
time.sleep(2)
print("Attack or Spare")
killorsparewhismunfirst = input(":")
if killorsparewhismunfirst == "Attack":
    print("You killed the whimsun in 1 shot!")
    time.sleep(2)
    totallove = totallove + 1
    print("Your LOVE has increased!")
    print(f"You are now at {totallove} LOVE!")
    time.sleep(1)
if killorsparewhismunfirst == "Spare":
    print("You spare the Whimsun")
    time.sleep(1)
print("You continue to progress")
time.sleep(2)
print("There is another room with two door ways")
spiderbakesaleornah = input("Go right or up: ")
if spiderbakesaleornah == "right":
    print("You go to the right... \n You see a spider web with lots of spiders")
    time.sleep(2)
    print("There is a sign that says 'Spider Bake Sale'")
    time.sleep(2)
    print("There is a spider in the web")
    time.sleep(2)
    spiderbakesaledialog = input("(What is going on here or What are the prices)")
    if spiderbakesaledialog == "what is going on here" or spiderbakesaledialog == "What is going on here" or spiderbakesaledialog == "What are the prices" or spiderbakesaledialog == "what are the prices":
        print("This is a spider bakesale, we sell spider donuts. The prices are 7 gold each")
        time.sleep(2)
        print("Do you want to buy a donut")
        buyadonutorno = input(":")
        if buyadonutorno == "yes":
            print("You purchased a donut")
            time.sleep(2)
print("You enter the 'up' room")
time.sleep(2)
print("You are outside!")
time.sleep(2)
print("You see Toriel returning")
time.sleep(2)
print("Toriel: Oh my I should not have left you alone for so long...")
time.sleep(2)
print("I am sorry that was foolish of me")
time.sleep(2)
print("Come with me")
time.sleep(2)
print("Toriel leads you into a house")
time.sleep(2)
print("This is your home now!")
time.sleep(2)
print("I suppose I cant hide it from you anymore...")
time.sleep(2)
print("SURPISE!")
time.sleep(1)
print("I baked you a butterscotch pie!")
time.sleep(2)
print("Oh my god! I think I left it in the oven!")
time.sleep(2)
print("I will be back child!")
time.sleep(2)