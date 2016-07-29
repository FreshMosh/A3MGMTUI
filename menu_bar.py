from tkinter import *

def dosomething():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do something awsome here")
    button.pack()

def menus(root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=dosomething)
    filemenu.add_command(label="Open", command=dosomething)
    filemenu.add_command(label="Save", command=dosomething)
    filemenu.add_command(label="Save as...", command=dosomething)
    filemenu.add_command(label="Close", command=dosomething)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=dosomething)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=dosomething)
    editmenu.add_command(label="Copy", command=dosomething)
    editmenu.add_command(label="Paste", command=dosomething)
    editmenu.add_command(label="Delete", command=dosomething)
    editmenu.add_command(label="Select All", command=dosomething)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=dosomething)
    helpmenu.add_command(label="About...", command=dosomething)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    return root

if __name__ == '__main__':
    root = Tk()
    root.title("Sample Menu Bar")
    menus(root)
    root.mainloop()

