# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest = 0
for each in student_scores:
    if each >= highest:
        highest = each
print(f"The highest score in the class is: {highest}")