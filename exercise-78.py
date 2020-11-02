import random


class Pet:
    is_human = False
    owner = "Michael Smith"

    def __init__(self, height):
        self.height = height

    @classmethod
    def owned_by_smith_family(cls):
        return "Smith" in cls.owner

    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0, 100)
        return cls(height)


for _ in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height)
