# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer n, the number of elements in the set s.
# The second line contains  space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Output Format
# Print the sum of the elements of set s on a single line.


n = input()
s = set(map(int, input().split()))

N = int(input())

print(s)

for i in range(N):
    # cmd, *digit = input().split()
    args = input().strip().split(" ")

    if args[0] == 'pop':
        x = s.pop()
        print(x)
    elif args[0] == 'remove':
        # print(args[1])
        s.remove(int(args[1]))
    elif args[0] == 'discard':
        print(args[1])
        s.discard(int(args[1]))

sum = 0
for x in s:
    sum += x
print(sum)






