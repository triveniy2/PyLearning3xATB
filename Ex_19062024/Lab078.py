def find_even_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(find_even_odd(10))

check_even_odd = lambda num: "even" if num % 2 == 0 else "odd"
print(check_even_odd(11))