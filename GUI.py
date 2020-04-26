import tkinter as tk
from tkinter.ttk import Progressbar


class tkinter1():
	def __init__(self):
		self.app = tk.Tk()

	def MainWindow(self):
		self.app.title('Manager')

		self.app.geometry('700x400')

		self.app.image = tk.PhotoImage(file='2.png')
		self.label = tk.Label(self.app, image=self.app.image, bg='white')
		self.app.wm_attributes("-transparentcolor", "white")  # TRANSPARENCY
		self.label.pack()
		self.app.lift()
		self.app.mainloop()
		bar = Progressbar(self.app, length=200, style='black.Horizontal.TProgressbar')
		bar['value'] = 70
		bar.grid(column=0, row=0)


	# self.style = ttk.Style()
	# self.style.theme_use('default')
	# self.style.configure("black.Horizontal.TProgressbar", background='black')





# bb = tkinter1
# bb.Bar()

# app.overrideredirect(True) #Borderless

# app.wm_attributes("-topmost", True)
# app.wm_attributes("-disabled", True)


# window = MainWindow()
win = tkinter1()
win.MainWindow()
win.Bar()

input()
