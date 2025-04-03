from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe Game")

PlayerA = StringVar()
PlayerB = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable = p1, bd = 5)
player1_name = Entry(row = 1, column = 1, columnspan = 8)
player2_name = Entry(tk, textvariable = p2, bd = 5)
player2_name = Entry(row = 2, column = 1, columnspan = 8)


bclick = True
flag = 0
def disableButton():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED)