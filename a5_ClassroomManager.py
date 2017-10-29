# CS 519 assignment 5 - a5_ClassroomManager by Paul ReFalo


class Students:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def get_assignments(self):
        return # list of all assignments teh student has submitted

    def get_assignment(self, name):
        return # the first assignment in the list with a matching name.  If no matching assignment is found, it returns None. Upgraded assignments not counted in the average

    def average(self):
        return # the average grade of ass assignments

    def submit_assignment(self, assignment):
        # takes the supplied assignment and adds it to the list of the students submitted assignments

    def remove_assignment(self, name):
        # removes the first assignment with a matching name


class Assignments:
    def __init__(self, name, max_score, grade="None"):
        self.name = name
        self.max_score = max_score
        self.grade = grade

    def assign_grade(self):
        if self.grade > self.max_score:
            self.grade = "None"
        else:
            self.grade = grade

student1 = Students(123, "Sara", "Smith")
fullName = student1.get_full_name()
print(fullName)
