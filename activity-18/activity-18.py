players = ["Magnus Carlsen", "Fabiano Caruana", "Yifan Hou", "Wenjun Ju"]

matches = [f"{x} vs {y}" for x in players for y in players if x != y]

print(matches)
