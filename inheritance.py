
class Person:#parent class
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        return f" {self.fname} {self.lname}"
teacherfname= input("Type in your first name\n")
teacherlname= input("Type in your last name\n")
teachergender = input("Are you a Mr., Ms., Mrs.\n")
teacher=Person(teacherfname,teacherlname)

#Let user input the class name and number of students
className=input("What is the name of the class?\n")
numberofStudents= int(input("How many students are in the class?\n"))
#Defining the class inheriting from "Person"
class Student(Person):#childclass
    def printname(self):
        print(f"Student names: {self.fname} {self.lname}")
students=[]#list to hold object(Students in this case)
for i in range(numberofStudents):
    studentfname= input("Please input your students first name:\n")
    studentlname=input("Please input your students last name:\n")
    student=Student(studentfname, studentlname)#calling student and creating a students object
    students.append(student)#this adds the students name to the list to be printed

print(f"Teacher name: {teacher.printname()}")
print(f"{teachergender} {teacher.printname()} ,you have {numberofStudents} student(s) in class {className}")
print("Students names:\n")
for student in students:#to repeat the loop to print the name
    student.printname()