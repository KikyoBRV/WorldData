import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from model import DataModel

class CorrelationView(ctk.CTkFrame):
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

        self.page_name = "Correlation"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=450, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(pady=20, padx=200, fill="both", expand=True)

        self.attribute_label1 = ctk.CTkLabel(self.middle_frame, text="Select Attribute 1:", font=("Arial", 22), text_color="#006C89")
        self.attribute_label1.pack(padx=20, side="left")

        self.attribute_var1 = ctk.StringVar()
        self.attribute_dropdown1 = ctk.CTkOptionMenu(self.middle_frame, variable=self.attribute_var1, values=self.get_numeric_attributes(), command=self.draw_correlation_graph)
        self.attribute_dropdown1.pack(pady=10, side="left")

        self.attribute_label2 = ctk.CTkLabel(self.middle_frame, text="Select Attribute 2:", font=("Arial", 22), text_color="#006C89")
        self.attribute_label2.pack(padx=20, side="left")

        self.attribute_var2 = ctk.StringVar()
        self.attribute_dropdown2 = ctk.CTkOptionMenu(self.middle_frame, variable=self.attribute_var2, values=self.get_numeric_attributes(), command=self.draw_correlation_graph)
        self.attribute_dropdown2.pack(pady=10, side="left")

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.canvas = None  # Initialize canvas attribute

    def get_numeric_attributes(self):
        numeric_attributes = [col for col in self.data.columns if pd.api.types.is_numeric_dtype(self.data[col])]
        return numeric_attributes

    def draw_correlation_graph(self, *args):
        attribute1 = self.attribute_var1.get()
        attribute2 = self.attribute_var2.get()

        if not attribute1 or not attribute2:
            return

        # Prepare data for correlation plot
        grouped = self.data.groupby('Region')
        regions = []
        colors = []
        for name, group in grouped:
            regions.extend([name] * len(group))
            colors.extend([self.get_region_color(name)] * len(group))

        x = self.data[attribute1]
        y = self.data[attribute2]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(x, y, c=colors, alpha=0.6)
        ax.set_xlabel(attribute1.capitalize())
        ax.set_ylabel(attribute2.capitalize())
        ax.set_title(f'Correlation between {attribute1.capitalize()} and {attribute2.capitalize()}')

        # Create legend with region names
        handles = [plt.Line2D([], [], marker="o", markersize=8, linestyle="",
                              color=self.get_region_color(region), label=region) for region in grouped.groups.keys()]
        ax.legend(handles=handles, title='Region', title_fontsize='15', fontsize='12')

        # Destroy existing canvas if it exists
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.bottom_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        # Close the figure explicitly to avoid the warning
        plt.close(fig)

    def get_region_color(self, region):
        region_colors = {
            'Asia': 'blue',
            'Europe': 'green',
            'Africa': 'red',
            'Northern America': 'orange',
            'Latin America and the Caribbean': 'pink',
            'Oceania': 'purple'
        }
        return region_colors.get(region, 'black')

    def exit_application(self):
        # Method to exit the application
        self.controller.exit_application()
