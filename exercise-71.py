class Pet:
    """
    A class to capture useful information regarding my pets, just in case
    I lose track of them.
    """
    is_human = False
    owner = "Michael Smith"


chubbles = Pet()
print(chubbles.is_human)
print(chubbles.owner)
print(chubbles.__doc__)
