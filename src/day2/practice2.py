# IF STATEMENT
age=21
if (age>=18):
    print(" YOU'RE AND ADULT")

# IF- ELSE STATEMENT
if(age>=18):
    print("YOU'RE AN ADULT")
else:
    print("YOU'RE A MINOR")

#if-elif-else statement
marks=45
if(marks>60):
    print(" AVERAGE")
elif(marks>70):
    print("good")
elif(marks>90):
    print("Topper")
else:
    print("fail")
# Ternary operator
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

# for loop

a=int(input("enter  number"))
if a%3==0 and a%7==0 :
    print("div by both")
else:
    print(" not div by both")
