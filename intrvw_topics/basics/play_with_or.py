# You are given an array arr[], you have to re-construct an array arr[].
# The values in arr[] are obtained by doing OR(bitwise or) of consecutive elements in the array.

# Example 1:

# â€‹Input : arr[ ] = {10, 11, 1, 2, 3}
# Output : 11 11 3 3 3
# Explanation:
# At index 0, arr[0] or arr[1] = 11
# At index 1, arr[1] or arr[2] = 11
# At index 2, arr[2] or arr[3] = 3
# ...
# At index 4, No element is left So, it will 
# remain as it is.
# New Array will be {11, 11, 3, 3, 3}.

def game_with_number(arr, n):
    new_arr = []
    for i in range(0, len(arr) - 1):
        new_arr.append(arr[i] | arr[i+1])
    new_arr.append(arr[-1])
    return new_arr

arr = [10, 11, 1, 2, 3]
res = game_with_number(arr, 5)
print(res)