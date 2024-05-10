import customtkinter as ctk

class ExploreView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        # Create a separate frame for page selection buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=10, fill="x")

        self.explore_button = ctk.CTkButton(self.button_frame, text="Home", command=self.controller.show_home_page)
        self.explore_button.pack(side=ctk.LEFT, padx=5)

        self.stats_button = ctk.CTkButton(self.button_frame, text="Statistic Data", command=self.controller.show_stats_page)
        self.stats_button.pack(side=ctk.LEFT, padx=5)

        self.page_name = "Explore Country's Data"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)
