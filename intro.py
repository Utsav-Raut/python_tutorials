message = 'Hello World'
# print(message)


# If we need to have a multiline string then we can start
# and end with three quotes

new_message = """Bobby's world was a good cartoon
in the 1980s"""
# print(new_message)

# print(len(message))
# print(message[0])
# print(message[0:5])  #first index is inclusive and the last one is exclusive
# print(message[:5])  #alternative of the above line
# print(message[6:])  # will print world


# print(message.lower())
# print(message.upper())

# print(message.count('Hello')) #Count the number of occurences of a particular word in the given string
# print(message.count('l'))


# print(message.find('World')) #This prints 6 because Worle begins at the sixth index of our message variable
# print(message.find('Universe')) #This returns -1 since the paramter passes does not exist in our string

# new_message = message.replace('World', 'Universe')
# print(new_message) #The replace method returns a modified string and hence we need to put the value in a variable

greeting = 'Hello'
name = 'Michael'
# message = greeting + ', ' + name + '. Welcome!'
# print(message)

#Alternatively, in case of complicated strings we can use a formatter string like we have done below:
# message = '{}, {}. Welcome!'.format(greeting, name)
# print(message)

#From Python 3.6 and above the concept of fstring has been introduced
#fstring makes string formatting as simpler as possible
# message = f'{greeting}, {name.upper()}. Welcome!'
# print(message)

# print(dir(name)) #This method shows us all the attributes and methods that we have access to for that variable

# print(help(str)) # shows us all info about string class
print(help(str.lower))
