def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')


****
Ierator
****

#An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc. 
#Iterators are implemented using a class and a local variable for iterating is not required here, 
#It follows lazy evaluation where the evaluation of the expression will be on hold and stored in the memory until the item is called specifically which helps us to avoid repeated evaluation. 
#As lazy evaluation is implemented, it requires only 1 memory location to process the value and when we are using a large dataset then, wastage of RAM space will be reduced the need to load the entire dataset at the same time will not be there.

#Using an iterator-
#
#iter() keyword is used to create an iterator containing an iterable object.
#next() keyword is used to call the next element in the iterable object.
#After the iterable object is completed, to use them again reassign them to the same object.

iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))



**************************************


****
Generator
****
#
#It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in a defined function. 
#Generators are implemented using a function. Just as iterators, generators also follow lazy evaluation. 
#Here, the yield function returns the data without affecting or exiting the function. 
#It will return a sequence of data in an iterable format where we need to iterate over the sequence to use the data as they won’t store the entire sequence in the memory.

def sq_numbers(n):
	for i in range(1, n+1):
		yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))


****************************************


# strptime vs strftime

# strptime means string parser, this will convert a string format to datetime.

# strftime means string formatter, this will format a datetime object to string format.

**************************************

# datetime

import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

# 2018-12-19 09:26:03.478039

date_object = datetime.date.today()
print(date_object)



from datetime import date

today = date.today()

print("Current date =", today)
