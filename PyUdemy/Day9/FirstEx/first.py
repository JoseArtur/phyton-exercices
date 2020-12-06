student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

print(student_scores["Harry"])
for name,grade in student_scores.items():
    if grade<=70:
        student_grades[name]="Fail"
    elif grade>70 and grade<=80:
        student_grades[name]="Acceptable"
    elif grade>80 and grade<=90:
        student_grades[name]="Exceeds Expectations"
    elif grade>90 and grade<=100:
        student_scores[name]="Outstading"
# 🚨 Don't change the code below 👇
print(student_grades)





