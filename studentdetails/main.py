import random
import csv
students = ['student'+str(i) for i in range(1, 101)] # we are taking total 100 students marks data by using range function

faculties  = [('Mathematics', 'Murali Krishna'), ('Telugu', 'Amarnath'), ('English', 'Samuel'),
              ('Social', 'Krishna Reddy'), ('Physics', 'Raja Gopal'), ('Chemistry', 'Ravi') ]

with open('student_marks.csv', 'w') as f: #Here in write mode writing the students,faculties in csv format

    for student in students: # Taking the data from students ie in range function in 3rd line
        for sub, fac in faculties:# Taking the data from faculties in 5th line
            f.write(','.join([student, sub, str(random.sample(range(1, 101), 1)[0])]) + '\n')

with open('subject_faculty.csv', 'w') as f: #Here in write mode subject_faculty data is creating in csv format
    for rec in faculties:
        f.write(','.join(rec) + '\n')
students_marks = [] #Table is created by this code
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))

subject_faculty = [] #Table is created by this code
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        subject_faculty.append(tuple(columns))
