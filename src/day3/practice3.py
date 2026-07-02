#

#dictionaries

student = {
    "Name": "John",
    "Age": 20,
    "City": "Chennai"
}

# Access
print(student["Name"])

# Add
student["Course"] = "Python"

# Update
student["Age"] = 21

# Remove
student.pop("City")

# Membership
if "Age" in student:
    print("Age Found")

print("\nKeys")
for i in student.keys():
    print(i)

print("\nValues")
for i in student.values():
    print(i)

print("\nItems")
for key, value in student.items():
    print(key, ":", value)

print("Length:", len(student))
