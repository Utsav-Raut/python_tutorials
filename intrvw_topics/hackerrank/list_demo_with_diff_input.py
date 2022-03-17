# For this program the user would provide the number of iterations to run for
# Next the user would enter the type of operations it wants to perform in each iteration
# The user needs to enter the data correctly as per the operation that needs to be performed.


N = int(input())
operation_list = []
for ele in range(N):
    args = input().strip().split(" ")
    if args[0] == 'insert':
        operation_list.insert(int(args[1]), int(args[2]))
    elif args[0] == 'append':
        operation_list.append(int(args[1]))
    elif args[0] == 'print':
        print(operation_list)
    elif args[0] == 'remove':
        operation_list.remove(int(args[1]))
    elif args[0] == "pop":
        operation_list.pop()
    elif args[0] == "sort":
        operation_list.sort()
    elif args[0] == "reverse":
        operation_list.reverse()


# Sample Input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
        