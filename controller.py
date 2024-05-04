from home_view import HomeView
from explore_view import ExploreView
from stats_view import StatsView
from barchart_view import BarChartView


class AppController:
    def __init__(self, master):
        self.master = master
        self.show_home_page()

    def show_home_page(self):
        self.clear_window()
        self.home_view = HomeView(self, master=self.master)
        self.home_view.pack()

    def show_explore_page(self):
        self.clear_window()
        self.explore_view = ExploreView(self, master=self.master)
        self.explore_view.pack()

    def show_stats_page(self):
        self.clear_window()
        self.stats_view = StatsView(self, master=self.master)
        self.stats_view.pack()

    def show_barchart_page(self):
        self.clear_window()
        self.barchart_view = BarChartView(self, master=self.master)
        self.barchart_view.pack()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

