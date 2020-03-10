import os,shutil,os.path,sys,glob,datetime
import filecmp
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox,filedialog

app = Tk()
app.title("Attacker: Copy file to attacker's folder")
app.geometry("500x200")
holderlist = []
#==========Function button browse to public folder=============
def browseBtnPublic():
    global track_path
    askDirectoryTrack= filedialog.askdirectory()   
    track_path.set(askDirectoryTrack) 
    os.chdir(askDirectoryTrack)
    src = os.getcwd()
    print("1",src)
    for f in os.listdir():
       print(os.path.splitext(f))
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
    #for f in os.listdir():
      #  print(f)
lbl3 = Label(app,text="Attacker's directory:")
lbl3.grid(column=0, row=2, sticky='W')

butBrsAt = Button(app, text='Browse',command=browseBtnAttacker) 
butBrsAt.grid(column=0, row=3)
dest_path = StringVar()
lbl4 = Label(app, textvariable=dest_path)
lbl4.grid(column=1, row=3,sticky='W')
#==========Start button-Function to start tracking===
src = "C:/Users/phanh/source/repos/Lab1/public"
dst = "C:/Users/phanh/source/repos/Lab1/attacker"
def are_dir_trees_equal(src, dst):
    dirs_cmp = filecmp.dircmp(src,dst)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        src, dst, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_src = os.path.join(src, common_dir)
        new_dst = os.path.join(dst, common_dir)
        if not are_dir_trees_equal(new_src, new_dst):
            return False
    return True
startBtn = Button(app,text='Start tracking!',command=are_dir_trees_equal(src,dst))
startBtn.grid(column=1, row=6, sticky='W')

#==================================================



app.mainloop()
