import tkinter
from tkinter import *
import tkinter.filedialog
import glob
import os
import datetime
from datetime import timedelta
import shutil


import File_Copy_Transfer1_Tkinter_main
import File_Copy_Transfer1_Tkinter_gui


def pickSourceDir(self):
    name = tkinter.filedialog.askdirectory()
    originPath.set(name)    #  coming back undefined after directory is chose?  why?  
   
def pickDestDir(self):
    name = tkinter.filedialog.askdirectory()
    DestDir.set(name)
    
def moveFiles():
    source = originPath.get()

    dest = DestDir.get()

    fileList = os.listdir(source)
    
    for file in fileList:
        # Get last modified date and today's date
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
    
        filePathList = file.split("\\") # Create a list from the filepath
        filename = filePathList[-1] # The last element is a the filename
    
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        # If the file was edited less then 24 hours ago then copy it
        if modifyDateLimit > todaysDate:
         shutil.copy2(file, dest + filename)

         

# function to get file from directory and insert into text field 
def Folder_Origin(self):
    SaveFile1 = tkinter.filedialog.askdirectory()
    self.txt_fname1.insert(0,str(SaveFile1))
    return SaveFile1

def Folder_Origin_File_In(self):
    temp1 = self.txt_fname1.insert(Folder_Origin())
    return temp1

def Folder_Dest(self):
    SaveFile = tkinter.filedialog.askdirectory()
    self.txt_fname.insert(0,str(SaveFile))
    return SaveFile

def Folder_Dest_File_In1(self):
    temp = self.txt_fname.insert(Folder_Dest())
    return temp





    

    


