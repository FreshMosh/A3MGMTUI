#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" TODO:
    Still plenty of work to do

    * Server_stop needs some rework

    """


import psutil
from configparser import ConfigParser
from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

class app():
    def __init__(self):
        root = Tk()
        self.config = ConfigParser() # Create a ConfigParser object called config
        self.config.read("config.ini") # Read the confi file to the config object
        ## Steam Standard Settings
        self.steam.exe = self.config.get("STEAM", "CMDPath")        # Set Path to the steamCMD exe
        self.steam.user = self.config.get("STEAM", "Username")      # Set the Username for Steam
        self.steam.password = self.config.get("STEAM", "Password")  # Set the Password for Steam
        ## Server Standard Settings
        self.server.appid = self.config.get("SERVER SETTINGS", "Branch-ID")         # Set the branch to use
        self.server.logdir = self.config.get("SERVER SETTINGS", "Log Directory")    # Set the log directory
        self.server.root = self.config.get("SERVER SETTINGS", "Root Directory")     # Set the Dir which will contain all instances
        self.server.moddir = self.config.get("SERVER SETTINGS", "Mod Directory")    # Set the Dir which will contain the mods
        self.server.mapdir = self.config.get("SERVER SETTINGS", "Map Directory")    # Dir for the Maps
        self.server.bikeydir = self.config.get("SERVER SETTINGS", "BiKey Directory")    # Dir for the BiKeys used by the mods
        ## Tools Standard Settings
        self.winscp = self.config.get("TOOLS", "WinSCP")    # Set the path to the WinSCP.exe
        self.java = self.config.get("TOOLS", "Java")        # Set the path to the Java.exe

        ## Some additional definitions
        self.server.instancedir = self.server.root + "A3_Instanzen\\"   # Concatenate the Instance dir
        self.server.missiondir = self.server.root + "A3_Missionen\\"    # Set the Mission dir
        self.instancesdict = {}

    def master_update(self):
        """Update the Master Instance"""
        instance = self.serverroot + "A3_Master"
        self.master = psutil.Popen([self.steam.exe, "+login", self.steam.user, self.steam.password, "+force_install_dir", instance, "+app_update", self.server.appid, "-validate +quit"])

    def server_start(self, instance, parameters):
        """Starts one Instance"""
        instance = self.server.root + instance
        instance.pid = psutil.Popen([instance, parameters])
        self.instancesdict.update({instance:instance.pid})

    def server_stop(self, instance):
        """Stops one Instance"""
        instance = self.instancesdict.get(instance)
        instance.kill()

    def server_update(self, instance):
        """Updates one Instance"""




Tk() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
print(filename)