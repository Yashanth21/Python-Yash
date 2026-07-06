#sets

s = {10, 20, 30, 40}

# Add one element
s.add(50)

# Add multiple elements
s.update([60, 70])

# Remove an element
s.remove(20)

# Membership
if 30 in s:
    print("30 Found")

# Iterate
print("Elements:")
for i in s:
    print(i)

# Length
print("Total Elements:", len(s))

#tuples
t = (10, 20, 30, 40, 20)

print("First Element:", t[0])
print("Slice:", t[1:4])

print("Elements:")
for i in t:
    print(i)

print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Length:", len(t))

if 40 in t:
    print("40 Found")

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