orders = {'apple':5, 'orange':3, 'banana':2}
print(orders.values())
print(list(orders.values()))

print(list(orders.keys()))

for tuple in list(orders.items()):
    print(tuple)
