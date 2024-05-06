import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import DataModel
import pandas as pd

class BarChartView(tk.Frame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.model = DataModel()
        self.data = self.model.get_data()

        self.page_name = "Bar Chart Page"

        self.top_frame = tk.Frame(self)
        self.top_frame.pack()

        self.label = tk.Label(self.top_frame, text=self.page_name, font=("Arial", 16))
        self.label.pack()

        self.attribute_label = tk.Label(self.top_frame, text="Select Attribute:")
        self.attribute_label.pack()

        self.attribute_var = tk.StringVar()
        self.attribute_dropdown = tk.OptionMenu(self.top_frame, self.attribute_var, *self.get_numeric_attributes(), command=self.update_bar_chart)
        self.attribute_dropdown.pack()

        self.back_button = tk.Button(self.top_frame, text="Back to Statistic Page", command=self.controller.show_stats_page)
        self.back_button.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.canvas = None  # Initialize canvas attribute

        self.draw_bar_chart()

        # Bind window closing event to exit_application method
        master.protocol("WM_DELETE_WINDOW", self.exit_application)

    def get_numeric_attributes(self):
        numeric_attributes = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        return numeric_attributes

    def draw_bar_chart(self):
        selected_attribute = self.attribute_var.get()

        if not selected_attribute:
            selected_attribute = self.get_numeric_attributes()[0]

        x = self.data['Region']
        y = self.data[selected_attribute]

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
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,
                                         expand=True)

    def update_bar_chart(self, *args):
        self.draw_bar_chart()

    def exit_application(self):
        # Method to exit the application
        self.controller.exit_application()
