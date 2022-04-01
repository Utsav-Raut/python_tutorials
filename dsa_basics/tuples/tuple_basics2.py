# TUPLE FUNCTIONS

# LENGTH
coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'depp-sea tangle', 'macrocystis')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print("the length of the tuple 'coral' is: ",len(coral))
print("the length of the tuple 'numbers' is: ",len(numbers))

# MAX and MIN
more_numbers = (11.13, 34.87, 95.59, 82.49, 42.73, 11.12, 95.57)

print("The min of the tuple 'more_numbers' = ",min(more_numbers))
print("The max of the tuple 'more_numbers' = ",max(more_numbers))



# TO MODIFY A TUPLE, WE CAN CONVERT IT TO A LIST
modify_tuple = ('India', 'Japan', 'China')
# modify_tuple[1] = 'Sri Lanka' # THIS WILL THROW AN ERROR (Tuple does not supprt item assignment)

tuple_list = list(modify_tuple)
tuple_list[1] = 'Sri Lanka'
modify_tuple = tuple(tuple_list)

print(modify_tuple)


# The tuple data type is a sequenced data type that cannot be modified, offering optimization to your programs by being a somewhat faster type than lists for Python to process. When others collaborate with you on your code, your use of tuples will convey to them that you don’t intend for those sequences of values to be modified.