'''name="Vinay"
college="GCEM"
age=21
marks=100.00
a=5
b=30
print("Name:",type(name))
print("College:", type(college))  
print("Age:", type(age))
print("Marks:", type(marks))'''

'''a=5
b=30
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Exponent:", a**b)'''

marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade: A")   
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks>=60:
    print("Grade: D")
else:
    print("Grade: F")
    