# '''
# Student Marks Analyzer

# Create a program to store marks of 10 students.

# Requirements:

# Store student names in a tuple.
# Store marks in a list.
# Create a dictionary with name as key and marks as value.
# Create a set of students scoring more than 80.
# Display:
# Highest scorer
# Lowest scorer
# Average marks
# Students scoring above average
# '''

names = ('harsh','sneh','vighnesh','sujal','mansavi')
marks = [98,97,45,67,78]

student = {}
max = ['',0]
min = ['',0]
avg = 0

for index in range(len(names)):
    student[names[index]] = marks[index]
    
    if max[1] < marks[index]:
        max = [names[index], marks[index]]
    if min[1] == 0  or min[1] > marks[index]:
        min = [names[index], marks[index]]
    
print(student)

marksMoreThan80 = [x for x in marks if x > 80]
marksMoreThan80 = set(marksMoreThan80)
# print(marksMoreThan80)

print(max)
print(min)

avg = sum(marks) / len(marks)
print(avg)

for i in student:
    if(student[i] > avg):
        print(i, '->',student[i] )