
#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import Quadratics as q
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIdzSSIE
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Quadcalc2App:
    def __init__(self, master=None):
        # build ui
        self.top_level = ttk.Frame(master)
        self.top_level.configure(height=200, padding=10, width=200)
        self.header_label = ttk.Label(self.top_level)
        self.header_label.configure(
            font="{Arial} 24 {}",
            justify="left",
            padding=10,
            relief="raised",
            takefocus=True,
            text='Quadratic Function Roots Calculator')
        self.header_label.grid(column=0, row=0)
        label2 = ttk.Label(self.top_level)
        self.img_quadfun = tk.PhotoImage(file=resource_path("/Users/johnprichard/Downloads/lab08JakePpycharm/quadfun.png"))
        label2.configure(image=self.img_quadfun, text='label2')
        label2.grid(column=0, row=1)
        self.description_1 = ttk.Label(self.top_level)
        self.description_1.configure(
            font="{Arial} 20 {}",
            padding=10,
            text='Enter values for a, b, and c.')
        self.description_1.grid(column=0, row=2, sticky="w")
        self.input_frame = ttk.Frame(self.top_level)
        self.input_frame.configure(height=200, width=200)
        self.a_label = ttk.Label(self.input_frame)
        self.a_label.configure(font="{Arial} 20 {}", text='a=')
        self.a_label.grid(column=0, row=0)
        self.a_entry = ttk.Entry(self.input_frame)
        self.a_entry.grid(column=1, row=0)
        self.b_label = ttk.Label(self.input_frame)
        self.b_label.configure(font="{Arial} 20 {}", text='b=')
        self.b_label.grid(column=0, row=1)
        self.b_entry = ttk.Entry(self.input_frame)
        self.b_entry.grid(column=1, row=1)
        self.c_label = ttk.Label(self.input_frame)
        self.c_label.configure(font="{Arial} 20 {}", text='c=')
        self.c_label.grid(column=0, row=2)
        self.c_entry = ttk.Entry(self.input_frame)
        self.c_entry.grid(column=1, row=2)
        self.input_frame.grid(column=0, row=3, sticky="w")
        self.button_frame = ttk.Frame(self.top_level)
        self.button_frame.configure(height=200, width=350)
        self.ok_button = ttk.Button(self.button_frame)
        self.ok_button.configure(text='OK')
        self.ok_button.grid(column=0, row=0)
        self.ok_button.configure(command=self.calculate)
        self.clear_button = ttk.Button(self.button_frame)
        self.clear_button.configure(text='Clear')
        self.clear_button.grid(column=3, padx=30, pady=30, row=0)
        self.clear_button.configure(command=self.clear)
        self.button_frame.grid(column=0, row=4, sticky="w")
        self.top_level.grid(column=0, row=0)

        # Main widget
        self.mainwindow = self.top_level

    def run(self):
        self.mainwindow.mainloop()

    def calculate(self):
        # gets the entries for a,b, and c and assigns them to variables.  The passes those variables into a function
        # called calculate from the quadratics module.  The calls the show_answer method to display the answer window.
        a = self.a_entry.get()
        b = self.b_entry.get()
        c = self.c_entry.get()
        top2 = tk.Toplevel(self.mainwindow)
        answer = q.calculate(a, b, c)
        self.show_answer(top2, answer)

    def clear(self):
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)

    def show_answer(self, master, text):
        #creates the window that shows the answer to the user.
        root_frame = ttk.Frame(master, padding=10)
        root_frame.grid(column=0, row=0)
        header_label = ttk.Label(root_frame, text="The Answer", font="{Arial} 20 {bold}")
        header_label.grid(column=0, row=0)

        answer_label = ttk.Label(root_frame, text=text, justify=tk.CENTER)
        answer_label.grid(column=0, row=1)
    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.mainwindow

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quadratic Function Roots Calculator")
    app = Quadcalc2App(root)
    app.run()



