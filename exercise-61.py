def avg(marks):
    assert len(marks) != 0, "Length of marks list cannot be 0."
    return round(sum(marks)/len(marks), 2)


sem1_marks = [62, 65, 75]
print(f"Average marks for semester 1: {avg(sem1_marks)}")

# sem2_marks = []
# print(f"Average marks for semester 1: {avg(sem2_marks)}")
