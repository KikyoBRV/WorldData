import tkinter as tk

class HomeView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        self.page_name = "Home"

        self.top_frame = tk.Frame(master)  # Use master instead of self
        self.top_frame.pack()

        # Create a menu bar
        self.menu_bar = tk.Menu(master)  # Use master instead of self

        # Create Page menu
        self.page_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.page_menu.add_command(label="Statistic Data", command=self.controller.show_stats_page)
        self.page_menu.add_command(label="Explore Country Data", command=self.controller.show_explore_page)

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label="Page Selection", menu=self.page_menu)

        # Configure the master (root) window to use the menu bar
        master.config(menu=self.menu_bar)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.label = tk.Label(self.bottom_frame, text=self.page_name)
        self.label.pack()
