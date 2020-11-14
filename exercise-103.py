from collections import defaultdict


john = {"first_name": "John", "surname": "Cleese"}
safe_john = defaultdict(str, john)

print(safe_john["middle_name"])

courses = defaultdict(lambda: "No!")
courses["Java"] = "This is Java"

print(courses["Python"])
print(courses["Java"])
