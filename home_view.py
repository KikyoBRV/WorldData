import tkinter as tk


class HomeView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        self.page_name = "Home"

        self.top_frame = tk.Frame(self)
        self.top_frame.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.label = tk.Label(self.bottom_frame, text=self.page_name)
        self.label.pack()

        self.explore_button = tk.Button(self.top_frame, text="Explore Country Data", command=self.controller.show_explore_page)
        self.explore_button.pack(side=tk.LEFT)

        self.stats_button = tk.Button(self.top_frame, text="Statistic Data", command=self.controller.show_stats_page)
        self.stats_button.pack(side=tk.LEFT)
