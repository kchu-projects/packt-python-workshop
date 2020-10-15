employees = [
    {
        "name": "John Mckee",
        "age": 38,
        "department": "Sales"
    },
    {
        "name": "Lisa Crawford",
        "age": 29,
        "department": "Marketing"
    },
    {
        "name": "Sujan Patel",
        "age": 33,
        "department": "HR"
    }
]

print(employees)

for employee in employees:
    for key, value in employee.items():
        print(f"{key.capitalize()}: {value}")
    print("--------------------")

for employee in employees:
    if employee["name"] == "Sujan Patel":
        for key, value in employee.items():
            print(f"{key.capitalize()}: {value}")
        print("--------------------")