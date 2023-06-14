# the goal of this exercise is to use loops to calculate the average height or weight of a group of people
# for this exercise we are not using the built-in Python functions


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_amount = 0
for student in student_heights:
    total_amount += student
    
#print(total_amount)    
total_split = 0
for student in student_heights:
    total_split += 1
    
print(round(total_amount/total_split)) 

