s5 = {1,2,3,4}
s6 = {3,4,5,6}

# union
print(s5 | s6)
print(s5.union(s6))

# intersection
print(s5 & s6)
print(s5.intersection(s6))

# difference
print(s5 - s6)
print(s5.difference(s6))

# subset
print(s5 <= s6)
print(s5.issubset(s6))
s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))

# proper subset
print(s7 < s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 < s9)

# superset and proper superset
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)
