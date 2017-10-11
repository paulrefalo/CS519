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
from pprint import pprint
from operator import itemgetter
import operator

students = []   # declare empty students list to contain student dictionaries

student1 = {'id':12345, 'first_name':'John', 'last_name':'Lennon', 'assignments':[('assignment_1',0),('assignment_2',2),('assignment_3',4)]}
student2 = {'id':12346, 'first_name':'Paul', 'last_name':'McCartney', 'assignments':[('assignment_1',2),('assignment_2',3),('assignment_3',2)]}
student3 = {'id':12347, 'first_name':'Ringo', 'last_name':'Starr', 'assignments':[('assignment_1',3),('assignment_2',1),('assignment_3',1)]}
student4 = {'id':12348, 'first_name':'George', 'last_name':'Harrison', 'assignments':[('assignment_1',3),('assignment_2',4),('assignment_3',3)]}
student5 = {'id':12349, 'first_name':'Pete', 'last_name':'Best', 'assignments':[('assignment_1',4),('assignment_2',2),('assignment_3',4)]}

students.extend((student5, student2, student3, student4, student1))     # students added out of order then sorted for testing
students.sort(key=itemgetter("id"))

# pprint(students)
# print("Number of assignments: " + str(numOfAssignments))
# print(s["assignments"][1][1])
# print(s["assignments"][num][1])


#This should return the average grade of all assignments from all students
#every assignment is equally weighted

def average_grade(students):
    grades = []                                     # define empty list to hold all of the grades for all of the students

    for s in students:                              # loop over all students and append their grades to grades list
        numOfAssignments = len(s["assignments"])    # get length of assignments list of tuples to set range
        for num in range(0, numOfAssignments):
            grades.append(s["assignments"][num][1]) # get the second element of the tuple and append grades list

    gradesAverage = sum(grades) / len(grades)       # do the math to get the avg and return it
    return gradesAverage

averageOfAllGrades = average_grade(students)        # call function and report the result
print(str("The average grade of all assignments of all the students is: " + str(averageOfAllGrades)))

#This function should return a list of the n student dictionaries with the
#highest grades on the assignment passed in as assignment name
#If there is a tie then it is broken by returning the student(s) with the
#lowest id number(s)

def highest_n_grades(students, assignment_name, n):
                                                            # Get tuple index for assignment_name
    numOfAssignments = len(students[0]["assignments"])      # get length of assignments list of tuples to set range
    assignmentIndex = -1

    for num in range(0, numOfAssignments):
        print(students[0]["assignments"][num][0])
        if students[0]["assignments"][num][0] == assignment_name:
            assignmentIndex = num
            print("Yes, found index:  " + str(assignmentIndex))
            break

    if assignmentIndex < 0:                                 # check to be sure we found the assignment
        print("Bummer, can't find the assignment you asked for")
        return []

    assignmentScores = []

    for s in students:
        id = s["id"]
        score = s["assignments"][assignmentIndex][1]
        assignmentScores.append([id, score])

    sortList = sorted(assignmentScores, key=operator.itemgetter(1), reverse=True)

    pprint(sortList)

    listOfHighest = []
    for e in sortList:
        id = e[0]
        for s in students:
            if s["id"] == id:
                listOfHighest.append(s)

    return listOfHighest[:n]                                # return appropriate slice of list

returnedList = highest_n_grades(students, "assignment_2", 3)
pprint(returnedList)


#This function should accept a student dictionary, a string representing
#an assignment name and a grade. If that assignment name does not exist
#the assignment and grade should be added to the end of the list of assignments. If
#this was successful it should return true, otherwise it should return false.

#def add_grade(student, assignment_name, grade):


#This function should accept a student dictionary, a string
#representing an assignment name and a grade. If that assignment name exists
#the grade should be changed to the supplied grade. If the assignment was found
#and updated the function should return true, otherwise it should return false.
#The order of assignments should be preserved.

#def update_grade(student, assignment_name, grade):


#Write a function called passing_student_ids which accepts as an argument a list
#of students. It should return a list of student ids which represent students
#having an average grade on all of their assignments which is >= 2.0


'''John Lennon, Paul McCartney, Ringo Starr, George Harrison, Pete Best, Stuart Sutcliffe'''