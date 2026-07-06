#decorators
def decorator(func):

    def wrapper(name):
        print("===== Welcome =====")
        func(name)
        print("===== Thank You =====")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


name = input("Enter Name: ")

greet(name)

#generator
def even_numbers(limit):

    for i in range(1, limit + 1):

        if i % 2 == 0:
            yield i


num = int(input("Enter Limit: "))

gen = even_numbers(num)

print("Even Numbers")

for value in gen:
    print(value)

#Lambda Func

square = lambda x: x * x

number = int(input("Enter Number: "))

print("Square :", square(number))

# Higher Orderfunc

from functools import reduce

numbers = [10, 15, 20, 25, 30]

print("Original List :", numbers)

# map()
square = list(map(lambda x: x * x, numbers))

# filter()
even = list(filter(lambda x: x % 2 == 0, numbers))

# reduce()
total = reduce(lambda x, y: x + y, numbers)

print("Squares :", square)
print("Even Numbers :", even)
print("Sum :", total)