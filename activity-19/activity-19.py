students = ["Vivian", "Racheal", "Tom", "Adrian"]
scores_list = [70, 82, 80, 79]

scores = {student:score for student, score in zip(students, scores_list)}
print(scores)
