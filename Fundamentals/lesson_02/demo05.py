class Student:

  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def get_average(self):
    return sum(self.grades) / len(self.grades)


student = Student(name="Bob", grades=[85, 90, 78])
print(f"{student.name}'s average: {student.get_average():.2f}")