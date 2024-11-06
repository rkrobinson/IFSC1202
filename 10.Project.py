class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score.strip() else 0.0 for score in scores]
    def RunningAverage(self):
        valid_scores = [score for score in self.Grades if score > 0]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)
    def TotalAverage(self):
        return sum(self.Grades) / len(self.Grades)
    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
def read_students_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 4:
                continue  
            firstname = parts[0].strip()
            lastname = parts[1].strip()
            tnumber = parts[2].strip()
            scores = parts[3:]
            student = Student(firstname, lastname, tnumber, scores)
            students.append(student)
    return students
def print_student_report(students):
    print(f"{'First Name':<12} {'Last Name':<12} {'ID':<12} {'Running Avg':<12} {'Semester Avg':<12} {'Letter Grade':<12}")
    print('-' * 72)
    for student in students:
        print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} "
              f"{student.RunningAverage():<12.2f} {student.TotalAverage():<12.2f} {student.LetterGrade():<12}")
if __name__ == "__main__":
    filename = '10.Project Student Scores.txt'
    students = read_students_from_file(filename)
    print_student_report(students)