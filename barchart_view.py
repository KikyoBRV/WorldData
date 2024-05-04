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

        self.draw_bar_chart()

    def get_numeric_attributes(self):
        # Get a list of headers containing numerical data
        numeric_attributes = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        return numeric_attributes

    def draw_bar_chart(self):
        # Get the selected attribute from the dropdown menu
        selected_attribute = self.attribute_var.get()

        # If no attribute is selected, default to the first numeric attribute
        if not selected_attribute:
            selected_attribute = self.get_numeric_attributes()[0]

        x = self.data['Region']
        y = self.data[selected_attribute]

        # Create a new figure
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot the bar chart
        ax.bar(x, y, width=0.8)

        # Set x and y axis labels
        ax.set_xlabel('Region')
        ax.set_ylabel(selected_attribute.capitalize())  # Capitalize attribute name

        # Set the title for the plot
        ax.set_title(f'{selected_attribute.capitalize()} of each Region')

        # Rotate x-axis labels by 0 degree
        plt.xticks(rotation=0, ha='center', fontsize=8)

        # Convert matplotlib figure to tkinter canvas
        self.canvas = FigureCanvasTkAgg(fig, master=self.bottom_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_bar_chart(self, *args):
        # Redraw the bar chart when a new attribute is selected
        self.canvas.get_tk_widget().destroy()  # Remove previous chart
        self.draw_bar_chart()
