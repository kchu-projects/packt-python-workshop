my_list = [5, 8, 1, 3, 2]

search_for = 8

result = -1

for i, elem in enumerate(my_list):
    if elem == search_for:
        result = i
        break

print(result)
