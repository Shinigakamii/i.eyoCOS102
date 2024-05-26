import pandas as pd
import csv
df = pd.read_csv('SIS.csv')
df

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.students = self.load_students()
        self.pirates = []
        self.yankees = []
        self.bulls = []

    def load_students(self):
        students = []
        with open(self.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                student = Student(row['name'], int(row['age']), row['grade'])
                students.append(student)
        return students

    def classify_students(self):
        for student in self.students:
            if 14 < student.age < 18:
                self.pirates.append(student)
            elif 18 < student.age < 22:
                self.yankees.append(student)
            elif 22 < student.age < 25:
                self.bulls.append(student)
            elif student.age > 25:
                print(self.get_error_message())

    def write_csv(self, category, students):
        filename = f"The_{category}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'age', 'grade'])
            for student in students:
                writer.writerow([student.name, student.age, student.grade])
        print(f"{filename} created and displayed.")

    def get_error_message(self):
        return "Error: Student age is greater than 25."

    def process(self):
        self.classify_students()
        if self.pirates:
            self.write_csv('Pirates', self.pirates)
        if self.yankees:
            self.write_csv('Yankees', self.yankees)
        if self.bulls:
            self.write_csv('Bulls', self.bulls)


# Creating a sample SIS.csv file because idk 
with open('SIS.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age', 'grade'])
    sample_data = [
        ["Aina Adeleke	",16, 80],
        ["Sola Egbune",23, 55],
        ["Callistus Okeke	",17, 40],
        ["Martin Alegbe	", 25, 77],
        ["Mary Akande",20, 87],
        ["Stella Olohimen",17, 44],
        ["Gabriel Pati	",18, 50],80
        ["Durojaiye Adamu	",24, 60],
        ["Kolawole Alabi",27, 67],
        ["Tope Ogunleye",22, 54],
        ["Wilfred Nwachukwu",16, 45],
        ["Mildred James",15, 70],
        ["Glory Babalola",21, 69],
        ["Edith Ade",22, 57],
        ["Godwin Osahon	",20, 51],
        ["Philip Odion	",19, 68],
        ["Adelabu Glory",26, 78],
        ["Igor Lawal",20, 55],
        ["Abraham Esther",28, 89],
        ["Agbara Jamiat",26, 67],
        ["Gbemisola Adewale",21, 80],      
    ]
    writer.writerows(sample_data)

# Running the StudentManager process
manager = StudentManager('SIS.csv')
manager.process()