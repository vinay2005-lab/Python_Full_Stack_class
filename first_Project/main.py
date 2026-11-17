'''class Student:
    def __init__(self, usn, name, marks):
        self.__usn = usn
        self.__name = name
        self.__marks = marks

    def get_usn(self):
        return self.__usn

    def set_usn(self, usn):
        self.__usn = usn

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print("USN:", self.__usn)
        print("Name:", self.__name)
        print("Marks:", self.__marks)
        print("=======================================")


class StudentManagement:
    def __init__(self):
        self.__students = []

    def add_student(self):
        usn = input("Enter USN: ").strip()

        for student in self.__students:
            if student.get_usn() == usn:
                print("Student with this USN already exists.")
                return

        name = input("Enter Name: ").strip()
        marks = float(input("Enter Marks: "))
        student = Student(usn, name, marks)
        self.__students.append(student)
        print("Student added successfully.")

    def display_students(self):
        if not self.__students:
            print("No students found.")
            return

        print("Student List:")
        for student in self.__students:
            student.display()

    def search_student(self, usn):
        for student in self.__students:
            if student.get_usn().lower() == usn.lower():
                print("Student found:")
                student.display()
                return
        print("Student not found.")

    def delete_student(self, usn):
        for student in self.__students:
            if student.get_usn().lower() == usn.lower():
                self.__students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

def main():
    app = StudentManagement()
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            app.add_student()
        elif choice == "2":
            app.display_students()
        elif choice == "3":
            usn = input("Enter USN to search: ")
            app.search_student(usn)
        elif choice == "4":
            usn = input("Enter USN to delete: ")
            app.delete_student(usn)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
'''
######################################################################################################################
'''class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)

        s1 = Student()
        s1.set_marks(85)
        s1.show_marks()
        '''

'''class grandfather:
    def land(self):
        print("Grandfather owns land.")

class father(grandfather):
    def house(self):
        print("Father owns a house .")
class son(father):
    def car(self):
        print("Son owns a car.")

s1 = son()
s1.land()   
s1.house()
s1.car()
'''


'''class animal:
        def sound(self):
            print("cat sound meow")

class dog(animal):
    def sound(self):
        print("dog sound bark")

class cat(animal):
    def sound(self):
        print("cat sound meow")

animals=[dog(), cat(), animal()]
for animal in animals:
    animal.sound()'''

########################################################################################
from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


class CreditCard(payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

p1 = UPI()
p1.pay(100000)
p2 = CreditCard()
p2.pay(1000)