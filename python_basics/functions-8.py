# def hello_func():
    # pass        #This keyword tells us that we can fill in the function body later but for now the compiler will not throw an error for leaving it blank
# hello_func()
# print(hello_func)

# def hello_func():
#     print('Hello Function!')
# hello_func()

#Returning values
# def hello_func():
#     return 'Hello Function.'
# print(hello_func())
# print(hello_func().upper())


#Passing arguments
# def hello_func(greeting):
#     return '{} Function.'.format(greeting)
# print(hello_func('Hi'))

# def hello_func(greeting, name = 'You'):
#     return '{}, {}'.format(greeting, name)
# print(hello_func('Hi', 'Bill'))
# print(hello_func('Hi', name = 'Corey'))
# print(hello_func('Hi'))

#It is important to remember that the required postional arguments have to come before the keyword arguments.
#If we try to create a function that is out of order then we might run into an error
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

#*args and **kwargs are allowing us to accept an arbitrary number of positional or keyword arguments.
#Let the above student_info function takes postional arguments that represents the classes that the student is taking plus the keyword arguments passed in would be random info about the student_info
#Thus in these scenarios we do not know how may positional and keyword argument parameters we might require.
#that is why we use *args and **kwargs
# student_info('Math', 'Art', name = 'John', age = 22)
#The output of args is actually a tuple with all of our positional arguments and our kwargs is the dictionary with all the keyword values


#sometimes we might notice a function call with arguments using the * or **. When it used in that context it will actually unpack a dictionary and pass those values into the function individually
# courses = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}
# student_info(courses, info)     #The output of this will be the complete list and the dictionary as postional arguments
# student_info(*courses, **info)  #This is how we unpack values. * unpack the list values and ** unpacks the keyword values



###############################################################################################################

#Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, false for non-leap years.""" #This is a doc string. It helps document where a function or a class is supposed to do
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in that month in that year"""

    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

# print(is_leap(2017))
print(days_in_month(2017, 2))
