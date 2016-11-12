#!/usr/bin/env python

from Tkinter import *
import time
import webbrowser
import random
import re

def setalarm():
	screen.title("Running")
	url = Entry.get(E1)
	Alarm = int(Entry.get(E2))
	reg=re.compile("[^(https|http):\/\/]")
	if reg.match(url):
		url = 'http://'+ url
	
	Alarm = time.time() + (int(Alarm)*60)
	Time = time.ctime()
	Alarm = time.ctime(Alarm)
	
	f = open("YT.txt", "r")
	content = f.readlines()
	random_music = random.choice(content)
	random_music = random_music.rstrip()
	
	while Alarm != Time:
		Time = time.ctime()

	if Time == Alarm:
		webbrowser.open(random_music)
		time.sleep(5)
		webbrowser.open(url,new=0, autoraise=True)


screen = Tk()
screen.geometry("350x200")
screen.title("Set Alarm")

var = StringVar()
msg = Message( screen, textvariable=var, relief=RAISED ,width=300 )
var.set("Set Alarm for url to open in specified minutes ")
msg.pack()

L1 = Label(screen, text="Url")
L1.place(x=20,y=50)

E1 = Entry(screen, bd =2, width=30)
E1.place(x=50,y=50)

L2 = Label(screen, text="Mins")
L2.place(x=20,y=90)

E2 = Entry(screen, bd =2, width=30)
E2.place(x=50,y=90)

B1 = Button(screen, text = "Set", command = setalarm)
B1.place(x=150,y=150)

screen.mainloop()