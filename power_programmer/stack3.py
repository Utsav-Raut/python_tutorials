"""
Use a stack data structure to convert Integer values to binary
We are going to use a divide by 2 method

Example: 242

          quo   rem
242 / 2 = 121 -> 0 
121 // 2 = 60 -> 1
60 / 2 = 30 -> 0
30 / 2 = 15 -> 0
15 / 2 = 7 -> 1
7 / 2 = 3 -> 1
3 / 2 = 1 -> 1
1 / 2 = 0 -> 1

121 / 2 will give us 60.5, but since we do not care about the decimal part, we use the // operator which gives us the floor value of the division

if we run the following on a python shell,
int('11110010', 2), we get 242

"""

from stack1 import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num
print(div_by_2(242))