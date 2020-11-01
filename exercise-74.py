class Pet:
    is_human = False
    owner = "Michael Smith"

    def __init__(self, height):
        self.height = height

    def is_tall(self):
        return self.height >= 50

bowser = Pet(40)
print(bowser.is_tall())

bowser.height = 60
print(bowser.is_tall())
