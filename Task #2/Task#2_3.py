#Factorial of a given number
n = int(input("enter number for finding factorial "))
fact =1
for i in range(1, n+1):
    fact = fact * i
print(fact)