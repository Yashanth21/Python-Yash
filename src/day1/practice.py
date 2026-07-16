name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

print("\n ---STUDENT DETAILS --- ")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"CGPA : {cgpa}")

print("\n ---Type of Variables---")
print(type(name))
print(type(age))
print(type(cgpa))

print("\n----- OBJECT ID -----")
print("ID of Name :", id(name))
print("ID of Age  :", id(age))

# Arithmetic Operators
print("\n----- ARITHMETIC OPERATORS -----")
a = 20
b = 10

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

# Comparison Operators
print("\n----- COMPARISON OPERATORS -----")
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Logical Operators
print("\n----- LOGICAL OPERATORS -----")
print(age >= 18 and cgpa >= 7.5)
print(age >= 18 or cgpa >= 7.5)
print(not(age >= 18))

# Assignment Operators
print("\n----- ASSIGNMENT OPERATORS -----")
x = 10
x += 5
print("After += :", x)

x *= 2
print("After *= :", x)

# Identity Operators
print("\n----- IDENTITY OPERATORS -----")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 == list3 :", list1 == list3)

# Membership Operators
print("\n----- MEMBERSHIP OPERATORS -----")
print("Python" in "I Love Python")
print(20 in [10, 20, 30])
print(50 not in [10, 20, 30])

# Type Casting
print("\n----- TYPE CASTING -----")
num = "100"

print(int(num))
print(float(num))
print(str(100))
print(bool(1))
print(bool(0))


# Mutable Data Types
print("\n----- MUTABLE DATA TYPES -----")

numbers = [10, 20, 30]
print("Original List :", numbers)

numbers.append(40)
print("After Append  :", numbers)

student = {
    "Name": name,
    "Age": age
}

student["CGPA"] = cgpa
print(student)

colors = {"Red", "Blue"}

colors.add("Green")
print(colors)

# Immutable Data Types
print("\n----- IMMUTABLE DATA TYPES -----")

text = "Python"
print(text)

marks = (90, 80, 70)
print(marks)

# Ordered Data Types
print("\n----- ORDERED DATA TYPES -----")

fruits = ["Apple", "Mango", "Orange"]
print(fruits)
print(fruits[0])

subjects = ("Math", "Science", "English")
print(subjects)

# Unordered Data Types
print("\n----- UNORDERED DATA TYPES -----")

languages = {"Python", "Java", "C++"}
print(languages)

# Dictionary
print("\n----- DICTIONARY -----")

employee = {
    "ID": 101,
    "Name": "John",
    "Salary": 45000
}

print(employee)
print(employee["Name"])

# String Operations
print("\n----- STRING OPERATIONS -----")

language = "Python Programming"

print(language.upper())
print(language.lower())
print(language.replace("Python", "Java"))
print(language.split())
print(len(language))

print(language.upper())
print(language.lower())
print(language.replace("Python", "Java"))
print(language.split())
print(len(language))