import csv
import matplotlib.pyplot as plt

lines = []
with open("activity-13/titanic_train.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        lines.append(line)

data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    passengers.append({header: item for header, item in zip(headers, d)})

survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]

fig = plt.figure(figsize=(8, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title("Survived")
ax1.pie([survived.count("0"), survived.count("1")], labels=["0", "1"], autopct="%1.1f%%", colors=["lightblue", "lightgreen", "yellow"])

ax2.set_title("surviving passengers count by gender")
ax2.bar(["female", "male"], [gender_survived.count("female"), gender_survived.count("male")])

plt.show()
