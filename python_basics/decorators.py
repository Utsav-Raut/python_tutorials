# A decorator is a function that takes another function as an argument, adds some kind of functionality and then returns another function.
# All of this without altering the source code of the original function that we passed in.

def decorator_function(original_function):
    def wrapper_function():
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)
decorated_display()