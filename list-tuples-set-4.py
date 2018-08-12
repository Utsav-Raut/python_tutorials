#Lists
courses = ['History', 'Maths', 'Physics', 'CompSci']
# print(courses)
# print('The length of the list is',len(courses))
# print(courses[2])
# print(courses[len(courses)-1])
# print(courses[-1]) #Negative indexes start from the end of the list
#It is sometimes convenient to use the negative index since that we way we need not worry about the length of the list

#Slicing of lists
# print(courses[0:2]) #Returns an array of elements from the list where the first index is inclusive but the second index is not
# print(courses[:2]) #It assumes that we want to start from the beginning and hence the first index is not necessary when we want elements from the beginning of the list
# print(courses[2:]) #Just as above, the compiler assumes that we want to go till the end of the list

#List methods
# courses.append('Art')#If we want to add an item to the end of our list, we can use the append method
# print(courses)
#
# courses.insert(0, 'Bio')#If we want to append an element at a specific location in the list we use the insert method. It takes two params- one is the index where we need to insert the new element and the second is the element itself
# print(courses)

courses_2 = ['Art', 'Education']
# courses.insert(0, courses_2)
# print(courses) #The entire list gets added instead of the values getting appended in the courses list---[['Art', 'Education'], 'History', 'Maths', 'Physics', 'CompSci']
# print(courses[0]) #This actually prints the list which is at index 0 -- ['Art', 'Education']
# courses.extend(courses_2)#To overcome the above situation we use Extend. Extend is used when we want to add multiple values to our list
# print(courses)

#Above if we would have used the method append then like insert the list would have got appended to the existing list as a list itself.


#Removing items from list
# courses.remove('Maths')
# print(courses)
#
# courses.pop() #By default this removes the last value from our list. This is useful if we want to use our list as a stack or a queue.
# print(courses)
#
# #pop actually returns the value that it removed. So we can capture the value in a variable
# popped = courses.pop()
# print(courses)
# print(popped)



#Sorting our list
# courses.reverse()#Reverse the list
# courses.sort()#Sorting our list in alphabetical order here
# print(courses)

# nums = [1, 5, 7, 6, 3]
# nums.sort() #Sorting takes place in the descending order by default, in case of a numeric list
# nums.sort(reverse=True) #Sorting the list in descending order
# print(nums)

#Till now we have been altering the list in place. But, there is also a way to sort our list without disturbing the original list like we have been doing till now
#The sorted method returns a sorted list. The actual list remains unaffected
# sorted_courses = sorted(courses)
# print('Actual courses',courses)
# print('Sorted courses',sorted_courses)


# nums = [1, 5, 7, 6, 3]
# print('Minimum value',min(nums))
# print('Maximum value',max(nums))
# print('Sum of the values in the list',sum(nums))

# print(courses.index('CompSci'))#index of a certain value
# print(courses.index('Geo')) #Returns a value error since Geo is not in our list

# print('Art' in courses)#Just to check if a value is in our list or not and get back a True or False result
# print('Maths' in courses)


# for item in courses:
#     print(item)


#We might want to retrieve the index of the value that we are on. To do this in Python, to access the index and value we can use enumerate function
# for index, course in enumerate(courses):
#     print(index, course)

#If we don't want to start at zero then we can pass the start value to our enumerate function
# for index, course in enumerate(courses, start=1):
#     print(index, course)


#Converting our lists into strings separated by a certain value
#Here we will be converting our list into a string of csv
# course_str = ', '.join(courses) #Or we can separate with hyphens
# course_str = ' - '.join(courses)
# print(course_str)


#WE can also turn a string back into a list
# new_list = course_str.split(' - ')
# print(new_list)


###############################################
#Tuples are very similar to lists with one major difference- We cannot modify Tuples.
#This lists are mutable and tuples are immutable

#MUTABLE
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
# print(list_1)
# print(list_2)


#IMMUTABLE
#In case of tuples we use parenthesis instead of square brackets
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

#Only those list methods that do not modify the lists can be used with tuples as well

###############################################

#Sets: These are values that are unordered and also have no duplicates
#In case of lists we use square brackets, in case of tuples we use parenthesis, in case of sets we use curly braces
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# print(cs_courses) #The outputs do not maintain the order of insertion. If we run the set a few more times we will see that the order keeps changing
#Sets  do not maintain order

# cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# print(cs_courses) #Still prints only one Math

#sets help in performing membership test where it checks if an element is a member of the set. Sets do these better than lists or tuples
# print('Math' in cs_courses) #Although the same thing can also be done by lists and tuples but set are optimized for this

#Sets also determine which values they share or don't share with other sets
art_courses = {'History', 'Math', 'Art', 'Design'}
# print(cs_courses.intersection(art_courses)) #Prints only math and history

# print(cs_courses.difference(art_courses)) #Shows those that are in cs but not in art

# print(cs_courses.union(art_courses)) #prints all elements from both sets
#for these kinds of operations only sets are better than lists and tuples


#How to create empty lists, tuples and sets

#Empty list
empty_list = []
empty_list = list()

#Empty tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty sets
empty_set = {} #THIS ACTUALLY WRONG.THIS WILL NOT CREATE AN EMPTY SET BUT INSTEAD WILL CREATE AN EMPTY DICTIONARY
empty_set = set() #This is the only way to create empty sets
