# The enumerate() method adds a counter to an iterable and returns it (the enumerate object).

# languages = ['C++', 'Python', 'Java', 'Javascript']
# enumerate_prime = enumerate(languages)

# print(list(enumerate_prime))

grocery = ['bread', 'pasta', 'grapes']
enumerateGrocery = enumerate(grocery)
# print(list(enumerateGrocery))
# for item in enumerateGrocery:
#     print(item)


enumerateGrocery = enumerate(grocery, 10)
# print(list(enumerateGrocery))
for count, item in enumerateGrocery:
    print(count, item)
