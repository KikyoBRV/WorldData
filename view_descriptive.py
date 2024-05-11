import customtkinter as ctk
from model import DataModel
import pandas as pd

class DescriptiveStatisticsView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.model = DataModel()
        self.data = self.model.get_data()

        # Create a separate frame for page selection buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=10, fill="x")

        self.home_button = ctk.CTkButton(self.button_frame, text="Home",
                                         font=("Arial", 20),
                                         corner_radius=20,
                                         fg_color="#4158D0",
                                         hover_color="#C850C0",
                                         border_color="#FFCC70",
                                         command=self.controller.show_home_page)
        self.home_button.pack(side=ctk.LEFT, padx=5)

        self.stats_button = ctk.CTkButton(self.button_frame, text="Statistic Data",
                                          font=("Arial", 20),
                                          corner_radius=20,
                                          fg_color="#4158D0",
                                          hover_color="#C850C0",
                                          border_color="#FFCC70",
                                          command=self.controller.show_stats_page)
        self.stats_button.pack(side=ctk.LEFT, padx=5)

        self.explore_button = ctk.CTkButton(self.button_frame, text="Explore Country's Data",
                                            font=("Arial", 20),
                                            corner_radius=20,
                                            fg_color="#4158D0",
                                            hover_color="#C850C0",
                                            border_color="#FFCC70",
                                            command=self.controller.show_explore_page)
        self.explore_button.pack(side=ctk.LEFT, padx=5)

        self.page_name = "Descriptive Statistics"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=450, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(pady=20, padx=400, fill="both", expand=True)

        self.attribute_label = ctk.CTkLabel(self.middle_frame, text="Select Attribute:", font=("Arial", 22), text_color="#006C89")
        self.attribute_label.pack()

        self.attribute_var = ctk.StringVar()
        self.attribute_dropdown = ctk.CTkOptionMenu(self.middle_frame, variable=self.attribute_var, values=self.get_numeric_attributes(), command=self.update_descriptive_statistics)
        self.attribute_dropdown.pack(pady=10)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(pady=20, padx=200, fill="both", expand=True)

        self.data_label = ctk.CTkLabel(self.bottom_frame, font=("Arial", 25), text_color="#006C89")
        self.data_label.pack()

        self.canvas = None  # Initialize canvas attribute

        self.show_descriptive_statistics()

        # Bind window closing event to exit_application method
        self.master.protocol("WM_DELETE_WINDOW", self.exit_application)

    def get_numeric_attributes(self):
        numeric_attributes = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        return numeric_attributes

    def show_descriptive_statistics(self):
        selected_attribute = self.attribute_var.get()

        if not selected_attribute:
            self.data_label.configure(text="Please select an attribute.")
            return

        attribute_data = self.data[selected_attribute]
        mean = attribute_data.mean()
        minimum = attribute_data.min()
        maximum = attribute_data.max()
        median = attribute_data.median()
        std_dev = attribute_data.std()

        statistics = f"Descriptive statistics for {selected_attribute}:\n\n"
        statistics += f"Mean: {mean}\n"
        statistics += f"Minimum: {minimum}\n"
        statistics += f"Maximum: {maximum}\n"
        statistics += f"Median: {median}\n"
        statistics += f"Standard Deviation: {std_dev}\n"

        self.data_label.configure(text=statistics)

    def update_descriptive_statistics(self, *args):
        self.show_descriptive_statistics()

    def exit_application(self):
        # Method to exit the application
        self.controller.exit_application()
