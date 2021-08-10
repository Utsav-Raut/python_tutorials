# PASSING FUNCTIONS AS PARAMETERS

# def square(x):
#     return x*x

# def cube(x):
#     return x*x*x

# def my_map(func, arg_list):
#     result = []
#     for arg in arg_list:
#         result.append(func(arg))
#     return result

# squares = my_map(square, [1, 2, 3, 4, 5]) # we pass square function as paramter without parenthesis
# print(squares)

# cubes = my_map(cube, [1, 2, 3, 4])
# print(cubes)

# ****************************************************

# RETURNING FUNCTIONS 

# def logger(msg):
#     def log_message():
#         print('Log: ',msg)
    
#     return log_message

# log_hi = logger('Hi')
# log_hi()

def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_text

print_h1 = html_tag('h1') # This returns a function which takes in a parameter
print(print_h1)
print_h1('Test Headline') # Calling the function returned above, with a parameter
print_h1('Another Headline')

print_h1 = html_tag('p')
print_h1('Test paragraph')