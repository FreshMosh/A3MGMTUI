import string
import tkinter
from tkinter import Tk, ttk
from tkinter import *
import menu_bar as mb
import MySQLdb


class gui_app():
    def __init__(self, root):
        self.root = root
        self.root.title("SRV MGMT")
        self.frame_upper = tkinter.Frame(root)
        self.frame_lists = tkinter.Frame(root)
        self.frame_lower = tkinter.Frame(root)
        self.button_1 = ttk.Button(self.frame_lists, text="jlkjlk")
        self.root.grid()
        self.frame_lists.grid()



if __name__ == '__main__':
    root = Tk()
    app = gui_app(root)
    app.
