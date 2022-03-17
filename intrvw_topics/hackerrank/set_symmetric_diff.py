# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format

# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

# list_of_vals1 = list(map(int, input().split()))
# print(list_of_vals1)
# set_a = set(list_of_vals1)
# print(set_a)


# list_of_vals2 = [int(x) for x in input().split()]
# set_b = set(list_of_vals2)
# print(set_b)

M = int(input())
list1 = list(map(int, input().split()))
N = int(input())
list2 = [int(x) for x in input().split()]

a = set(list1)
b = set(list2)

c = a.difference(b)
d = b.difference(a)

union_set = c.union(d)

result = sorted(union_set)

for x in result:
    print(x)