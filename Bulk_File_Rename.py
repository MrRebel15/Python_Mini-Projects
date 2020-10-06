import os
from tkinter import *


def Rename():
    folder_Path=r''+path.get()
    counter=1
    for files in os.listdir(folder_Path):
        os.rename(folder_Path+'\\'+files,folder_Path+'\\'+word.get()+str(counter)+ext.get())
        counter+=1


root=Tk()
root.title("Bulk_File_Renaming")
root.geometry('600x400')


path=StringVar()
Directory=Label(root,text='Enter the Directory',font=("TimesNewRoman",'12')).pack()
directory_entry=Entry(root,textvariable=path,font=("TimesNewRoman",'12')).pack()

word=StringVar()
name=Label(root,text='Enter Name',font=("TimesNewRoman",'12')).pack()
name_entry=Entry(root,textvariable=word,font=("TimesNewRoman",'12')).pack()


ext=StringVar()
extension=Label(root,text='Enter Name',font=("TimesNewRoman",'12')).pack()
extension_entry=Entry(root,textvariable=ext,font=("TimesNewRoman",'12')).pack()


btn=Button(root,text='change' ,command=Rename).pack()

root.mainloop()