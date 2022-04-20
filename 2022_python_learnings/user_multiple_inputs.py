# https://python.plainenglish.io/taking-multiple-inputs-from-user-in-python-3-6cbe02d03a95

##################################################
# In Python, users can take multiple values or inputs in one line by two methods.
# - Using the split() method
# - Using List comprehension
##################################################

##################################################
# USING LIST METHOD
# input().split(separator, maxsplit)
# separator: This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.
# maxsplit: It is a number, which tells us to split the string into a maximum of provided number of times. If it is not provided then the default is -1 which means there is no limit.
##################################################

# a) Taking two inputs at a time:
a, b = input('Enter two values\n').split()
print(f'a is {a} and b is {b}')

# b) Taking Inputs with Separator and Maxsplit defined
new_args = input('Enter another set of values\n').split(',', 3)
print(new_args)

# c) Taking Multiple Inputs As List

# With Map Function:
x = list(map(int, input("Enter multiple values..").split()))
print('Marks of the students are:',x)

# Without Map Function:
y = list(input('Enter some more values....'.split()))
print(y)