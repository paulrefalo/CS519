# CS 519 assignment 5 - classroom_test.py by Paul ReFalo
# Test file for classroom.py Classes

from classroom import Students
from classroom import Assignments
from pprint import pprint


# It should create two students "Allen Allenson" and "Becky Beckyson" with ids of 123 and 456.
print("\n============= Instanciate two students 'Allen Allenson' and 'Becky Beckyson' with ids of 123 and 456 ===================")
s1 = Students(123, "Allen", "Allenson")
s2 = Students(456, "Becky", "Beckyson")

# It should use the get_full_name method to get their name and print it along with their id numbers.
print("\n============= Print names and IDs of both students ===================")
print("Student 1's full name is " + s1.get_full_name() + " and has an ID of " + str(s1.id))
print("Student 2's full name is " + s2.get_full_name() + " and has an ID of " + str(s2.id))

# You should create two different instances of an assignment named "Assignment 1" and two instances of "Assignment 2" with a maximum score of 100.
print("\n============= Instanciate four Assignments as described ===================")
a1_1 = Assignments("Assignment 1", 100)
a1_2 = Assignments("Assignment 1", 100)
a2_1 = Assignments("Assignment 2", 100)
a2_2 = Assignments("Assignment 2", 100)

# Assign a grade of 75 and 85 to Assignment 1 and 2 and submit them to Allen.
print("\n============= Assign 75 and 85 to Allen's Assignments 1 and 2 ===================")
a1_1.assign_grade(75)
a2_1.assign_grade(85)

print("\n============= Submit these two assignments ===================")
s1.submit_assignment(a1_1)
s1.submit_assignment(a2_1)

# Assign a grade of 90 and 100 to the other instances of Assignment 1 and 2 and submit them to Becky.
print("\n============= Similarly assign grades and submit assignments for Becky ===================")
a1_2.assign_grade(90)
a2_2.assign_grade(100)

s2.submit_assignment(a1_2)
s2.submit_assignment(a2_2)

# Use the get_assignment and get_full_name functions to get and print the scores of assignment 1 for Allen and Becky, printing out the name and the score.
print("\n============= Get 'Assignment 1' for Allen and Becky and print their names and scores ===================")
if s1.get_assignment("Assignment 1") == "None":
    print("No such assignment found for " + s1.get_full_name())
else:
    print(s1.get_full_name() + "'s score on Assignment 1 is a " + str(s1.get_assignment("Assignment 1").grade) + ".")

if s2.get_assignment("Assignment 1") == "None":
    print("No such assignment found for " + s2.get_full_name())
else:
    print(s2.get_full_name() + "'s score on Assignment 1 is a " + str(s2.get_assignment("Assignment 1").grade) + ".")

# Use the get_assignments function to get all of Beckys assignments printing out their name and grades.
print("\n============= Get all of Becky's assignment names and scores ===================")
beckysAssignments = s2.get_assignments()
print(s2.get_full_name() + "'s full list of assignments are:")
for ass in beckysAssignments:
    print("     " + ass.name + " with a score of " + str(ass.grade))

# Print the average grade of Becky.
print("\n============= Get Becky's average grade ===================")
print(s2.get_full_name() + "'s average on all graded assignments so far is " + str(s2.average()))

# Remove assignment 2 from Becky.
print("\n============= Remove Assignment 2 from Becky ===================")
s2.remove_assignment("Assignment 2")


# Print the average grade of Becky.
print("\n============= Get Becky's average grade again ===================")
print(s2.get_full_name() + "'s average on all graded assignments so far is " + str(s2.average()))

pprint(dir(s1))
print("Done")