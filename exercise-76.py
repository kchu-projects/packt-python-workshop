class Country:
    def __init__(self, name="Unspecified", population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self):
        label = self.name
        if self.population is not None:
            label = f"{label}, population: {self.population}"
        if self.size_kmsq is not None:
            label = f"{label}, size_kmsq: {self.size_kmsq}"
        return label

chad = Country(name="Chad", population=100)
print(chad)
