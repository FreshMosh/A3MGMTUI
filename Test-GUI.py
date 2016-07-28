#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from server import server
import os

import MySQLdb

#db = MySQLdb.Connect()



class appgui():
    def __init__(self):
        self.root = Tk()
        self.root.title("Testitest")

        self.test_list = [
            'ls',
            'pwd',
            'gnome-terminal'
        ]

    def create_listbox(self):
        self.test_listbox = tkinter.Listbox(self.root)
        self.test_listbox.bind('<<ListboxSelect>>', self.listbox_changed)
        self.test_listbox.grid(columnspan=2)

        for i, item in enumerate(self.test_list):
            self.test_listbox.insert(i, item)

        self.test_label = tkinter.Label(self.root, text="Test Box")
        self.test_label.grid(column='1', row='0', sticky=NSEW)

    def listbox_changed(self, *args, **kwargs):
        selection_index = self.test_listbox.curselection()
        selection_text = self.test_listbox.get(selection_index, selection_index)
        self.test_label.config(text=selection_text)
        print(selection_text)

    def dosomething(self):
        selection_index = self.test_listbox.curselection()
        selection_text = self.test_listbox.get(selection_index, selection_index)
        selection_text = str(selection_text)
        print(selection_text)

        #os.system(selection_text)


    def create_buttons(self):
        self.button1 = ttk.Button(self.root, text="Instanz 1", command=lambda : self.dosomething(), default="disabled")
        self.button1.grid(column=0, row=0, sticky=NSEW)




    def run(self):
        self.create_buttons()
        self.create_listbox()
        #self.scrollbar_listbox()
        self.root.mainloop()

if __name__ == '__main__':
    app = appgui()
    app.run()

