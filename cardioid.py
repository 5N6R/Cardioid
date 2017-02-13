# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from tkinter import *
from random import *
import math
def stars():
	for i in range(0,800):
		xx=randint(0,600)
		yy=randint(0,400)
		c.create_oval(xx,yy,xx+2,yy+2,fill=choice(["lightblue","blue","darkblue","lightyellow","yellow"]))
		c.update()
def plot_f():
	for t in range(0,1000):
		x=80*math.sin(t)-24*math.sin(3*t)
		y=80*math.cos(t)+24*math.cos(2*t)-15*math.cos(3*t)-math.cos(4*t)
		c.create_oval(x+300,y+130,x+301,y+151,outline="red")
		c.create_oval(x+302,y+132,x+303,y+153,outline="darkred")
		c.update()
def txt():
	c.create_text(300,300,text="С Днем Всех Влюбленных!",font="Verdana 25",fill="red")
	c.create_text(301,301,text="С Днем Всех Влюбленных!",font="Verdana 25",fill="darkred")
app=Tk()
app.title(chr(9825)*3+" Cardioid версия 0.14.2 бета "+chr(169)+" 2017, программирование 5n6r "+chr(9825)*3)
app.geometry("600x400")
app.resizable(0,0)
c=Canvas(app,width=599,heigh=399,bg="black",cursor = "heart")
stars()
plot_f()
txt()
c.pack()
app.mainloop()

