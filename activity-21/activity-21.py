import re


customers = ["Xander Harris", "Jennifer Smith", "Timothy Jones", "Amy Alexandrescu", "Peter Price", "Weifung Xu"]

pattern = "[Xx]"
new_list = [c for c in customers if re.search(pattern, c) is not None]
print(new_list)
