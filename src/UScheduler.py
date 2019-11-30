import os
from tkinter import *

from src import interface


def create_interface(argv):
    cwd = os.path.dirname(os.path.abspath(__file__))

    root = Tk()
    root.title('Uni-Scheduler')
    root.geometry("659x337")
    root.tk.call('tk', 'scaling', 1.3)
    try:
        try:
            root.iconbitmap(f'{cwd}\\src\\assets\\unischeduler_icon.ico')
        except:
            root.iconbitmap(f'{cwd}\\assets\\unischeduler_icon.ico')
    except:
        pass
    interface.UserInterface(root)
    root.mainloop()


if __name__ == "__main__":
    create_interface(sys.argv)

