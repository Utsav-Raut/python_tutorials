# A Tuple, like a list is an ordered collection of elements, but unlike a list is immutable.
# Each element or value in a tuple is called an item.

coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
print(coral)

# Tuples have values between parentheses ( ) separated by commas ,. Empty tuples will appear as coral = (), but tuples with even one value must use a comma as in coral = ('blue coral',).

print('The following gives us a string....')
one_ele = ('elephaunt')
print(type(one_ele))
print(one_ele)

print('The following will make it a tuple...')
new_one_ele = ('elephaunt',)
print(type(new_one_ele))
print(new_one_ele)


# ACCESSING TUPLE ELEMENTS USING INDEXES
print('Accessing elements using positive indexes in tuples')
for i in range(0, len(coral)):
    print(coral[i])

print('Accessing elements using negative indexes in tuples')
for i in range(1, len(coral)+1):
    print(coral[-i])


# SLICING IN TUPLES WORKS EXACTLY LIKE LISTS
print("Slicing tuples in various ways............")
print(coral[1:3])
print(coral[:3])
print(coral[2:])
print(coral[-4:-2])
print(coral[-3:])

print()
print('Using strides..')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

print(numbers[2:11:2])

# CONCATENATING AND MULTPLYING TUPLES
# The + operator can be used to concatenate two or more tuples together. We can assign the values of two existing tuples to a new tuple:

print("Here are concetenated tuples....")
coral = ('blue coral', 'staghorn coral', 'pillar coral', 'elkhorn coral')
kelp = ('wakame', 'alaria', 'depp-sea tangle', 'macrocystis')
coral_kelp = coral + kelp

print(coral_kelp)

print('Now some multiplied tuples')
multiplied_corals = coral * 3
multiplied_kelps = kelp * 3

print(multiplied_corals)
