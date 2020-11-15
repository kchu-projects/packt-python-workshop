import itertools


players = ["White", "Black"]
turns = itertools.cycle(players)

countdown = itertools.count(10, -1)
print([turn for turn in itertools.takewhile(lambda x: next(countdown) > 0, turns)])
