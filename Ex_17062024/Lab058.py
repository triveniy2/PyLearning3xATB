# def say_hello():
#     print("Hello")
#
# result = say_hello()
# print(result)  # None
#
# def say_hello_arg(name):
#     print("Hello",name)
#
# result = say_hello_arg("Triveni")
# print(result)  # None
# say_hello_arg("Rahul")

def say_hello_arg_default(name = "triveni"):
    print("Hello", name)
say_hello_arg_default()
say_hello_arg_default("sachin")
say_hello_arg_default(name = "Rahul")


def sum_number_arg_ret(a, b):
    return a + b

result = sum_number_arg_ret(10, 20)
print(result)
result = sum_number_arg_ret(a =30, b=40)
print(result)

