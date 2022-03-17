# Given a natural number N, the task is to find the sum of the divisors of all the divisors of N.

# Example 1:

# Input:
# N = 54
# Output:
# 232
# Explanation:
# Divisors of 54 = 1, 2, 3, 6, 9, 18, 27, 54.
# Sum of divisors of 1, 2, 3, 6, 9, 18, 27, 54 
# are 1, 3, 4, 12, 13, 39, 40, 120 respectively.
# Sum of divisors of all the divisors of 54
#  = 1 + 3 + 4 + 12 + 13 + 39 + 40 + 120 = 232.

import math as ma


def sumOfDivisors(N):
    #code here 
    sum = 0
    for x in range(1, N + 1):
        if N%x == 0:
            # print(x)
            sum_of_divisor = 0
            for i in range(1, x + 1):
                if x%i == 0:
                    sum_of_divisor = sum_of_divisor + i
                    # print("Sum of divisor = ",sum_of_divisor)
            sum = sum + sum_of_divisor
    return sum


result = sumOfDivisors(10)
print(result)