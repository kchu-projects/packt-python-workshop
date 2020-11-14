cubes = []
for x in [1, 2, 3, 4, 5]:
    cubes.append(x ** 3)
print(cubes)

cubes = [x ** 3 for x in [1, 2, 3, 4, 5]]
print(cubes)

cubes = [x ** 3 for x in range(1, 6)]
print(cubes)

names = ["Graham Chapman", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
print([name.upper() for name in names if name.startswith("T")])
