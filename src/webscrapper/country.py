class Country():
    def __init__(self, name, totalcases, deaths) -> None:
        self.name = name
        self.totalcases = totalcases
        self.deaths = deaths

    def display(self):
        return self.name, self.totalcases, self.deaths
