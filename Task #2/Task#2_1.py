# Leap year
y = int(input("enter a year"))
if y % 400 == 0:
    print("the given year is leap year")
elif y % 100 == 0:
    print("the given year is not a leap year")
elif y % 4 != 0:
    print("the given year is a leap year")
else:
    print("given year is not leap year")