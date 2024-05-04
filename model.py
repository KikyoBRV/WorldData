import pandas as pd


class DataModel:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        try:
            self.data = pd.read_csv("world-data-2023.csv")
        except FileNotFoundError:
            print("Error: File 'world-data-2023.csv' not found.")

    def get_data(self):
        return self.data
