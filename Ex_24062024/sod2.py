# sum of digits in given number
def sum_of_digits(num):
    """Returns the sum of digits in the given integer"""

    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    return sum
print(sum_of_digits(12345))