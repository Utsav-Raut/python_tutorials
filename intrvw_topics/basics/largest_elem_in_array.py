# Given an array A[] of size n. The task is to find the largest element in it.
 

# Example 1:

# Input:
# n = 5
# A[] = {1, 8, 7, 56, 90}
# Output:
# 90
# Explanation:
# The largest element of given array is 90.

def largest(arr, n):
    largest_elem = arr[0]
    for x in arr:
        if x > largest_elem:
            largest_elem = x
    
    return largest_elem

A = [1, 8, 7, 56, 90]
res = largest(A, 5)
print(res)