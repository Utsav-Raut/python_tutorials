# Continuing with generators
# Part 2

# Demonstrating the last example with list-comprehension
# my_nums = [i*i for i in [1, 2, 3, 4, 5]]
# print(my_nums)




# Demonstrating the same with generator
# my_nums = (i*i for i in [1, 2, 3, 4, 5])
# for num in my_nums:
#     print(num)




#  Although it takes away the real purpose of generators but we can still convert the results of a generator into a list and print all at once
my_nums = (i*i for i in [1, 2, 3, 4, 5])
print(list(my_nums))