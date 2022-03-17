n = 3

upper = (10**(n)) - 1
lower = 1 + (upper // 10)

print(upper, lower)

num = 999
rev = 0

while(num > 0):
    rev = (rev * 10) + (num % 10)
    num = num // 10

print(rev)