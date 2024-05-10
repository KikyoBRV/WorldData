import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import DataModel
import pandas as pd

class BarChartView(ctk.CTkFrame):
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

        self.explore_button = ctk.CTkButton(self.button_frame, text="Explore Country Data",
                                            font=("Arial", 20),
                                            corner_radius=20,
                                            fg_color="#4158D0",
                                            hover_color="#C850C0",
                                            border_color="#FFCC70",
                                            command=self.controller.show_explore_page)
        self.explore_button.pack(side=ctk.LEFT, padx=5)

        self.page_name = "Bar Chart"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=450, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(pady=20, padx=400, fill="both", expand=True)

        self.attribute_label = ctk.CTkLabel(self.middle_frame, text="Select Attribute:", font=("Arial", 22), text_color="#006C89")
        self.attribute_label.pack()

        self.attribute_var = ctk.StringVar()
        self.attribute_dropdown = ctk.CTkOptionMenu(self.middle_frame, variable=self.attribute_var, values=self.get_numeric_attributes(), command=self.update_bar_chart)
        self.attribute_dropdown.pack(pady=10)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.canvas = None  # Initialize canvas attribute

        self.draw_bar_chart()

        # Bind window closing event to exit_application method
        self.master.protocol("WM_DELETE_WINDOW", self.exit_application)

    def get_numeric_attributes(self):
        numeric_attributes = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        return numeric_attributes

    def draw_bar_chart(self):
        selected_attribute = self.attribute_var.get()

        if not selected_attribute:
            selected_attribute = self.get_numeric_attributes()[0]

        # Sum values in the selected_attribute
        region_list = []
        for i in self.data['Region']:
            if i not in region_list:
                region_list.append(i)
        region_dict = dict.fromkeys(region_list, 0)
        for j in range(self.data.shape[0]):
            if pd.notna(self.data.loc[j, selected_attribute]):
                Jvalue = str(self.data.loc[j, selected_attribute]).replace(",", "")
                region_dict[self.data.loc[j, 'Region']] += float(Jvalue)
            else:
                region_dict[self.data.loc[j, 'Region']] += 0

        x = list(region_dict.keys())
        y = list(region_dict.values())

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(x, y, width=0.8)
        ax.set_xlabel('Region')
        ax.set_ylabel(selected_attribute.capitalize())
        ax.set_title(f'{selected_attribute.capitalize()} of each Region')
        plt.xticks(rotation=8, ha='center', fontsize=8)

        # Destroy existing canvas if it exists
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.bottom_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Close the figure explicitly to avoid the warning
        plt.close(fig)

    def update_bar_chart(self, *args):
        self.draw_bar_chart()

    def exit_application(self):
        # Method to exit the application
        self.controller.exit_application()