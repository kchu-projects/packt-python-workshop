class Country:
    def __init__(self, name="Unspecified", population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def size_miles_sq(self, conversion_rate=0.621371):
        return self.size_kmsq * conversion_rate ** 2
    
algeria = Country(name="Algeria", size_kmsq=2.382e6)
print(algeria.size_miles_sq())
print(algeria.size_miles_sq(conversion_rate=0.6))
