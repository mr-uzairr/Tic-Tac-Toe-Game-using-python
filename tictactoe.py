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
