# print('Hello World!!')

# msg = 'Hello World!'
# print(msg)

# first_name = 'Round'
# last_name = 'Robin'
# full_name = first_name + ' ' + last_name
# print(full_name)

# LISTS

# trees = ['Oak', 'Pine', 'Redwood', 'Chestnut', 'Neem', 'Deodar']
# print(trees)

# print(trees[0])
# print(trees[-1])

# print('Pine' in trees)

# for x in trees:
#     print(x)

# for i in range(0, len(trees)):
#     print(trees[i])

# INDEX
# print(trees.index('Chestnut'))
# print(trees.index('Pine', 1, 7))

# print(trees[:])

# APPEND
# trees.append('Bonsai')
# trees.append('Mango')
# trees.append('Neem')
# print(trees)

# shrubs = ['Tulsi', 'Pudina']
# trees.append(shrubs)
# print(trees)


# EXTEND
# shrubs = ['Tulsi', 'Pudina']
# trees.extend(shrubs)
# print(trees)

# INSERT
# trees.insert(3, 'Tomato')
# print(trees)

# REMOVE
# trees.remove('Oak')
# print(trees)
# trees.append('Neem')
# print(trees)
# trees.remove('Neem')
# print(trees)

# COUNT
# print(trees.count('Oak'))
# print(len(trees))
# alphanumeric = [1, ('a', 1), [3, 4], ('a', 1), (7, 5, 6)]
# print(alphanumeric)
# print(alphanumeric.count(('a', 1)))

# POP
# pop_op = trees.pop()
# print(pop_op)
# print(trees)

# pop_op = trees.pop(1)
# print(pop_op)
# print(trees)

# pop_op = trees.pop(-1)
# print(pop_op)
# print(trees)

# REVERSE
# reverse() function is doing in place reversal of list and it is not returning anything that's the reason l gets assigned None

# trees.reverse()
# print(trees)

# for x in reversed(trees):
#     print(x)

# SORT
# trees.sort(reverse=True)
# print(trees)

# COPY
# = makes changes to both the lists since they refer to the same location
# new_trees = trees
# new_trees.append('Banyan')
# print(trees)
# print(new_trees)

# new_trees = trees.copy()
# new_trees.append('Banyan')
# print(trees)
# print(new_trees)


# CLEAR and DELETE
# trees.clear()
# print(trees)

# del trees[:]
# print(trees)



# TUPLE
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable,  and allow duplicate values.

# my_names = ('Tim', 'Pong', 'Toot', 'Potts', 'Catss', 'Bats')
# print(type(my_names))
# print(my_names)
# print(my_names[0])
# print(my_names[-1])

# print(len(my_names))

# TUPLE with one item
# my_tuple = ("Grindlewald",)
# print(my_tuple)

# print(my_names[-4:-1])

# if "Bats" in my_names:
#     print("Yess")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# names_list = list(my_names)
# names_list[1] = 'Kiwi'
# my_names = tuple(names_list)
# print(my_names)

# SAME WAY IF ONE WANTS TO REMOVE ANY ITEM THEY CAN CONVERT TO LIST AND DO POP OR REMOVE

# PACKING AND UNPACKING
# veggies = ('cabbage', 'peas', 'potato', 'tomato', 'corainder')
# (red, *yellow, blue) = veggies

# print(red)
# print(yellow)
# print(blue)
# print(veggies)


# print("Hi"*10)

# JOINING TUPLES
# tuple1 = (1, 2, 3)
# tuple2 = ('a',)

# print(tuple1 + tuple2)
# print(tuple2 * 2)

# COUNT
# print(my_names.count('Bats'))


# SETS
# A set is a collection which is both unordered, unindexed, unchangeable, and do not allow duplicate values.
# Sets are written with curly brackets.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Once a set is created, you cannot change its items, but you can add new items.

# set_of_fruits = {'pineapple', 'grapes', 'mango', 'guava', 'pear', 'banana', 99, 75, 255.36}
# print(set_of_fruits)

# for x in set_of_fruits:
#     print(x, end=',')
# print()
# print(99 in set_of_fruits)


# ADDING ITEMS
# set_of_fruits.add("orange")
# print(set_of_fruits)

# seasonal = {'mango', 'jojoba'}
# set_of_fruits.update(seasonal)
# print(set_of_fruits)


# REMOVING
# set_of_fruits.remove('banana')
# print(set_of_fruits)

# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# set_of_fruits.clear()
# print(set_of_fruits)


# SET OPERATIONS
# Union

# seasonal = {'jackfruit', 'papaya', 'mango'}
# set_union = set_of_fruits.union(seasonal)
# print(set_union)

# set_intersec = set_of_fruits.intersection(seasonal)
# print(set_intersec)

# sym_diff = set_of_fruits.symmetric_difference(seasonal)
# print(sym_diff)



# DICTIONARIES
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# my_dict = {
#     "name": "Tom",
#     "species": "cat",
#     "gender": "Male"
# }
# print(len(my_dict))

# print(my_dict['gender'])
# print(my_dict.get('species'))

# print(my_dict.keys())
# print(my_dict.values())

# editing the value of a key
# my_dict['species'] = 'Cat'
# print(my_dict)

# adding a new key-value pair
# my_dict['channel'] = 'Cartoon Network'
# print(my_dict)


# key-value  pair items
# print(my_dict.items())


# checking if a key exists
# if 'name' in my_dict:
#     print('Name exists')

# my_dict.update({"name": "Thomas"})
# print(my_dict)

# pop, delete, clear
# print(my_dict.pop('name'))
# print(my_dict.popitem())

# del my_dict['species']
# print(my_dict)

# my_dict.clear()
# print(my_dict)

# LOOPING
# for x in my_dict:
#     print(x, my_dict[x])

# for i in my_dict.values():
#     print(i)

# for i in my_dict.keys():
#     print(i)

# for x, y in my_dict.items():
#     print(x, y)

# COPY DICTIONARIES
# new_dict = my_dict.copy()
# print(new_dict)

# new_dict = dict(my_dict)
# print(new_dict)

# NESTED DICTONARIES




# MATHSSSSSS...

# a = max(15, 7, 88)
# print(a)

# print(abs(-47.84))

# print(pow(4, 2))

# import math
# print(math.sqrt(16))

# print(math.ceil(1.4))
# print(math.floor(1.4))
# print(math.pi)



# JSON
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.
# import json

# details = '{"name": "Ram", "age": 15, "city": "Kolkata"}'
# res = json.loads(details)
# print(res)


# my_dict = {
#     "name": "Tom",
#     "species": "cat",
#     "gender": "Male"
# }

# my_dict_json = json.dumps(my_dict)
# print(my_dict_json)

# details = {
#             "name": "John",
#             "age": 30,
#             "married": True,
#             "divorced": False,
#             "children": ("Ann","Billy"),
#             "pets": None,
#             "cars": [
#                 {"model": "BMW 230", "mpg": 27.5},
#                 {"model": "Ford Edge", "mpg": 24.1}
#             ]
# }

# print(json.dumps(details))
# print(json.dumps(details, indent=4, sort_keys=True))


# FILE OPS

# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# f = open('/home/boom/Desktop/hadoop.txt', 'rt')
# print(f.read())

# print(f.read(5))

# For reading just one line
# print(f.readline())

# for i in f:
#     print(i)

# f.close()

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# f = open('/home/boom/Desktop/prac.txt', 'a')
# f.write("Now we have more text into it.")
# f.close()

# f = open('/home/boom/Desktop/prac.txt', 'rt')
# print(f.read())



# f = open('/home/boom/Desktop/prac.txt', 'w')
# f.write("Whoops I deleted the whole content.")
# f.close()

# f = open('/home/boom/Desktop/prac.txt', 'rt')
# print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# f = open('/home/boom/Desktop/prac2.txt', 'x')
# f.write('Hey Buds!')
# f.close()
# f = open('/home/boom/Desktop/prac2.txt', 'r')
# print(f.read())

# import os
# if os.path.exists('/home/boom/Desktop/prac2.txt'):
#     os.remove('prac2.txt')
#     print("Done!!")
# else:
#     print("File doesnt exist")

# To remove folder: 
# os.rmdir("myfolder")

#SWAPPING

a = [1,2,3,4]
b = [5,6,7,8]

a,b = b,a

print(a)
print(b)