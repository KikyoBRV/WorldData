from view_home import HomeView
from view_explore import ExploreView
from view_stats import StatsView
from view_barchart import BarChartView
from view_piechart import PieChartView
from view_correlation import CorrelationView
from view_distribution import DistributionView
import webbrowser


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

    def show_piechart_page(self):
        self.clear_window()
        self.piechart_view = PieChartView(self, master=self.master)
        self.piechart_view.pack()

    def show_correlation_page(self):
        self.clear_window()
        self.correlation_view = CorrelationView(self, master=self.master)
        self.correlation_view.pack()

    def show_distribution_page(self):
        self.clear_window()
        self.distribution_view = DistributionView(self, master=self.master)
        self.distribution_view.pack()


    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def open_link(self, link):
        webbrowser.open(link)

    def exit_application(self):
        self.master.quit()
