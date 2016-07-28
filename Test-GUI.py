#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from server import server
import os
import re
import string

import MySQLdb

#db = MySQLdb.Connect()

test_list = [
    'ls',
    'pwd',
    '/usr/bin/gnome-terminal',
    'touch whatever.iso'
]

class appgui():
    def __init__(self):
        self.root = Tk()
        self.root.title("Testitest")

    def create_listbox(self):
        """Creates a listbox object to contain a list, for example of the current instances or available missions"""
        self.test_listbox = tkinter.Listbox(self.root)
        self.test_listbox.bind('<<ListboxSelect>>', self.listbox_changed) # If an Item in the list is selected, do something
        self.test_listbox.grid(columnspan=2)    # This widget shall span over 2 columns so that its as wide as the whole window

        self.test_label = tkinter.Label(self.root, text="Test Box")
        self.test_label.grid(column='1', row='0', sticky=N+S+E+W)

    def fill_listbox(self, list):
        for i, item in enumerate(list):   # iterate through the list and fill the listbox with its content
            self.test_listbox.insert(i, item)

    def listbox_changed(self, *args, **kwargs):
        selection_index = self.test_listbox.curselection()
        selection_text = self.test_listbox.get(selection_index, selection_index)
        self.test_label.config(text=selection_text)
        print(selection_text)

    def dosomething(self):
        selection_index = self.test_listbox.curselection()
        selection_text = self.test_listbox.get(selection_index, selection_index)
        selection_text = str(selection_text)
        refined_text = self.applie_char_whitelist(selection_text)
        print(refined_text)

    def applie_char_whitelist(self, text):
        whitelist = string.ascii_letters + string.digits + ' -./'
        new_s = ''.join(c for c in text if c in whitelist)
        return str(new_s)


    def create_buttons(self):
        self.button1 = ttk.Button(self.root, text="Instanz 1", command=lambda : self.dosomething(), default="disabled")
        self.button1.grid(column=0, row=0, sticky=N+S+E+W)
        self.button1.des




    def run(self):
        list = [
            'ls',
            'pwd',
            '/usr/bin/gnome-terminal',
            'touch whatever.iso'
        ]
        self.create_buttons()
        #self.scrollbar_listbox()
        self.create_listbox()
        self.fill_listbox(list)
        self.root.mainloop()

if __name__ == '__main__':
    app = appgui()
    app.run()

