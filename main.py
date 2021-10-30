import tkinter.messagebox
from tkinter import *
import random

win=Tk() #creating the main window and storing the window object in 'win'
win.title('Choose your item') #setting title of the window
win.geometry('500x160') #setting the size of the window
win.resizable(False, False)


def func1():#function of Hammer
    num = random.randint(1,3)
    if num == 1:
        # Computer chose Hammer
        comp1 = 'Computer chose Hammer'
        outcome1 = 'Its a draw!'
    elif num == 2:
        # Computer chose Scissors
        comp1 = 'Computer chose Scissors'
        outcome1 = 'You win!'
    else:
        # Computer chose Paper
        comp1 = 'Computer chose Paper'
        outcome1 = 'You lose!'

    tkinter.messagebox.showinfo(outcome1, comp1)

def func2():#function of Scissors
    num = random.randint(1,3)
    if num == 1:
        # Computer chose Hammer
        comp1 = 'Computer chose Hammer'
        outcome1 = 'You lose!'
    elif num == 2:
        # Computer chose Scissors
        comp1 = 'Computer chose Scissors'
        outcome1 = 'Its a draw!'
    else:
        # Computer chose Paper
        comp1 = 'Computer chose Paper'
        outcome1 = 'You win!'
    tkinter.messagebox.showinfo(outcome1, comp1)

def func3():#function Paper button
    num = random.randint(1,3)
    if num == 1:
        # Computer chose Hammer
        comp1 = 'Computer chose Hammer'
        outcome1 = 'You win!'
    elif num == 2:
        # Computer chose Scissors
        comp1 = 'Computer chose Scissors'
        outcome1 = 'You lose!'
    else:
        # Computer chose Paper
        comp1 = 'Computer chose Paper'
        outcome1 = 'Its a draw!'

    tkinter.messagebox.showinfo(outcome1, comp1)

    
btn=Button(win,text="Hammer", width=10,height=5,command=func1)
btn.place(x=60,y=30)

btn=Button(win,text="Scissors", width=10,height=5,command=func2)
btn.place(x=200,y=30)

btn=Button(win,text="Paper", width=10,height=5,command=func3)
btn.place(x=340,y=30)

win.mainloop() #running the loop that works as a trigger