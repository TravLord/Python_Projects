from tkinter import *
import tkinter as tk
from tkinter import messagebox

import WebPageGenerator2GUI



class ParentWindow(Frame):                      # Frame is primary tkinter class object
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master         #master level frame
        self.master.minsize(325,325)   #(Height, Width)
        self.master.maxsize(325,325)

        #accessing phonebook_func.center script (center_window function)
        self.master.title("Add some text within file")
        self.master.configure(bg="#708090")
        arg = self.master

        WebPageGenerator2GUI.WinOpen(self)




if __name__=='__main__':
    root = tk.Tk()                       # this creates the window
    App = ParentWindow(root)    # attach root/window Parentwindow
    root.mainloop()       
