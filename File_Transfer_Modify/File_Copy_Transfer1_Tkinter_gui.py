from tkinter import *
import tkinter as tk

import File_Copy_Transfer1_Tkinter_main
import File_Copy_Transfer1_func

def OpenWin(self):

    self.txt_fname1 = tk.Entry(self.master ,width=15, font=('Arial 17'),text="")
    self.txt_fname1.grid(row=10,column=5, rowspan=1,columnspan=5,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
    self.txt_fname = tk.Entry(self.master ,width=10, font=('Arial 17'),text="")
    self.txt_fname.grid(row=11,column=5, rowspan=1,columnspan=5,padx=(25,0),pady=(35,10),sticky=N+E+W)

    self.btn_Submit = tk.Button(self.master, width=22, height=2, text = ' Folder to Check',command=lambda: File_Copy_Transfer1_func.Folder_Origin(self))
    self.btn_Submit.grid(row=10, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
    self.btn_Submit = tk.Button(self.master, width=12, height=2, text = 'File transfer recieving folder',command=lambda: File_Copy_Transfer1_func.Folder_Dest(self))
    self.btn_Submit.grid(row=11, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
    self.btn_Submit = tk.Button(self.master, width=12, height=2, text = 'Initiate File transfer',command=lambda: File_Copy_Transfer1_func.GetFileList(self))
    self.btn_Submit.grid(row=12, column=0,padx=(25,0),pady=(35,10),sticky=N+E+W)
    
    self.btn_Submit = tk.Button(self.master, width=12, height=2, text = 'Close Program')
    self.btn_Submit.grid(row=12, column=9,padx=(460,0),pady=(35,10))    ## first number from right second from left 
if __name__ == "__main__":
    pass
