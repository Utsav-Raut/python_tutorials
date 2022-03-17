# Given a number \’n\’, how to check if n is a Fibonacci number. 
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .. 

# Examples : 

# Input : 8
# Output : Yes

# Input : 34
# Output : Yes

# Input : 41
# Output : No

# Following is an interesting property about Fibonacci numbers that can also be used to check if a given number is Fibonacci or not. 
# A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 – 4) is a perfect square
import math
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    # print(s)
    return s*s == x

def check_fib(num):
    # print(5 * (num ** 2) + 4)
    return isPerfectSquare(5 * (num ** 2) + 4) or isPerfectSquare(5 * (num ** 2) - 4)

num = int(input('Enter a number to check : '))

result = check_fib(num)

if result == True:
    print(f'{num} is a Fibonacci no.')
else:
    print(f'{num} is not a Fibonacci no.')


