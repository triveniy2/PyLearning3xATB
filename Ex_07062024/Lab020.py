# strings
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

name = "Triveni"
print(name)
print(type(name))
print(id(name))#-> memory location of the variable
print(len(name))
name = name.upper()
print(name)
name = name.lower()
print(name)
print(name.count('i'))
print(name[6])
# strings are immutable, we cant change the value of string