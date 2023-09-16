# Author:            Jake Prichard
# Lab:              Lab 8
# Date:             03/06/2023
# Description:      Program uses a GUI to display an app.  The app contains two tabs, an about tab and the main App.
#                   The main app is a calculator for calculating the roots of quadratic functions of the form
#                   y=ax^2+bx+c.  Users input values for a,b, and c and the app displays the roots of the function.
#
# Input:           a (float), b(float), c(float).
#
# Output:           1, 2 values are displayed to the user depending on the nature of the inputs.  The outputs can be
#                   either floating point numbers or complex numbers.
#
# Sources:         lab 08 specifications, textbook





from description import TheaboutApp
from Quadcalc import Quadcalc2App

import tkinter as tk
import tkinter.ttk as ttk
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class MainApp:
    def __init__(self, master):
        # build ui
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)


        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        self.__mainwindow = self.__main_notebook
        #calls the _init_method of the theAbout class.  Sets up the about tab.
        about_app = TheaboutApp(self.__mainwindow)
        #Label the tab that is connected to the theAbout class
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")
        #label the tab the is connected to the Quadcalc2App class
        quadroots_app=Quadcalc2App(self.__mainwindow)
        self.__main_notebook.add(quadroots_app.get_top_frame(), text="Quadratic Function Roots Calculator")

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()