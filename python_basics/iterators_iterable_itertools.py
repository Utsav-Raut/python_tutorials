# In Python if we can loop over something in a for-loop, we call it an iterable.
# The process of looping over elements is called iterating.

# for x in something:
#   Code and stuff

# here 'something' is an iterable.

# Using LIST 
# list = ['CX32', 'GSOF', 'Emily', 'Franz', 'Rex']
# for element in list:
#     print(element)

# A List is one type of sequence
# A Sequence is an iterable with a clear order to the components.
# Sequence = Iterable + Ordered
# Other common sequences are : tuples, strings, bytes

# Using TUPLE
# for element in ('Jose', 'Boh', 'Rusti'):
#     print(element)

# Using STRING
# for letter in 'Socratica':
#     print(letter)


# Iterating over a bytes object, one byte at a time
# for byte in b'Binary':
    # print(byte) # The ASCII code for each letter in 'Binary' is printed here


# WE CANNOT ITERATE OVER THE DIGITS OF AN INTEGER
# for digit in 299792458:
#     print(digit)

# The error message will read as 'int' object is not iterable

# To loop over the digits of an integer and have the digits treated as integers, we need to have this constructed ourselves

# c = 299792458
# digits = [int(d) for d in str(c)]

# for digit in digits:
#     print(digit)
# print(type(digits))

# So what makes an object iterable??

# Starting from python 3.3 there is a Collections.abc module where ABC stands for Abstract Base Classes
# We can read about it in the official python doc

# The key to iteration lies in two special methods - __iter__ and __next__

# container.__iter__()
#       returns an iterator object

# container.__next__()
#       returns the next item from the container
#       if there are no further items,
#           raise StopIterationException

3:00