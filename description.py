import tkinter as tk
import tkinter.ttk as ttk
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIdzSSIE
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class TheaboutApp:
    def __init__(self, master=None):
        # build ui
        self.top_level = ttk.Frame(master)
        self.top_level.configure(height=200, width=200)
        self.header_label = ttk.Label(self.top_level)
        self.header_label.configure(
            font="{Arial} 20 {bold underline}",
            justify="left",
            relief="flat",
            takefocus=False,
            text='Quadratic Roots Calculator')
        self.header_label.grid(column=0, row=0)
        self.description_label = ttk.Label(self.top_level)
        self.description_label.configure(
            font="{Arial} 16 {bold}",
            text='Featuring a calculator that finds the roots of any quadratic function.')
        self.description_label.grid(column=0, padx=10, pady=15, row=1)
        frame3 = ttk.Frame(self.top_level)
        frame3.configure(height=200, width=200)
        self.description_two = ttk.Label(frame3)
        self.description_two.configure(
            compound="none",
            font="{Arial} 12 {}",
            text='-The roots of a quadratic function are the functions x-intercepts or the \nsolution to the equation.....')
        self.description_two.grid(column=0, padx=20, row=0, sticky="w")
        label6 = ttk.Label(frame3, class_="image")
        self.img_stdform = tk.PhotoImage(file=resource_path("/Users/johnprichard/Downloads/lab08JakePpycharm/stdform.png"))
        label6.configure(image=self.img_stdform)
        label6.grid(column=0, padx=20, row=1)
        label7 = ttk.Label(frame3)
        label7.configure(
            text='-Users can plug in values of a,b, and c, and the calculator will produce the roots\n(solutions).')
        label7.grid(column=0, padx=20, row=2, sticky="w")
        label8 = ttk.Label(frame3)
        label8.configure(
            font="{Arial} 12 {}",
            padding=5,
            text='By Jake Prichard')
        label8.grid(column=0, ipadx=10, row=3, sticky="e")
        frame3.grid(column=0, row=2, sticky="w")
        self.top_level.grid(column=0, row=0)

        # Main widget
        self.mainwindow = self.top_level

    def run(self):
        self.mainwindow.mainloop()

    def get_top_frame(self):
        return self.mainwindow

if __name__ == "__main__":
    root = tk.Tk()
    app = TheaboutApp(root)
    app.run()

"""
#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import sys
import os


def resource_path(relative_path):
     Get absolute path to resource, works for dev and for PyInstaller 
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / resource_path("theAbout.ui")

class TheaboutApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.__mainwindow = builder.get_object("top_level", master)
        builder.connect_callbacks(self)

    def run(self):
        self.__mainwindow.mainloop()









    def get_top_frame(self):
       
        return self.__mainwindow

if __name__ == "__main__":
    root = tk.Tk()
    app = TheaboutApp(root)
    app.run()

"""