class Country():
    def __init__(self, name, total_cases, total_deaths) -> None:
        self.name = name
        self.total_cases = total_cases
        self.total_deaths = total_deaths

    def display(self):
        return self.name, self.total_cases, self.total_deaths
