import customtkinter as ctk

class StatsView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        # Create a separate frame for page selection buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=10, fill="x")

        self.home_button = ctk.CTkButton(self.button_frame, text="Home",
                                         corner_radius=20,
                                         fg_color="#4158D0",
                                         hover_color="#C850C0",
                                         border_color="#FFCC70",
                                         command=self.controller.show_home_page)
        self.home_button.pack(side=ctk.LEFT, padx=5)

        self.explore_button = ctk.CTkButton(self.button_frame, text="Explore Country Data",
                                            corner_radius=20,
                                            fg_color="#4158D0",
                                            hover_color="#C850C0",
                                            border_color="#FFCC70",
                                            command=self.controller.show_explore_page)
        self.explore_button.pack(side=ctk.LEFT, padx=5)

        self.page_name = "Statistic Data"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.button1 = ctk.CTkButton(self.bottom_frame, text="Bar Chart", command=self.controller.show_barchart_page, font=("Arial", 12))
        self.button1.grid(row=0, column=0, padx=5, pady=5)

        self.button2 = ctk.CTkButton(self.bottom_frame, text="Button 2", command=self.controller.show_explore_page, font=("Arial", 12))
        self.button2.grid(row=0, column=1, padx=5, pady=5)

        self.button3 = ctk.CTkButton(self.bottom_frame, text="Button 3", command=self.controller.show_stats_page, font=("Arial", 12))
        self.button3.grid(row=0, column=2, padx=5, pady=5)

        self.button4 = ctk.CTkButton(self.bottom_frame, text="Button 4", command=self.controller.show_home_page, font=("Arial", 12))
        self.button4.grid(row=1, column=0, padx=5, pady=5)

        self.button5 = ctk.CTkButton(self.bottom_frame, text="Button 5", command=self.controller.show_explore_page, font=("Arial", 12))
        self.button5.grid(row=1, column=1, padx=5, pady=5)

        self.button6 = ctk.CTkButton(self.bottom_frame, text="Button 6", command=self.controller.show_stats_page, font=("Arial", 12))
        self.button6.grid(row=1, column=2, padx=5, pady=5)