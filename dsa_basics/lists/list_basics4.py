# LIST METHODS

# Unlike strings, which are immutable, whenever we apply any method on a list we affect the list itself and not a copy of it.

# ######################################################
# LIST APPEND
# The method list.append(x) will add an item (x) to the end of a list. 

print('Before Append...')
fish = ['barracuda', 'cod', 'devil ray', 'eel']
print(fish)

print('After appending...')
fish.append('flounder')
print(fish)

# ######################################################
# LIST INSERT
# The list.insert(i,x) method takes two arguments, with i being the index position you would like to add an item to, and x being the item itself.

fish.insert(0, 'anchovy')
print('After INSERTING a new element...')
print(fish)

# ######################################################
# LIST EXTEND
# If we want to combine more than one list, we can use the list.extend(L) method, which takes in a second list as its argument.

more_fish = ['goby', 'herring', 'ide', 'kissing gourami']
fish.extend(more_fish)
print('After EXTENDING the fish list...')
print(fish)

# ######################################################
# LIST REMOVE
# When we need to remove an item from a list, we’ll use the list.remove(x) method which removes the first item in a list whose value is equivalent to x.

fish.remove('kissing gourami')
print('After removing an element from the list...')
print(fish)

# If you pass an item in for x in list.remove() that does not exist in the list, you’ll receive the following error:
# ValueError: list.remove(x): x not in list

# Keep in mind that list.remove() will only remove the first instance of the item you pass to it, so if we had two kissing gouramis at our aquarium and we only loaned one to the scientists, we could use the same construction of fish.remove('kissing gourami') and still have the second kissing gourami on our list.


# ######################################################
# LIST POP
# We can use the list.pop([i]) method to return the item at the given index position from the list and then remove that item. The square brackets around the i for index tell us that this parameter is optional, so if we don’t specify an index (as in fish.pop()), the last item will be returned and removed.

print('The element being popped: ', end = ' ')
print(fish.pop(3))
print(fish)



# ######################################################
# LIST INDEX
print('The INDEX of herring is:', end = ' ')
print(fish.index('herring'))


# ######################################################
# LIST COPY
# When we are working with a list and may want to manipulate it in multiple ways while still having the original list available to us unchanged, we can use list.copy() to make a copy of the list.

fish_2 = fish.copy()
print('This is the copied list: ')
print(fish_2)

# ######################################################
# LIST REVERSE
# We can reverse the order of items in a list by using the list.reverse() method. Perhaps it is more convenient for us to use reverse alphabetical order rather than traditional alphabetical order. In that case, we need to use the .reverse() method with the fish list to have the list be reversed in place.

print('Normal ordering of the list:')
print(fish)
print('The REVERSED Order is...')
fish.reverse()
print(fish)

reversed_fish_2 = list(reversed(fish_2))
print(reversed_fish_2)


# ######################################################
# LIST COUNT
# The list.count(x) method will return the number of times the value x occurs within a specified list. We may want to use this method when we have a long list with a lot of matching values.
print('Count =', end = ' ')
print(fish.count('goby'))


# ######################################################
# LIST SORT
# We can use the list.sort() method to sort the items in a list.

fish.sort()
print('Sorted fishes...')
print(fish)


# ######################################################
# LIST CLEAR
# When we’re done with a list, we can remove all values contained in it by using the list.clear() method.
fish.clear()
print('Clearing the list...')
print(fish)