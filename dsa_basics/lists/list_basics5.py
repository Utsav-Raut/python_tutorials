# LIST COMPREHENSION
# Syntax:
# list_variable = [x for x in iterable]

# ist comprehensions offer a succinct way to create lists based on existing lists. When using list comprehensions, lists can be built by leveraging any iterable, including strings and tuples.

shark_letters = [letter for letter in 'shark']
print(shark_letters)

# The above snippet can be rewritten as 
shark_letters = []
for i in 'shark':
    shark_letters.append(i)
print('Using FOR LOOP....')

print(shark_letters)

# Using Conditionals with List Comprehensions

fish_tuple = ['blowfish', 'catfish', 'clownfish', 'octopus']
print('Using conditionals in list comprehension....')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

print('Another conditional example...')
num_list = [i **2 for i in range(10) if i % 2 == 0]
print(num_list)

new_num_list = [i for i in range(100) if i % 3 == 0 and i % 5 == 0]
print(new_num_list)


# Nested Loops in a List Comprehension
print('Without List Comprehension..')

my_list = []

for i in [20, 40, 60]:
    for j in [2, 4, 6]:
        my_list.append(i*j)
print(my_list)

print('With List comprehension')

new_my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(new_my_list)
