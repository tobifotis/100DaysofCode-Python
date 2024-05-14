# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Your code here
sum = 0
for each_student in student_heights:
  sum += each_student

print(f"total height = {sum}")

num_students = 0
for students in student_heights:
  num_students += 1

print(f"number of students = {num_students}")

avg_height = round(sum / num_students)
print(f"average height = {avg_height}")
