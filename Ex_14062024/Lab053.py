# Multiple conditions
# switch in Java
# Match case in python
numbers = int(input("Enter a number: "))
match numbers:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")
