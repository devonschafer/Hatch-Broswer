from tkinter import *
from ui import UI
from dds import DDS


class Window:
    def __init__(self, master):
        self.master = master
        self.master.title('DDS Browser Alpha 0.2')
        self.master.geometry('800x800')

        u = UI(self.master)
        u.update()

root = Tk()
win = Window(root)
#root.after(0, Window.update(win))
root.mainloop()
