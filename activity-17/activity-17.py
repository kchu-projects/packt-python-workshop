import functools


class Hero:
    DEFAULT_NAME = "Superman"
    def __init__(self):
        self.name = Hero.DEFAULT_NAME

    def rename(self, new_name):
        self.name = new_name

    reset_name = functools.partialmethod(rename, DEFAULT_NAME)

    def __repr__(self):
        return f"Hero({self.name!r})"


if __name__ == "__main__":
    # help(functools.partialmethod)
    hero = Hero()
    assert hero.name == "Superman"
    hero.rename("Batman")
    assert hero.name == "Batman"
    hero.reset_name()
    assert hero.name == "Superman"
