import math
import matplotlib.pyplot as plt
import networkx as nx
import customtkinter as ctk
from model import DataModel


class NetworkGraphView(ctk.CTkFrame):
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

        self.page_name = "Network Graph"

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=450, fill="both", expand=True)

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

        self.start_country_label = ctk.CTkLabel(self.middle_frame_right, text="Start Country:", font=("Arial", 22), text_color="#006C89")
        self.start_country_label.grid(row=0, column=0, padx=10, pady=20)
        self.start_country_var = ctk.StringVar()
        self.start_country_entry = ctk.CTkComboBox(self.middle_frame_right, values= self.get_country_names(), variable=self.start_country_var)
        self.start_country_entry.grid(row=1, column=0, padx=10, pady=20)

        self.dest_country_label = ctk.CTkLabel(self.middle_frame_right, text="Destination Country:", font=("Arial", 22), text_color="#006C89")
        self.dest_country_label.grid(row=0, column=1, padx=10, pady=20)
        self.dest_country_var = ctk.StringVar()
        self.dest_country_entry = ctk.CTkComboBox(self.middle_frame_right, values= self.get_country_names(), variable=self.dest_country_var)
        self.dest_country_entry.grid(row=1, column=1, padx=10, pady=20)

        self.max_distance_label = ctk.CTkLabel(self.middle_frame_right, text="Maximum Distance (km):", font=("Arial", 22), text_color="#006C89")
        self.max_distance_label.grid(row=0, column=2, padx=10, pady=20)
        self.max_distance_entry = ctk.CTkEntry(self.middle_frame_right, placeholder_text="Example: 2500", width=150, font=("Arial", 18))
        self.max_distance_entry.grid(row=1, column=2, padx=10, pady=20)

        self.draw_button = ctk.CTkButton(self.middle_frame_right, text="Draw Graph",
                                         font=("Arial", 20),
                                         corner_radius=20,
                                         fg_color="#4158D0",
                                         hover_color="#C850C0",
                                         border_color="#FFCC70",
                                         command=self.draw_graph)
        self.draw_button.grid(row=1, column=3, padx=10, pady=20)

        self.top_frame2 = ctk.CTkFrame(self)
        self.top_frame2.pack(pady=10, padx=450, fill="both", expand=True)

        self.Describe_label = ctk.CTkLabel(self.top_frame2,
                                           text="The latitude and longitude of each country are from their capital city.",
                                           font=("Arial", 15),
                                           text_color="#006C89")
        self.Describe_label.pack(pady=0)
        self.Describe_label2 = ctk.CTkLabel(self.top_frame2,
                                           text="The output is the shortest path from the capital of the starting country, passing",
                                           font=("Arial", 15),
                                           text_color="#006C89")
        self.Describe_label2.pack(pady=0)
        self.Describe_label3 = ctk.CTkLabel(self.top_frame2,
                                           text="through each capital of the countries in the list until it reaches the capital of the destination country",
                                           font=("Arial", 15),
                                           text_color="#006C89")
        self.Describe_label3.pack(pady=0)

        self.middle_frame2 = ctk.CTkScrollableFrame(self)
        self.middle_frame2.pack(pady=20, padx=100, fill="both", expand=True)

        self.distance_label = ctk.CTkLabel(self.middle_frame2, text="", font=("Arial", 20), text_color="#006C89")
        self.distance_label.pack(pady=0)

        self.construction_label1 = ctk.CTkLabel(self.middle_frame2, text="", font=("Arial", 14), text_color="#B21F05")
        self.construction_label1.pack(pady=0)

        self.construction_label2 = ctk.CTkLabel(self.middle_frame2, text="", font=("Arial", 14), text_color="#B21F05")
        self.construction_label2.pack(pady=0)

        self.country_list_label = ctk.CTkLabel(self.middle_frame2, text="", font=("Arial", 18), text_color="#006C89")
        self.country_list_label.pack(pady=20)

        self.canvas = None

    def get_country_names(self):
        return self.data['Country'].tolist()

    def draw_graph(self):
        # Get selected start and destination countries
        start_country = self.start_country_var.get()
        dest_country = self.dest_country_var.get()

        # Get maximum distance
        max_distance = float(self.max_distance_entry.get())

        # Create a graph (adjacency list)
        G = {}

        # Add nodes with country names
        for index, row in self.data.iterrows():
            country = row['Country']
            G[country] = {}

        # Add edges with weights
        for index1, row1 in self.data.iterrows():
            for index2, row2 in self.data.iterrows():
                if index1 != index2:
                    distance = self.haversine(row1['Latitude'], row1['Longitude'], row2['Latitude'], row2['Longitude'])
                    if distance <= max_distance:
                        G[row1['Country']][row2['Country']] = distance

        # Ensure that the provided country names match exactly with the nodes in the graph
        if start_country not in G:
            print("Start country not found.")
            return
        if dest_country not in G:
            print("Destination country not found.")
            return

        # Run custom Dijkstra's algorithm
        distances, previous = self.dijkstra(G, start_country)

        # Get shortest path
        shortest_path = [dest_country]
        while previous[dest_country] is not None:
            shortest_path.insert(0, previous[dest_country])
            dest_country = previous[dest_country]

        # Calculate distance between the two countries
        shortest_distance = distances[shortest_path[-1]]

        # Print distance between the two countries
        self.distance_label.configure(text=f"Distance between {start_country} and {shortest_path[-1]} is {shortest_distance} km")
        self.construction_label1.configure(text="If the distance is 'inf', it means there's no path from the starting country to the")
        self.construction_label2.configure(text="destination country within this range of maximum distance between each country.")

        # Print list of countries in the shortest path
        self.country_list_label.configure(text="List of countries in the shortest path:\n" + "\n".join(shortest_path))

        # Draw the graph
        G_nx = nx.Graph()
        for country, neighbors in G.items():
            for neighbor, weight in neighbors.items():
                G_nx.add_edge(country, neighbor, weight=weight)

        # Highlight the shortest path
        edge_colors = ['orange' if (u, v) in shortest_path or (v, u) in shortest_path else 'gray' for u, v in G_nx.edges()]
        node_colors = ['orange' if node in shortest_path else 'skyblue' for node in G_nx.nodes()]
        pos = nx.spring_layout(G_nx, seed=42)  # Positions for all nodes
        nx.draw(G_nx, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10, font_weight='bold', edge_color=edge_colors, width=2)

        # Add edge labels (weights)
        edge_labels = {(u, v): f"{G_nx[u][v]['weight']:.2f}" for u, v in G_nx.edges()}
        nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels, font_color='red')

        # Show the graph
        plt.show()

    # Haversine formula to calculate distance between two points on Earth's surface
    def haversine(self, lat1, lon1, lat2, lon2):
        # Replace """ with "" if present and remove leading/trailing quotes
        lat1 = lat1.replace('"', '').strip() if isinstance(lat1,
                                                             str) else lat1
        lon1 = lon1.replace('"', '').strip() if isinstance(lon1,
                                                             str) else lon1
        lat2 = lat2.replace('"', '').strip() if isinstance(lat2,
                                                             str) else lat2
        lon2 = lon2.replace('"', '').strip() if isinstance(lon2,
                                                             str) else lon2

        if lat1 == "" or lon1 == "" or lat2 == "" or lon2 == "":
            return float(
                'inf')  # Return infinity if any of the coordinates is missing

        lat1 = float(lat1)
        lon1 = float(lon1)
        lat2 = float(lat2)
        lon2 = float(lon2)

        R = 6371  # Radius of the Earth in kilometers
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(
            lat2_rad) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    # Dijkstra's algorithm
    def dijkstra(self, graph, start):
        visited = {node: False for node in graph} # set all vertices to unexplored
        distances = {node: float('inf') for node in graph} # set distance for every node as inf
        previous = {node: None for node in graph} # set previous node to be none
        distances[start] = 0 # set distance of start city = 0

        while True:
            # current node always select the node that has minimum distance first.
            current_node = min((node for node in graph if not visited[node]), key=distances.get)
            visited[current_node] = True # set that the current node got visited

            for neighbor, weight in graph[current_node].items():
                if not visited[neighbor]:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        #update distance of neighbor node if new distance is smaller than it own
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_node

            if all(visited[node] for node in graph): # if all node got visited
                break

        return distances, previous
