# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
t_height=0 #This is the counter of the sum of all heights inside the list student_heights
n_students=0 #This is the counter of the number of heights, know as len function
for height in student_heights:
  t_height+=height #As while the loop is rolling, this will add the N Height to the counter
  n_students+=1
print(t_height//n_students) 
    