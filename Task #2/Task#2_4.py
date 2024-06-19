# Fibonacci series:

n = int(input("Enter the value of n: "))
a1= 0
a2= 1
print(a1)
print(a2)
for i in range(2, n):
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print(a3)
    i = i+1