from tkinter import Tk
from tkinter import ttk
from tkinter import *
import tkinter
import string

root = Tk()
frame0 = tkinter.Frame(root)
frame1 = tkinter.Frame(root)
frame2 = tkinter.Frame(root)
button1 = ttk.Button(frame1, text="Select")
button2 = ttk.Button(frame1, text="Edit")
button3 = ttk.Button(frame1, text="Switch", command=lambda:on_buttonpress())
listbox = tkinter.Listbox(frame2)
frame0.grid()
frame1.grid()
frame2.grid()
button1.grid(column=0,row=0,sticky=N+S+W+E)
button2.grid(column=1,row=0,sticky=N+S+W+E)
button3.grid(column=2,row=0,sticky=N+W+S+E)
listbox.grid(sticky=N+S+E+W, columnspan=3)
def listbox1_changed(listbox1, *args, **kwargs):
    selection_index = listbox1.curselection()
    selection_text = listbox1.get(selection_index, selection_index)
    new_s = applie_char_whitelist(selection_text)
    return str(new_s)

def applie_char_whitelist(self, text):
    whitelist = string.ascii_letters + string.digits + ' -./'
    new_s = ''.join(c for c in text if c in whitelist)
    return str(new_s)


def on_buttonpress():
    subroot = Tk()
    button1 = ttk.Button(subroot, text="Apply")
    button2 = ttk.Button(subroot, text="Change Mission")
    list = ['Mission1', 'Mission2', 'Mission3']
    listbox1 = tkinter.Listbox(subroot)
    for i, item in enumerate(list):
        listbox1.insert(i, item)
    button1.grid(column=0, row=0)
    button2.grid(column=1, row=0)
    listbox1.grid(columnspan=2, row=1)
    m = listbox1.bind('<<ListboxSelect>>',listbox1_changed(listbox1))  # If an Item in the list is selected, do something
    print(m)

root.mainloop()