import tkinter as tk

class StatsView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        self.page_name = "Statistic Data"

        self.top_frame = tk.Frame(master)  # Use master instead of self
        self.top_frame.pack()

        # Create a menu bar
        self.menu_bar = tk.Menu(master)  # Use master instead of self

        # Create Page menu
        self.home_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.home_menu.add_command(label="Home", command=self.controller.show_home_page)
        self.home_menu.add_command(label="Explore Country Data", command=self.controller.show_explore_page)

        # Add Home menu to the menu bar
        self.menu_bar.add_cascade(label="Page", menu=self.home_menu)

        # Configure the master (root) window to use the menu bar
        master.config(menu=self.menu_bar)

        self.label = tk.Label(self.top_frame, text=self.page_name)
        self.label.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.button1 = tk.Button(self.bottom_frame, text="Bar Chart", command=self.controller.show_barchart_page, font=("Arial", 12))
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        self.button2 = tk.Button(self.bottom_frame, text="Button 2", command=self.controller.show_explore_page, font=("Arial", 12))
        self.button2.grid(row=0, column=1, padx=5, pady=5)

        self.button3 = tk.Button(self.bottom_frame, text="Button 3", command=self.controller.show_stats_page, font=("Arial", 12))
        self.button3.grid(row=0, column=2, padx=5, pady=5)

        self.button4 = tk.Button(self.bottom_frame, text="Button 4", command=self.controller.show_home_page, font=("Arial", 12))
        self.button4.grid(row=1, column=0, padx=5, pady=5)

        self.button5 = tk.Button(self.bottom_frame, text="Button 5", command=self.controller.show_explore_page, font=("Arial", 12))
        self.button5.grid(row=1, column=1, padx=5, pady=5)

        self.button6 = tk.Button(self.bottom_frame, text="Button 6", command=self.controller.show_stats_page, font=("Arial", 12))
        self.button6.grid(row=1, column=2, padx=5, pady=5)
