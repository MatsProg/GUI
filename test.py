import tkinter as tk
from tkinter.ttk import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.UpdateBar(40, 50, 60, 70)
        self.Progressbar1()





    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def UpdateBar(self, P1, P2, P3, P4):
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3
        self.P4 = P4
        return self.P1, self.P2, self.P3, self.P4
    def Progressbar1(self):

        self.paa1 = Progressbar(root, orient="vertical", length=200, mode="determinate")
        self.paa2 = Progressbar(root, orient="vertical", length=200, mode="determinate")
        self.paa3 = Progressbar(root, orient="vertical", length=200, mode="determinate")
        self.paa4 = Progressbar(root, orient="vertical", length=200, mode="determinate")
        self.paaList = [self.paa1, self.paa2, self.paa3, self.paa4]
        for x in self.paaList:
            x.pack()
           # x.start()
        self.paa1['value'] = self.P1
        self.paa2['value'] = self.P2
        self.paa3['value'] = self.P3
        self.paa4['value'] = self.P4




    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
app.UpdateBar(40,50,60,90)