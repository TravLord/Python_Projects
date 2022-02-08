import tkinter 
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import File_Copy_Transfer1_func
import File_Copy_Transfer1_Tkinter_gui



class ParentWindow(Frame):                      # Frame is primary tkinter class object.
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master         #master level frame
        self.master.minsize(760,315)   #(Height, Width)
        self.master.maxsize(760,315)

        #accessing phonebook_func.center script (center_window function)
        self.master.title("Recently Created and Modified File Transfer Initiator")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        File_Copy_Transfer1_Tkinter_gui.OpenWin(self)





if __name__=='__main__':
    root = tk.Tk()                       # this creates the window
    App = ParentWindow(root)    # attach root/window Parentwindow
    root.mainloop()              
