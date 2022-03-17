# Program to find the factorial of a number

# METHOD 1
# try:
#     num = int(input("Enter a number "))
#     res = 1
#     if res == 0 or res == 1:
#         print(res)
#     else:
#         for i in range(1, num+1):
#             res = res * i

#         print(res)

# except Exception as e:
#     print('Caught exception -> {}'.format(e))


# METHOD 2 using recursion
try:

    def rec_val(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * rec_val(num - 1)

    
    num = int(input('Enter a number '))

    result = rec_val(num)
    print('The recursion result is = {}'.format(result))

except Exception as e:
    print('Exception caught -> {}'.format(e))