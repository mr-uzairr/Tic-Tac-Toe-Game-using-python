from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe Game")

playerA = StringVar()
playerB = StringVar()
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

def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerB, playerA
    if buttons["text"] ==  " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerB = p2.get() + "Wins!!"
        playerA = p1.get() + "Wins!!"   
        checkforwin()
        flag += 1
    elif buttons["text"] ==  " " and bclick == True:
        buttons["text"] = "o"
        bclick = False
        playerB = p2.get() + "Wins!!"
        playerA = p1.get() + "Wins!!"   
        checkforwin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe","Button already clicked")    
    
    