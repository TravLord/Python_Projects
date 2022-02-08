import os
import os.path
import shutil
from datetime import datetime, timedelta
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import *

class ParentWindow(Frame):                      # Frame is primary tkinter class object.
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master         #master level frame
        self.master.minsize(315,315)   #(Height, Width)
        self.master.maxsize(315,315)

        #accessing phonebook_func.center script (center_window function)
        self.master.title("Recently Created and Modified File Transfer Initiator")
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        self.btn_Submit = tk.Button(self.master, width=22, height=2, text = ' Folder to Check',command = lambda:pickSourceDir())
        self.btn_Submit.grid(row=10, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
        self.btn_Submit = tk.Button(self.master, width=12, height=2, text = 'File transfer recieving folder',command =lambda:pickDestDir())
        self.btn_Submit.grid(row=11, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
        self.btn_Submit = tk.Button(self.master, width=12, height=2, text = 'Initiate File transfer',command= lambda: moveFiles())
        self.btn_Submit.grid(row=12, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    


def pickSourceDir():
    name = tkinter.filedialog.askdirectory()
    originPath.set(name)    
    
   
def pickDestDir():
    name = tkinter.filedialog.askdirectory()
    destDir.set(name)
    
def moveFiles():
    source = originPath.get()
    dest = destDir.get()
    fileList = os.listdir(source)

    cur_time = datetime.now()
    print("current time" + str(cur_time))

    for i in fileList:
          file_path = os.path.join(source, i)
          #changing the time until the past 24 hours
          past_24hrs = cur_time - timedelta(hours=24)
          #gettting the modifacation date of the files
          mod_date_in_sec = os.path.getmtime(file_path)
          #converting the time from seconds into days
          recent_update_files = datetime.fromtimestamp(mod_date_in_sec)
          if past_24hrs < recent_update_files:
              shutil.copy2(source + '/' + i, dest)
              print(i + 'File transfer successful!')
          else:
              print("No recent updates to files.")
        

if __name__=='__main__':
    root = tk.Tk()  # this creates the window
    originPath = StringVar()
    destDir = StringVar()
    App = ParentWindow(root)    # attach root/window Parentwindow
    root.mainloop()              


  

