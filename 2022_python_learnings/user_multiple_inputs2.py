# https://python.plainenglish.io/taking-multiple-inputs-from-user-in-python-3-6cbe02d03a95

# Using List Cpmrehensions:

# 2 Input at a Time:
x,y = [int(a) for a in input('Enter some values').split()]
print(x, y)

# Taking Multiple Inputs at a time:
z = [int(p) for p in input('Enter multple values\n').split()]
print('List of values are : ',z)

# Taking User-Defined Number of Inputs:
num_of_inputs = int(input('How many inputs do u want to enter??\n'))
list_of_inputs = []

for i in range(num_of_inputs):
    t = input()
    print(t)