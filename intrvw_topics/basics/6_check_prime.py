# Program to check if a number is prime or not

num = int(input('Enter the number to be checked for prime '))

flag = 0
for i in range(2, (num // 2) + 1):
    if num > 1:
        if num % i == 0:
            flag = 1
            break

if flag == 0:
    print('Prime')
else:
    print('Not a prime')