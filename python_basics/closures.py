# def outer_func():
#     message = "Hi"

#     def inner_func():
#         print(message)

#     return inner_func()

# outer_func()

# **********************************

# def outer_func():
#     message = "Hi"

#     def inner_func():
#         print(message)

#     return inner_func

# my_func = outer_func()
# print(my_func)
# print(my_func.__name__)

# **********************************

# def outer_func():
#     message = "Hi"

#     def inner_func():
#         print(message)

#     return inner_func

# my_func = outer_func()

# my_func()
# my_func()
# my_func()

# A Closure is an inner function that remembers and has access to variables of the local scope in which it was created, even after the outer function has stopped executing


# **********************************

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func()
hello_func()