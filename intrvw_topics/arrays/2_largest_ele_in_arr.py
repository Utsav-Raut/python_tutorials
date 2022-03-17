# Program to find out the largest element in an array

def largest_ele(arr):
    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
    
    return largest

print("Enter the array elements ")
arr = [int(val) for val in input().split()]

res = largest_ele(arr)

print('The largest element in the array is ',res)