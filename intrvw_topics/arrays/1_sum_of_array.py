# Program to find the sum of array elements

def arr_sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i
    
    return sum

# inp_arr = [2, 3, 4, 19, 29]
print('Enter the array elements')
inp_arr = [int(val) for val in input().split()]
res = arr_sum(inp_arr)

print('The sum of array elements = ',res)