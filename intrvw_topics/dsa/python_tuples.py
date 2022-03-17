# Demonstrating Tuples
# Tuples are sequences of immutable Python objects. They are quite similar to lists.
# The difference is, that tuples can't be changed, once creaed. i.e. they are immutable
# Also, tuples use parentheses while Lists use Square Brackers

# Let us declare some tuples to look at the general syntax.
tuple1 = ('history', 'geography', 1, 2, 3)
tuple2 = (1, 10, 20, 30)
tuple3 = "name", "age", "qualification"

tuple4 = () #Empty tuple

# Tuple with just one element: make sure to use the comma
tuple5 = (10,)

# Accessing values in tuples. Indexing and Slicing.
# Quite similar to Lists.
print(tuple1)
print(tuple1[2])
print(tuple1[1:3])

# Updating Tuples
# We can't update or change existing tuples since they are immutable. 
# However, we can make new tuples out of them
tuple4 = tuple2 + tuple3
print(tuple4)