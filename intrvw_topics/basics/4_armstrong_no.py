# Program to check if a number is an Armstrong number or not
import math
def check_armstrong(num):
    res = 0
    while(num > 0):
        mod_val = num % 10
        res = res + (mod_val ** 3)
        # num = int(num / 10)
        num = num // 10
    return res

inp = int(input('Enter a number to check '))

res = check_armstrong(inp)
print(res)
if inp == res:
    print('{} is an armstrong number'.format(inp))
else:
    print('{} is not an armstrong number'.format(inp))
