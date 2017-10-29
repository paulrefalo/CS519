# CS 519 assignment 5 - classroom.py by Paul ReFalo
# Workig with Classes and Objects

# define Students class
class Students:
    # define constructor with id, first_anme, and last_name.  Add Class property assignments as list
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = []

    def get_full_name(self):
        # return string of full name with a space in the middle
        full_name = self.first_name + " " + self.last_name
        return full_name

    def get_assignments(self):
        # return the list of all assignments the student has submitted
        return self.assignments

    def get_assignment(self, name):
        # returns the first assignment in the list with a matching name.
        # If no matching assignment is found, it returns None. Upgraded assignments not counted in the average
        for ass in self.assignments:
            if ass.name == name:
                return ass
        return "None"

    def average(self):
        # return the average grade of ass assignments
        result = 0
        gradedAssignmentsCount = 0
        for ass in self.assignments:
            if ass.grade != "None" and isinstance( ass.grade, int ):
                result += ass.grade
                gradedAssignmentsCount += 1
        return result / gradedAssignmentsCount

    def submit_assignment(self, assignment):
        # takes the supplied assignment and adds it to the list of the students submitted assignments
        self.assignments.append(assignment)

    def remove_assignment(self, name):
        # removes the first assignment with a matching name
        for idx, ass in enumerate(self.assignments):
            if ass.name == name:
                self.assignments.remove(self.assignments[idx])


# define Assignments class
class Assignments:
    # define constructor with name, max_score, and grade with default="None"
    def __init__(self, name, max_score, grade="None"):
        self.name = name
        self.max_score = max_score
        self.grade = grade

    def assign_grade(self, grade):
        # assign grade property to grade or "None" if grade is greater than max_score
        if grade > self.max_score:
            self.grade = "None"
        else:
            self.grade = grade

