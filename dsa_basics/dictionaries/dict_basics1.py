# The dictionary is Python’s built-in mapping type. Dictionaries map keys to values and these key-value pairs provide a useful way to store data in Python.

sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
jesse = {'username': 'JOctopus', 'online': False, 'points': 723}
print('READING FROM DICTIONARIES....')
print(sammy)
print(sammy['username'])
print(sammy['online'])
print(sammy['followers'])

# In addition to using keys to access values, we can also work with some built-in methods:
# dict.keys() isolates keys
# dict.values() isolates values
# dict.items() returns items in a list format of (key, value) tuple pairs

print(sammy.keys())
print(sammy.values())

for key, value in sammy.items():
    print(key, value)

print('Printing common keys.............')
for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])


# MODIFYING DICTIONARIES

print('Adding and changing dictionary elements......')
user_names = {'Sammy': 'sammy-shark', 'Jamie': 'mantisshrimp54'}
user_names['Drew'] = 'squidly'

print(user_names)

# DICTIONARIES MAY BE UNORDERED AND HENCE THE ITEMS MAY APPEAR IN ANY ORDER


drew = {'username': 'squidly', 'online': True, 'followers': 305}
drew['followers'] = 342
print(drew)

# We can also add and modify dictionaries by using the dict.update() method.
print('Before applying update method....')
print(jesse)
print('After applying update method')
jesse.update({'followers': 481})
print(jesse)

# DELETING ELEMENTS FROM DICTIONARY
# To remove a key-value pair from a dictionary, we’ll use the following syntax:
del jesse['points']
print('After deleting....')
print(jesse)

# If we would like to clear a dictionary of all of its values, we can do so with the dict.clear() method. This will keep a given dictionary in case we need to use it later in the program, but it will no longer contain any items.
print('After clearing...')
jesse.clear()
print(jesse)

# If we no longer need a specific dictionary, we can use del to get rid of it entirely:
del jesse
print('After deletion....')
print(jesse)