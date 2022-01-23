import sqlite3

conn = sqlite3.connect('MyDB.db')   # this connect method creates a database 
with conn:                   # cursor method operates the db when commands are given
    cur = conn.cursor()   # Adding table and columns to dB
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_customers(\
        custID INTEGER PRIMARY KEY AUTOINCREMENT, \
        custFname TEXT, \
        FileName TEXT \
        )')
    conn.commit()

# tuple with filelist names to pull from
FileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')            
for x in FileList:          # this for loop iterates through the tuple to find files ending with t
    if x.endswith('t'):
        with conn:
            cur = conn.cursor()  #this command(below) inserts files(ending in t) into FileName column
            cur.execute('INSERT INTO tbl_customers (FileName) VALUES (?)',(x,))
        print(x)
    conn.commit()
conn.close()
