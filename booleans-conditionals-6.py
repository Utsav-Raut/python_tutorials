# Comparisons:
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Grreater or Equal:    >=
# Less or Equal:        <=
# Object Identity:      is      This checks if values have the same id, or basically if they are the same object in the memory

# language = 'Python'
#
# if language == 'Python':
#     print('Language is python')
# elif language == 'Java':
#     print('Language is java')
# else:
#     print('No match')

#Python does not have a switch case


# Boolean operations

# Using and
# user = 'Admin'
# logged_in = True
#
# if user == 'Admin' and logged_in:
#     print('Admin page')
# else:
#     print('Bad creds')


# Using or
# user = 'Admin'
# logged_in = False
#
# if user == 'Admin' or logged_in:
#     print('Admin page')
# else:
#     print('Bad creds')


# Using not
# user = 'Admin'
# logged_in = True
#
# if not logged_in:
#     print('Please log in')
# else:
#     print('Welcome')


###############################################
#Object Identity tests if two objects have the same id which means that they are basically the same objects in memory.
#Two objects can actually be equal and not be the same objects in memory
a = [1,2,3]
# b = [1,2,3]

# print(a==b) #This returns True
# print(a is b)   #This returns False because they are two different objects in memory and we can print out these locations with the built-in id function
# print(id(a))
# print(id(b))


#Now if we do like:
# b = a           #Now these are the same objects in memory
# print(id(a))
# print(id(b))
# print(a is b)   #This is true
# print(id(a) == id(b))
# print(a == b)   #This is true as well



#FALSE VALUES:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence, for example, '', (), []
    # Any empty mapping. For example, {}

# condition = None
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')


# condition = 0   # If condition is any value other than 0, the statement evaluates to True
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')


# condition = ''
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')


# condition = []
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')


# condition = {}
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')


# Now that we everything that evaluates to false, everything else will evaluate to True
condition = 'Test'
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
