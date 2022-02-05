from tkinter import *
import tkinter as tk

import WebPageGenerator2_main
import WebPageGenerator2_func


def WinOpen(self):



    self.lbl_fname = tk.Label(self.master, text ='Add new text to the file below: ')            #defined
    self.lbl_fname. grid(row=0, column=0, padx =(27,0),pady=(10,0),sticky=N+W)  #painted

   
    self.txt_fname = tk.Entry(self.master ,text="")
    self.txt_fname.grid(row=3,column=0, rowspan=1,columnspan=2,padx=(30,50),pady=(30,0), ipadx =(30), ipady = (30), sticky=N+E+W)


    self.btn_Submit = tk.Button(self.master, width=25, height=2, text = 'Update text & Create webpage!',command=lambda: WebPageGenerator2_func.Update(self))
    self.btn_Submit.grid(row=4, column=0,columnspan =4,padx=(25,0),pady=(50,10),sticky=N+E+W)

    

if __name__ == "__main__":
    pass
