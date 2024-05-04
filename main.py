import tkinter as tk
from controller import AppController

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVC App")
    controller = AppController(root)
    root.mainloop()
