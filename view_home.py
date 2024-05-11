import customtkinter as ctk
from PIL import Image, ImageTk


class HomeView(ctk.CTkFrame):
    def __init__(self, controller, master=None):
        super().__init__(master)
        self.controller = controller

        # Create a separate frame for page selection buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=10, fill="x")

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

        self.page_name = "Home"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=10, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.top_frame, text=self.page_name, font=("Arial", 50), text_color="#006C89")
        self.label.pack(pady=0)

        self.middle_frame = ctk.CTkFrame(self)
        self.middle_frame.pack(pady=10, padx=60, fill="both", expand=True)

        # Load the image
        DescriptionImage_path = "Picture_Used/WordData_Description1.png"
        self.Description_Image = Image.open(DescriptionImage_path)

        GitHubImage_path = "Picture_Used/GitHub_Icon.png"
        self.GitHub_image = Image.open(GitHubImage_path)

        YouTubeImage_path = "Picture_Used/Youtube_Icon.png"
        self.YouTube_image = Image.open(YouTubeImage_path)

        # Convert the image to PhotoImage format
        self.Description_photo = ImageTk.PhotoImage(self.Description_Image)

        # Create a Canvas widget to display the image
        self.canvas = ctk.CTkCanvas(self.middle_frame, width=self.Description_Image.width, height=self.Description_Image.height)
        self.canvas.pack()

        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.Description_photo)

        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(pady=10, padx=20)

        github_link = "https://github.com/KikyoBRV/WorldData"
        youtube_link = "https://youtu.be/dQw4w9WgXcQ?si=rG0YOF-toERYo2aV"
        self.github_button = ctk.CTkButton(self.info_frame,
                                           text="Click here to visit our GitHub repository",
                                           image=ctk.CTkImage((self.GitHub_image)),
                                           font=("Arial", 15),
                                           corner_radius=20,
                                           fg_color="#4158D0",
                                           hover_color="#C850C0",
                                           border_color="#FFCC70",
                                           command=lambda: self.controller.open_link(github_link))
        self.github_button.pack(padx=10, pady=5, side="left")

        self.youtube_button = ctk.CTkButton(self.info_frame,
                                           text="Click here to watch app demonstration",
                                           image=ctk.CTkImage((self.YouTube_image)),
                                           font=("Arial", 15),
                                           corner_radius=20,
                                           fg_color="#4158D0",
                                           hover_color="#C850C0",
                                           border_color="#FFCC70",
                                           command=lambda: self.controller.open_link(youtube_link))
        self.youtube_button.pack(padx=10, pady=5, side="right")
