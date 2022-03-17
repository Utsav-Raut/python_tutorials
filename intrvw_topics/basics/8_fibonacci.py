# Program to print the nth fibonacci number

# METHOD 1: using recursion

# def fib_with_recur(n):
#     if (n <= 0):
#         print('Incorrect input')
#         return
#     elif (n == 1):
#         return 0
#     elif (n == 2):
#         return 1
#     else:
#         return (fib_with_recur(n-1) + fib_with_recur(n-2))

# num = int(input('Enter the nth number '))
# val = fib_with_recur(num)
# print(f'The term {num} of fibonacci series is {val}')


# METHOD 2: Using array

# def fib_with_arr(n):
#     if(n <= 0):
#         print('Incorrect input')
#         return 
#     data = [0, 1]

#     if n > 2:
#         for j in range(2, n):
#             data.append(data[j-1] + data[j-2])
#     return data[n-1]

# num = int(input('Enter the nth number '))
# val = fib_with_arr(num)
# print(f'The term {num} of fibonacci series is {val}')


# METHOD 3: Using Dynamic Programming

def fib_with_dynamic_prog(n):
    a = 0
    b = 1
    sum = 0
    if n <= 0:
        print('Incorrect input')
        return
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        for j in range(2, n):
            sum = a + b
            a = b
            b = sum
        
        return sum

num = int(input('Enter the nth number '))
val = fib_with_dynamic_prog(num)
print(f'The term {num} of fibonacci series is {val}')