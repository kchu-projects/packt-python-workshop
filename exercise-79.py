class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last


customer = Person("Mary", "Lou")
print(customer.full_name)
customer.full_name = "Mary Schmidt"
print(customer.last_name)
