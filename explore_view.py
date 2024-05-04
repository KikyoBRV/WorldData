import tkinter as tk

class ExploreView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        self.page_name = "Explore Country's Data"

        self.top_frame = tk.Frame(self)
        self.top_frame.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.label = tk.Label(self.bottom_frame, text=self.page_name)
        self.label.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.home_button = tk.Button(self.top_frame, text="Home", command=self.controller.show_home_page)
        self.home_button.pack(side=tk.LEFT)

        self.stats_button = tk.Button(self.top_frame, text="Statistic Data", command=self.controller.show_stats_page)
        self.stats_button.pack(side=tk.LEFT)
