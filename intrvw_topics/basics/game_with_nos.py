# You are given an array arr[], you have to re-construct an array arr[].
# The values in arr[] are obtained by doing Xor of consecutive elements in the array.

# Example 1:

# Input : arr[ ] = {10, 11, 1, 2, 3}
# Output : 1 10 3 1 3
# Explanation:
# At index 0, arr[0] xor arr[1] = 1
# At index 1, arr[1] xor arr[2] = 10
# At index 2, arr[2] xor arr[3] = 3
# ...
# At index 4, No element is left So, it will remain as
# it is.
# New Array will be {1, 10, 3, 1, 3}.

def game_with_number(arr, n):
    new_arr = []
    for i in range(0, len(arr)-1):
        new_arr.append(arr[i] ^ arr[i+1])
    new_arr.append(arr[-1])
    return new_arr

# arr = [10, 11, 1, 2, 3]
arr = [5, 9, 7, 6]
res = game_with_number(arr, 5)
print(res)