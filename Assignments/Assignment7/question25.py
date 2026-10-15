# 25. Given a nested dictionary of students and their subject marks, calculate
#     each student's total marks and find the topper.
student= {
    "kashish":{"hindi":96,"english":78,"maths":98},
    "keshav":{"hindi":66,"english":88,"maths":98},
    "kartavya":{"hindi":66,"english":58,"maths":68},
    "raghav":{"hindi":46,"english":48,"maths":88}

}
max = 0
name=""
for i in student.keys():
    sum=0
    for j in student[i]:
        sum+=student[i][j]
    if sum > max:
        max = sum
        name = i
print(f"The name of the student who secured the maximum marks is : {name} and marks is {max}")
