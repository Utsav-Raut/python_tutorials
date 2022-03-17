# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in range(0, len(seq)):
        count = 0
        for j in range(0, len(seq)):
            if seq[i] ==  seq[j]:
                count += 1
        if count%2 != 0:
            return seq[i]

    return None

# find_it([20,1,-1,2,-2,3,3])
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# ANOTHER METHOD TO SOLVE THIS 
# USING X-OR OPERATION

def find_it(seq):
    res = 0
    for elem in seq:
        res = res ^ elem
    if res == 0:
        return None
    else:
        return res

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))