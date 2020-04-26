import tkinter as tk
from tkinter.ttk import *




class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        #self.create_widgets()
        #self.Progressbar1(22)

    def add(a):
        # returning sum of a and b
        return a

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def Progressbar1(self, w):

        self.paa1 = Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.paa1.pack()

        self.paa1['value'] = Application.add(w)




    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
#app.Upd(4)
app.Progressbar1()
app.mainloop()
#