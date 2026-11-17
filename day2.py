'''for i in range(0,5):
    print("good morning")
    print("coding is fun")'''

'''i=2
while i<=5:
    print("good morning")
    i+=5'''


'''def greet(name):
    print("Hello", name)
    print("Welcome to Python programming")
greet("Vinay")
greet("HuLK")'''

'''def add(a,b):
    result=a+b
    print(result)
add(5,10)
add(20,30)

def sub(a,b):
    result=a-b
    print(result)
sub(10,5)

def mul(a,b):
    result=a*b
    print(result)
mul(5,10)

def div(a,b):
    result=a/b
    print(result)
div(10,5)'''

'''student=["raj","ram","Alice", "Bob", "Charlie", "David", "Eva","vinay","sudeep"]
print(student[5])
print(student.append("John"))
student.insert(2,"Mia")
print(student)'''

'''student_details = {"vinay","GCEM", 21, 100.00}
print(student_details)'''

'''student={"name":"Vinay", "college":"GCEM", "age":21, "marks":100.00}
student["marks"]=90.00
print(student)'''

class Student:
    def __init__(self, name, college, age, marks): # self 
        self.name = name
        self.college = college
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("College:", self.college)
        print("Age:", self.age)
        print("Marks:", self.marks)

student1 = Student(1, "GCEM", 21, 100.00)
student1.display()  
student2 = Student("Alice", "XYZ University", 22, 95.50)
student2.display()