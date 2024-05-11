import customtkinter as ctk
from model import DataModel

class ExploreView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller
        self.model = DataModel()
        self.data = self.model.get_data()

        # Create a separate frame for page selection buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=10, fill="x")

        self.explore_button = ctk.CTkButton(self.button_frame, text="Home",
                                            font=("Arial", 20),
                                            corner_radius=20,
                                            fg_color="#4158D0",
                                            hover_color="#C850C0",
                                            border_color="#FFCC70",
                                            command=self.controller.show_home_page)
        self.explore_button.pack(side=ctk.LEFT, padx=5)

        self.stats_button = ctk.CTkButton(self.button_frame, text="Statistic Data",
                                          font=("Arial", 20),
                                          corner_radius=20,
                                          fg_color="#4158D0",
                                          hover_color="#C850C0",
                                          border_color="#FFCC70",
                                          command=self.controller.show_stats_page)
        self.stats_button.pack(side=ctk.LEFT, padx=5)

        self.page_name = "Explore Country's Data"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.big_middle_frame1 = ctk.CTkFrame(self)
        self.big_middle_frame1.pack(pady=20, padx=10, fill="both", expand=True)

        self.middle_frame_left = ctk.CTkScrollableFrame(self.big_middle_frame1)
        self.middle_frame_left.pack(side="left", pady=20, padx=5, fill="both", expand=True)

        self.country_list = ctk.CTkLabel(self.middle_frame_left, text="", font=("Arial", 18), text_color="#006C89")
        self.country_list.pack(pady=20)
        self.country_list.configure(text="List of countries:\n" + "\n".join(self.get_country_names()))

        self.middle_frame_right = ctk.CTkFrame(self.big_middle_frame1)
        self.middle_frame_right.pack(side="right", pady=20, padx=5, fill="both", expand=True)

        self.start_country_label = ctk.CTkLabel(self.middle_frame_right, text="Select Country:", font=("Arial", 22), text_color="#006C89")
        self.start_country_label.grid(row=0, column=0, padx=10, pady=20)
        self.start_country_var = ctk.StringVar()
        self.start_country_entry = ctk.CTkComboBox(self.middle_frame_right, values= self.get_country_names(), variable=self.start_country_var)
        self.start_country_entry.grid(row=1, column=0, padx=10, pady=20)

        self.show_data_button = ctk.CTkButton(self.middle_frame_right, text="Show Data", command=self.show_country_data)
        self.show_data_button.grid(row=2, column=0, padx=10, pady=20)

        self.bottom_frame = ctk.CTkScrollableFrame(self)
        self.bottom_frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Create a label to display the country data
        self.country_data_label = ctk.CTkLabel(self.bottom_frame, text="", font=("Arial", 14), text_color="#006C89", wraplength=400)
        self.country_data_label.pack(pady=10)

        # Bind the combobox selection event to the update method
        self.start_country_entry.bind("<<ComboboxSelected>>", self.update)

    def get_country_names(self):
        return self.data['Country'].tolist()

    def show_country_data(self):
        selected_country = self.start_country_var.get()
        if selected_country:
            country_data = self.data[self.data['Country'] == selected_country]
            country_info = ""
            for col in country_data.columns:
                country_info += f"{col}: {country_data[col].iloc[0]}\n"
            self.country_data_label.configure(text=country_info)
        else:
            self.country_data_label.configure(text="")

    def update(self, event=None):
        self.show_country_data()
