import tkinter as tk


class StatsView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        self.page_name = "Statistic Data"

        self.top_frame = tk.Frame(self)
        self.top_frame.pack()

        self.label = tk.Label(self.top_frame, text=self.page_name)
        self.label.pack()

        self.home_button = tk.Button(self.top_frame, text="Home", command=self.controller.show_home_page, font=("Arial", 12))
        self.home_button.pack(side=tk.LEFT)

        self.explore_button = tk.Button(self.top_frame, text="Explore Country Data", command=self.controller.show_explore_page, font=("Arial", 12))
        self.explore_button.pack(side=tk.LEFT)

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
