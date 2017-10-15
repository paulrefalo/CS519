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

student1 = {'id':12345, 'first_name':'John', 'last_name':'Lennon', 'assignments':[('assignment_1',0),('assignment_2',2),('assignment_3',3)]}
student2 = {'id':12346, 'first_name':'Paul', 'last_name':'McCartney', 'assignments':[('assignment_1',2),('assignment_2',3),('assignment_3',2)]}
student3 = {'id':12347, 'first_name':'Ringo', 'last_name':'Starr', 'assignments':[('assignment_1',2),('assignment_2',1),('assignment_3',1)]}
student4 = {'id':12348, 'first_name':'George', 'last_name':'Harrison', 'assignments':[('assignment_1',3),('assignment_2',4),('assignment_3',3)]}
student5 = {'id':12349, 'first_name':'Pete', 'last_name':'Best', 'assignments':[('assignment_1',4),('assignment_2',2),('assignment_3',3)]}
# student 6 added for testing but not added to list because Tom Petty is not one of the Beatles
student6 = {'id':12350, 'first_name':'Tom', 'last_name':'Petty', 'assignments':[('assignment_1',4),('assignment_2',2),('assignment_3',4)]}


# add multiple elements to list with extend
students.extend((student5, student2, student3, student4, student1))     # students added out of order then sorted for testing
students.sort(key=itemgetter("id"))                                     # sort by id first off to make second sort easier


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
print("Called function averageOfAllGrades *******************************************")
print(str("The average grade of all assignments of all the students is: " + str(averageOfAllGrades)))
print("\n")


#This function should return a list of the n student dictionaries with the
#highest grades on the assignment passed in as assignment name
#If there is a tie then it is broken by returning the student(s) with the
#lowest id number(s)

def highest_n_grades(students, assignment_name, n):
                                                            # Get tuple index for assignment_name
    numOfAssignments = len(students[0]["assignments"])      # get length of assignments list of tuples to set range
    assignmentIndex = -1

    for num in range(0, numOfAssignments):
        if students[0]["assignments"][num][0] == assignment_name:
            assignmentIndex = num
            break

    if assignmentIndex < 0:                                 # check to be sure we found the assignment
        print("Bummer, can't find the assignment you asked for")
        return []

    assignmentScores = []

    for s in students:
        id = s["id"]
        score = s["assignments"][assignmentIndex][1]
        assignmentScores.append([id, score])

    # students list previously sorted by Id in ascending order
    sortList = sorted(assignmentScores, key=operator.itemgetter(1), reverse=True)

    listOfHighest = []
    for e in sortList:
        id = e[0]
        for s in students:
            if s["id"] == id:
                listOfHighest.append(s)

    return listOfHighest[:n]                                # return appropriate slice of list

returnedList = highest_n_grades(students, "assignment_2", 2)
print("Called function returnedList *************************************************")
print("The returned List of Highest Grades for this assigment is: ")
pprint(returnedList)
print("\n")


#This function should accept a student dictionary, a string representing
#an assignment name and a grade. If that assignment name does not exist
#the assignment and grade should be added to the end of the list of assignments. If
#this was successful it should return true, otherwise it should return false.

def add_grade(student, assignment_name, grade):
    studentID = student["id"]
    assignmentsTuples = student["assignments"]
    assignmentsList = []

    for tup in assignmentsTuples:
        assignmentsList.append(tup[0])

    if assignment_name not in assignmentsList:
        for s in students:                          # find student by ID and append assign list for that student
            if s["id"] == studentID:
                s["assignments"].append((assignment_name, grade))
                return True
        # Shouldn't happen unless you passed in a student not in our list
        print("Student not found in master students list")

    return False

print("Calling function add_grade ****************************************************")
addGradeResult = add_grade(student3, "assignment_4", 3)
if addGradeResult:
    print("The result of add_grade is True\n")
else:
    print("The result of add_grade is False\n")


#This function should accept a student dictionary, a string
#representing an assignment name and a grade. If that assignment name exists
#the grade should be changed to the supplied grade. If the assignment was found
#and updated the function should return true, otherwise it should return false.
#The order of assignments should be preserved.

def update_grade(student, assignment_name, grade):
    studentID = student["id"]
    assignmentsTuples = student["assignments"]
    assignmentsList = []

    for tup in assignmentsTuples:
        assignmentsList.append(tup[0])

    if assignment_name in assignmentsList:
        for s in students:  # find student by ID and append assign list for that student
            if s["id"] == studentID:
                studentAssignments = s["assignments"]
                for idx, a in enumerate(studentAssignments):
                    if a[0] == assignment_name:
                        s["assignments"][idx] = (assignment_name, grade)
                        return True

        # Shouldn't happen unless you passed in a student not in our list
        print("Student not found in master students list")

    return False

print("Calling function update_grade *************************************************")
updateGradeResult = update_grade(student5, 'assignment_2', 4)
if updateGradeResult:
    print("The result of update_grade is True\n")
else:
    print("The result of update_grade is False\n")


#Write a function called passing_student_ids which accepts as an argument a list
#of students. It should return a list of student ids which represent students
#having an average grade on all of their assignments which is >= 2.0

def passing_student_ids(students):
    passingStudents = []

    for s in students:                              # loop over all students and append their grades to grades list
        grades = []
        numOfAssignments = len(s["assignments"])    # get length of assignments list of tuples to set range
        for num in range(0, numOfAssignments):
            grades.append(s["assignments"][num][1]) # get the second element of the tuple and append grades list

        print(s["first_name"])
        print(sum(grades))
        print(len(grades))
        print(sum(grades) / len(grades))
        if (sum(grades) / len(grades) >= 2.0):
            passingStudents.append(s["id"])


    return passingStudents       # list of IDs of students with grade avg >= 2.0

print("Calling function passing_student_ids *******************************************")
passingStudentsIDs = passing_student_ids(students)
print("The list of students passing have IDs: ")
pprint(passingStudentsIDs)