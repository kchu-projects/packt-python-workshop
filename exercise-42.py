def get_second_element(my_list):
    try:
        return my_list[1]
    except IndexError:
        return "List was too small"


print(get_second_element([1, 2, 3]))
print(get_second_element([1]))