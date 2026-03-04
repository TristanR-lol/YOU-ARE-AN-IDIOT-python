from tkinter import *
from random import randint

root = Tk()
root.withdraw()

def Move(Window):
    ScreenW = root.winfo_screenwidth()
    ScreenH = root.winfo_screenheight()
    Window.geometry("200x100+" + str(randint(1, ScreenW)) + "+" + str(randint(1, ScreenH)))
    Window.after(50, Move, Window)

def Create_Window():
    Window = Toplevel(root)
    Window.title("You cant catch me >:)")
    Move(Window)

for i in range(10):
    Create_Window()

root.mainloop()