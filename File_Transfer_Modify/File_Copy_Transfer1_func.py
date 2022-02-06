import glob
import os
import datetime
import shutil
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

import File_Copy_Transfer1_Tkinter_main
import File_Copy_Transfer1_Tkinter_gui


def GetFileList(path, type):
    '''
    Return a list of filename matching the given path and file type
    '''
    return glob.glob(path + "*" + type)

#### This is my problem I need to get the users input to add as the origin path and destination path
#### I've tried several different approaches but can't seem to get it quite right 
#### I need to reference the File_Copy_Transfer1_Tkinter_gui document in order to get my variable txt_fname which is
#### the entry field for user inputted filepath
#### when I put this in a function then the vars originPath and destinationPath can't acess them anymore because they're local
inp = self.txt_fname1.get(1.0, "end-1c")
inp1 = self.txt_fname.get(1.0, "end-1c")

originPath = inp
destinationPath = inp1
fileType = ".txt"

# Create list of text filenames in Origin folder
fileList = GetFileList(originPath, fileType)

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
         shutil.copy2(file, destinationPath + filename)

# function to get file from directory and insert into text field 
def Folder_Origin(self):
    SaveFile1 = tk.filedialog.askdirectory()
    self.txt_fname1.insert(0,str(SaveFile1))
    return SaveFile1

def Folder_Origin_File_In(self):
    temp1 = self.txt_fname1.insert(Folder_Origin())
    return temp1

def Folder_Dest(self):
    SaveFile = tk.filedialog.askdirectory()
    self.txt_fname.insert(0,str(SaveFile))
    return SaveFile

def Folder_Dest_File_In1(self):
    temp = self.txt_fname.insert(Folder_Dest())
    return temp


    

    


