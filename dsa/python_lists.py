# Demonstrating Lists in Python 
# Lists are dynamically sized arrays. They are fairly general and can contain any linear sequence of Python objects: functions, strings, integers, floats, objects and also, other lists. It is not necessary that all objects in the list need to be of the same type. You can have a list with strings, numbers , objects; all mixed up. 

# Constructing a basic list
# This list purely has integers
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(test_list)

# Constructing a mixed list
# This list has integers as well as strings
test_mixed_list = [1, 2, 3, 'test list']
print("Displaying test list:",test_list)
print("Displaying test mixed list:", test_mixed_list)

# Appending to a list
test_list.append(10)
print("After appending to test list:",test_list)

test_list = test_list + [13, 12, 11]
print("Now the test list is:",test_list)

# Delete from the test_list(IMP KEYWORD-DEL)
del test_list[2]
print("After deleting from test_list:",test_list)

# Sorting a list
test_list.sort()
print("The sorted list is : ",test_list)

# Reverse a list
test_list.reverse()
print("After reversing the list:",test_list)

# Now we will demonstrate "Multiplying" a list with a constant. I.e, the 
# list will be repeatedly concatenated to itself
list_to_multiply = ['a', 'b', 'c']
print("List to multiply originally:",list_to_multiply)

print("After multiplying the list by 3, we get")
product_list = 3 * list_to_multiply
print(product_list)