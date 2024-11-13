class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grades = []
    def calculate_running_average(self):
        non_blank_grades = [grade for grade in self.grades if grade is not None]
        if len(non_blank_grades) == 0:
            return 0.0
        return sum(non_blank_grades) / len(non_blank_grades)
    def calculate_total_average(self):
        total_sum = 0
        for grade in self.grades:
            if grade is not None:
                total_sum += grade
            else:
                total_sum += 0
        if len(self.grades) == 0:
            return 0.0
        return total_sum / len(self.grades)
    def get_letter_grade(self):
        average = self.calculate_total_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
class StudentList:
    def __init__(self):
        self.students = []
    def add_student(self, firstname, lastname, tnumber):
        new_student = Student(firstname, lastname, tnumber)
        self.students.append(new_student)
    def find_student(self, tnumber):
        for i in range(len(self.students)):
            if self.students[i].tnumber == tnumber:
                return i
        return -1
    def print_student_list(self):
        print(f"{'First Name':>10} {'Last Name':>10} {'ID Number':>10} {'Running Avg':>12} {'Semester Avg':>12} {'Letter Grade':>12}")
        print('-' * 68)
        for student in self.students:
            running_avg = f"{student.calculate_running_average():.2f}"
            total_avg = f"{student.calculate_total_average():.2f}"
            letter_grade = student.get_letter_grade()
            print(f"{student.firstname:>10} {student.lastname:>10} {student.tnumber:>10} {running_avg:>12} {total_avg:>12} {letter_grade:>12}")
    def add_student_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                self.add_student(firstname, lastname, tnumber)
    def add_scores_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                tnumber = parts[0]
                score = parts[1]
                score = int(score) if score.isdigit() else None
                index = self.find_student(tnumber)
                if index != -1:
                    self.students[index].grades.append(score)
student_list = StudentList()
student_list.add_student_from_file('11.Project Students.txt')
student_list.add_scores_from_file('11.Project Scores.txt')
student_list.print_student_list()