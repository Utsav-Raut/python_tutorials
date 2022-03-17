# MAP function

def times2(num):
    return num ** 2

seq = [1, 2, 3, 4, 5]

res = list(map(times2, seq))
print(res)

# Using lambda instead of creating a separate function

res = list(map(lambda var: var ** 2, seq))
print(res)



# USING FILTER FUNCTION

filt_res = list(filter(lambda num: num%2 == 0, seq))
print(filt_res)