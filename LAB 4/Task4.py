class Student:
    def __init__(self,id,name):
        self.id = id 
        self.name = name
    def display_details(self):
        print(f"The student id is {self.id}")
        print(f"The student name is {self.name}")
class Marks(Student):
    def __init__(self,id,name,marks_algo,marks_dataScience,marks_calculus):
        super().__init__(id,name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus
    def display_marks(self):
        print(f"The student marks in algo are {self.marks_algo}")
        print(f"The student marks in data science are {self.marks_dataScience}")
        print(f"The student marks in calculus are {self.marks_calculus}")
class Result(Marks):
    def __init__(self,id,name,marks_algo,marks_dataScience,marks_calculus):
        super().__init__(id,name,marks_algo,marks_dataScience,marks_calculus)
    def calculate_total_and_average_marks(self):
        self.total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        self.average_marks = self.total_marks/3
        super().display_details()
        super().display_marks()
        print(f"The total marks are {self.total_marks}")
        print(f"The average marks are {self.average_marks}")

result = Result("24K-0022","Muhammad Omer Siddiqui",4,4,2.33)
result.calculate_total_and_average_marks()