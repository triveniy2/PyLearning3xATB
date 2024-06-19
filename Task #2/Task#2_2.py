#Triangle classifier:
side1 = int(input("enter side1 of triangle"))
side2 = int(input("enter side2 of triangle"))
side3 = int(input("enter side3 of triangle"))
if side1 == side2 and side2 == side3 :
    print("the given triangle is equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("the given triangle is isosceles triangle")
else:
    print("the given triangle is scalene triangle")
