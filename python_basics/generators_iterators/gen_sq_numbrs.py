# The following is for understanding generators in python
# Part 1

# This is how we usually implement
# def square_numbers(nums):
#     result = []
#     for num in nums:
#         result.append(num * num)
#     return result

# my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums) 
# Output : [1, 4, 9, 16, 25]


# This is by using generators
def square_numbers(nums):
    for num in nums:
        yield num * num

my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums)  # <generator object square_numbers at 0x7f7dfb4ab740>
# print(next(my_nums))    # 1
# print(next(my_nums))    # 4
# print(next(my_nums))    # 9
# print(next(my_nums))    # 16
# print(next(my_nums))    # 25
# print(next(my_nums))    #Stop Iteration exception

#Another way of printing values from generators and also for getting rid of StopIteration exception
for num in my_nums:
    print(num)

