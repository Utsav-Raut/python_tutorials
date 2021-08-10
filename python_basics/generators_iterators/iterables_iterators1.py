# A list is iterable because we can loop over it, but it is not an iterator
# We can also loop over tuples, dictionaries, files, strings, generators and all kinds of different objects, hence are iterable.
# We say something is iterable if it has a special method, a dunder method : __iter__()
# Dunder methods are also called special methods or magic methods

nums = [1,2,3]

# for num in nums:
#     print(num)

#print(dir(nums))   # We can see this prints the dunder iter method and hence can be looped over. In the background, the 'for-loop' is calling the iter on our object and it returns an iterator that we can loop over.



# An iterator is an object with a state so that it remembers where it is during iteration.
# Iterators know how to get the next value. This is done using the __next__() method. 
# We can see that a list doesn't has a __next__() method and thus the list doesnt have a state and hence doesn't know how to get the next values and is not an iterator.

# print(next(nums))   # This throws a TypeError: 'list' object is not an iterator



# When we run dunder iter method, it returns an iterator for us. We can manually run an iter method and check what it looks like.
# This is what the for-loop gets for us in the background.

# i_nums = nums.__iter__()  We can also write it as 
i_nums = iter(nums)     #This is the preferred way
print(i_nums)
print(dir(i_nums))      #We get several dunder methods but our concern is dunder iter() and dunder next()
# the dunder iter returns another dunder iter because iterators are also iterable. the returned dunder iter() returns the same object (i.e itself)

# We can use the next() method now
# print(next(i_nums)) # prints 1
# print(next(i_nums)) # prints 2
# print(next(i_nums)) # prints 3
# print(next(i_nums)) # prints StopIteration exception
# The for loop does the same as above until the last element.

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

# Iterators can only go forward and thus we cannot go backward, resetting it, or anything. We only go forward calling next()
