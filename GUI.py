import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk


class tkinter1():
    def __init__(self):
        self.app = tk.Tk()


    def MainWindow(self):

        self.app.title('Manager')
        self.app.geometry('700x400')
        #self.app.image = tk.PhotoImage(file='2.png')
       # self.label = tk.Label(self.app, image=self.app.image, bg='white')
       # self.app.wm_attributes("-transparentcolor", "white")  # TRANSPARENCY
        #self.label.pack()
        self.app.lift()
        self.app.mainloop()
    def Bar(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='black')
        self.bar = Progressbar(self.app, length=200, style='black.Horizontal.TProgressbar')
        self.bar['value'] = 70
        self.bar.grid(column=0, row=0)






# app.overrideredirect(True) #Borderless

# app.wm_attributes("-topmost", True)
# app.wm_attributes("-disabled", True)


# window = MainWindow()
win = tkinter1()
win.MainWindow()
win.Bar()

input()
