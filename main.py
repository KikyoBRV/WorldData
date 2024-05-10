import customtkinter as ctk
from controller import AppController

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("WorldData")
    controller = AppController(root)
    root.mainloop()
