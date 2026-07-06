def double(func):
    def wrapper():
        print(" doubling the value")
        r = func()
        return r*2
    return wrapper
@double
def value():
    a=int(input("Enter a Number"))
    print(f"value is {a} ")
    return a
print(value())
