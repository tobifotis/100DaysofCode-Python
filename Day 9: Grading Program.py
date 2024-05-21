student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for i in student_scores:
  if student_scores[i] >= 91:
    student_scores[i] = "Outstanding"
  elif student_scores[i] >= 81 and student_scores[i] <= 90:
    student_scores[i] = "Exceeds Expectations"
  elif student_scores[i] >= 71 and student_scores[i] <= 80:
    student_scores[i] = "Acceptable"
  else:
    student_scores[i] = "Fail"
  student_grades[i] = student_scores[i]
  # print(student_scores[i])

print(student_grades)