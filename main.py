from description import TheaboutApp
from Quadcalc import Quadcalc2App

import tkinter as tk
import tkinter.ttk as ttk

class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        self.__mainwindow = self.__main_notebook

        about_app = TheaboutApp(self.__mainwindow)

        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        quadroots_app=Quadcalc2App(self.__mainwindow)
        self.__main_notebook.add(quadroots_app.get_top_frame(), text="Quadratic Function Roots Calculator")

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()