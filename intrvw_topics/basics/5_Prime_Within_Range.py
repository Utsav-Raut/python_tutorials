# Prime numbers within a range

start = int(input('Enter the starting value '))
end = int(input('Enter the ending value '))

for i in range(start, end+1):
    flag = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)