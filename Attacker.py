import os,shutil,os.path,sys,glob,re
import filecmp
import multiprocessing
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
    target_files = []
    askDirectoryTrack= filedialog.askdirectory()   
    track_path.set(askDirectoryTrack) 
    os.chdir(askDirectoryTrack)
    src = os.getcwd()
    print("1",src)
    
    for f in os.listdir(src):
        target_files.append(f)
        lstbox_target = Listbox(app) #List box to show all files in target folder
    for fl in target_files:    
        lstbox_target.insert(END,fl)
    lstbox_target.grid(column=1,row=2,ipadx=20) 
           
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
        print(f)

lbl3 = Label(app,text="Attacker's directory:")
lbl3.grid(column=0, row=3, sticky='W')

butBrsAt = Button(app, text='Browse',command=browseBtnAttacker) 
butBrsAt.grid(column=0, row=4)
dest_path = StringVar()
lbl4 = Label(app, textvariable=dest_path)
lbl4.grid(column=1, row=4,sticky='W')
#==========Start button-Function to start tracking===
src = r"C:\Users\phanh\source\repos\Lab1\public"
dst = r"C:\Users\phanh\source\repos\Lab1\attacker"
found_files = []
def Track():
    for file in glob.glob(os.path.join(src,'*.*'),recursive=True):
        shutil.copy(file,dst)
        found_files.append(file)

    listbox = Listbox(app) #listbox to show all target files
    len_max = 0
    for a_file in found_files:
        if len(a_file)> len_max:
            len_max = len(a_file)
        listbox.insert(END,a_file)
    listbox.grid(column=1, row=6, ipadx = 100)
    '''
    def rename():
        for file in enumerate(os.listdir(dst)):
            create_time = os.path.getctime(file)
            modified_time = os.path.getmtime(file)
            modified_date = datetime.date.fromtimestamp(modified_time)
            format_time = datetime.datetime.fromtimestamp(create_time)
            format_time_string = format_time.strftime("%d-%m-%Y %H:%M:%S" "-"+ file) # e.g. 01-04-2020 09.03.45-demo.txt
            newfile = format_time_string      
            os.rename(file,newfile)
    rename()
    '''
startBtn = Button(app,text='Start tracking!',command=Track)
startBtn.grid(column=1, row=7, sticky='W')





#==================================================



app.mainloop()
