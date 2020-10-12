x = [
    [1, 2],
    [4, 5],
    [3, 6]
]

y = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

result = []

for row_x in x:
    new_result_row = []
    new_y = zip(*y)  # pair the rows to make multiplication easier
    for row_new_y in new_y:
        number_pairs = zip(row_x, row_new_y)
        partial_result = 0
        for elem_x, elem_y in number_pairs:
            # print(elem_x, elem_y)
            partial_result += elem_x * elem_y
        new_result_row.append(partial_result)
    result.append(new_result_row)

print(result)
