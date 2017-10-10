# CS 519 assignment 3 - a3_skeleton by Paul ReFalo

#This is an example of the structure of a student dictionary
#They have an id number
#They have a first name, last name and a list of assignments
#Assignments are tuples of an assignment name and grade
#The grade is a 4 point scale from 0 to 4
'''
{'id':12345, first_name':'Alice', 'last_name':'Anderson',
'assignments':[('assignment_1',0),('assignment_2',2),('assignment_3',4)]}
'''

#This should return the average grade of all assignments from all students
#every assignment is equally weighted
def average_grade(students):


#This function should return a list of the n student dictionaries with the
#highest grades on the assignment passed in as assignment name
#If there is a tie then it is broken by returning the student(s) with the
#lowest id number(s)
def highest_n_grades(students, assignment_name, n):


#This function should accept a student dictionary, a string representing
#an assignment name and a grade. If that assignment name does not exist
#the assignment and grade should be added to the end of the list of assignments. If
#this was successful it should return true, otherwise it should return false.
def add_grade(student, assignment_name, grade):


#This function should accept a student dictionary, a string
#representing an assignment name and a grade. If that assignment name exists
#the grade should be changed to the supplied grade. If the assignment was found
#and updated the function should return true, otherwise it should return false.
#The order of assignments should be preserved.
def update_grade(student, assignment_name, grade):


#Write a function called passing_student_ids which accepts as an argument a list
#of students. It should return a list of student ids which represent students
#having an average grade on all of their assignments which is >= 2.0


