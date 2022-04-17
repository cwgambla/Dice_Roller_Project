"""
This is a dice rolling program, which will be using Tkinter
as the graphical user interface
"""

import tkinter as tk
from tkinter import ttk
#main
def main():
    root = tk.Tk()

    #changes widget title
    root.title("DICE ROLLER PROGRAM")

    #need to work on file pathing for Linux operating system
    #root.iconbitmap(r'.dice_icon.ico')
    root.geometry("700x800+0+0")

    #changes message
    ttk.Label(root, text = "DICE ROLLER").pack()
    

    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        root.mainloop()
   
main();
    
