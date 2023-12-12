# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total = 0
num_Stu = 0
average = 0
for each in student_heights:
    num_Stu += 1
    total += each
average = round(total / num_Stu)
print(f"total height = {total}\nnumber of students = {num_Stu}\naverage height = {average}")
