import customtkinter as ctk
from PIL import Image, ImageTk

class StatsView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

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

        self.explore_button = ctk.CTkButton(self.button_frame, text="Explore Country Data",
                                            font=("Arial", 20),
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

        # Load the image
        pic1_path = "Picture_Used/1.png"
        self.Pic1_Image = Image.open(pic1_path)
        # Convert the image to PhotoImage format
        self.Pic1_photo = ImageTk.PhotoImage(self.Pic1_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic1_photo)

        self.button1 = ctk.CTkButton(self.bottom_frame, text="Bar Chart",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_barchart_page)
        self.button1.grid(row=1, column=0, padx=5, pady=5)

        # Load the image
        pic2_path = "Picture_Used/2.png"
        self.Pic2_Image = Image.open(pic2_path)
        # Convert the image to PhotoImage format
        self.Pic2_photo = ImageTk.PhotoImage(self.Pic2_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=0, column=1, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic2_photo)

        self.button2 = ctk.CTkButton(self.bottom_frame, text="Pie Chart",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_explore_page)
        self.button2.grid(row=1, column=1, padx=20, pady=20)

        # Load the image
        pic3_path = "Picture_Used/3.png"
        self.Pic3_Image = Image.open(pic3_path)
        # Convert the image to PhotoImage format
        self.Pic3_photo = ImageTk.PhotoImage(self.Pic3_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=0, column=2, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic3_photo)

        self.button3 = ctk.CTkButton(self.bottom_frame, text="Correlation",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_stats_page)
        self.button3.grid(row=1, column=2, padx=20, pady=20)

        # Load the image
        pic4_path = "Picture_Used/4.png"
        self.Pic4_Image = Image.open(pic4_path)
        # Convert the image to PhotoImage format
        self.Pic4_photo = ImageTk.PhotoImage(self.Pic4_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=2, column=0, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic4_photo)

        self.button4 = ctk.CTkButton(self.bottom_frame, text="Network Graph",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_home_page)
        self.button4.grid(row=3, column=0, padx=20, pady=20)

        # Load the image
        pic5_path = "Picture_Used/5.png"
        self.Pic5_Image = Image.open(pic5_path)
        # Convert the image to PhotoImage format
        self.Pic5_photo = ImageTk.PhotoImage(self.Pic5_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=2, column=1, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic5_photo)

        self.button5 = ctk.CTkButton(self.bottom_frame, text="Descriptive",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_explore_page)
        self.button5.grid(row=3, column=1, padx=20, pady=20)

        # Load the image
        pic6_path = "Picture_Used/6.png"
        self.Pic6_Image = Image.open(pic6_path)
        # Convert the image to PhotoImage format
        self.Pic6_photo = ImageTk.PhotoImage(self.Pic6_Image)
        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.bottom_frame, width=400, height=250)
        self.canvas.grid(row=2, column=2, padx=20, pady=20)
        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Pic6_photo)

        self.button6 = ctk.CTkButton(self.bottom_frame, text="Distribution",
                                     font=("Arial", 30),
                                     corner_radius=20,
                                     fg_color="#4158D0",
                                     hover_color="#C850C0",
                                     border_color="#FFCC70",
                                     command=self.controller.show_stats_page)
        self.button6.grid(row=3, column=2, padx=20, pady=20)