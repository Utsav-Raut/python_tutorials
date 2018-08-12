#Dictionaries allow us to work with key-value pairs. They are like maps of Java
#Keys can be any immutable data-types

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# print(student)
# print(student['name'])
# print(student['courses'])

# print(student['phone']) # This throws a key error
 #Instead of errors, we might want to display 'None' or some other message when a key is not found. We can do so by using the other method for retrieval of values-get() method
# print(student.get('name'))
# print(student.get('phone')) #instead of error, this returns a None by default.
# print(student.get('phone', 'Not Found')) # This is how we can specify default values for keys that don't exist


#Adding a new entry to our DICTIONARY
# student['phone'] = '555-5555'
# print(student.get('phone', 'Not Found'))

#If a key already exists, if we set it's value again, then it will update the value
# student['name'] = 'Jane'
# print(student.get('name'))
# print(student)

#We can also update using the update method. In order to update multiple values at a time we use the update method
#The update method takes in a DICTIONARY as an argument and the DICTIONARY is just everything that we either want to add or update
# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
# print(student)


#delete a specific key and it's values
# del student['age']
# print(student)

#another way to delete is by using the pop method. Pop method removes and returns the popped value
# age = student.pop('age')
# print(student)
# print(age)

# print(len(student)) #this prints the number of keys in our DICTIONARY
# print(student.keys()) #this prints all the keys of the DICTIONARY
# print(student.values()) #this prints the values in our DICTIONARY
# print(student.items()) # this prints the keys along with the values

#Looping through all the keys and values of our DICTIONARY
#If we have to loop through all the keys and values in our DICTIONARY we might be tempted to loop through like we loop through our list
#But if we just loop through our list without using any method then it will just loop through the keys
# for key in student:
#     print(key)

#In order to loop through keys and values we need to use the items method
for key, value in student.items():
    print(key, value)
