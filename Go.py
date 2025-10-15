import tkinter as tk
from EnzoGui import EnzoGUI
import sys
import os

if __name__ == "__main__":
    root = tk.Tk()
    if getattr(sys, 'frozen', False):  # se è un exe
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    lupin_path = os.path.join(base_path, "enzo.png")
    icon_path = os.path.join(base_path, "icon.png")


    gui = EnzoGUI(root, lupin_path)
    root.iconphoto(False, tk.PhotoImage(file=icon_path))
    root.mainloop()