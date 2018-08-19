# import my_module_9
# import my_module_9 as mm
# from my_module_9 import find_index        #This gives us access only to the find_index function
# from my_module_9 import find_index, test   # This gives us access to both find_index and test
#from my_module_9 import find_index as fi, test
#from my_module_9 import *          # This imports everything

# import sys

# courses = ['History', 'Math', 'Physics', 'CompSci']
# index = my_module_9.find_index(courses, 'Math')
# print(index)

# index = mm.find_index(courses, 'Math')
# print(index)


# index = find_index(courses, 'Math')
# print(index)
# print(test)


# When we import a module it checks multiple locations and the locations that it checks is within a list called sys.path
# we can see the list if we import the module. So we import sys above
# The order in which the search is made in order of the directory in which we are running the script, followed by the directories listed in the python path environment variable, next it adds the standard libraries directories, lastly it adds the side packages directories(3rd party library packages)
# print(sys.path)


#If we move the module to some other location then we can add that location to our sys list as well. The steps to do so are:
# import sys
# sys.path.append('path_to_module_on_our_system')

#Next we can make the change in the python path environment variable
#To set environment variable on Linux, we open a terminal --> open .bash_profile file using nano ~/bash_profile --> Go to the very end  and set the python path as export PYTHONPATH = "path_to_module_on_our_system"
#Next we open a new terminal and type python
# On getting a prompt, we type import my_module_9 --> the print statement within the module shows that the path got added successfully



################################################

# Using the standard python library
# import random
#
# courses = ['History', 'Math', 'Physics', 'CompSci']
# random_course = random.choice(courses)
# print(random_course)


# import math
#
# rads = math.radians(90)
# print(rads)
# print(math.sin(rads))


# import datetime
# import calendar
#
# today = datetime.date.today()
# print(today)
# print(calendar.isleap(2020))



# import os
# print(os.getcwd())
# The standard library files are just python files themselves. We can view the location of a module just by printing out it's dunder-file attribute
# print(os.__file__)



import antigravity
