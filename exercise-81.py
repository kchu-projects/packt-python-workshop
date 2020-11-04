class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Baby(Person):
    def speak(self):
        print("Blah blah blah")


class Adult(Person):
    def speak(self):
        print(f"Hello, my name is {self.first_name}")

jess = Baby("Jessie", "McDonald")
tom = Adult("Thomas", "Smith")

jess.speak()
tom.speak()
