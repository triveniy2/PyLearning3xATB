#What does the ^ operator do in Python, and in what context is it commonly used?


"""^ operator is used for bitwise XOR operation in python.
It returns 1 if one of the bits is 1 and the other is 0 else returns 0.
It is commonly used in cryptography and other bitwise operations."""
a = 10
b = 6
print(a ^ b)

"""
10 binary equivalent is 1010
6 binary equivalent is 0110
1010
0110
_____(XOR)
1100
which is eual to decimal 12.

"""