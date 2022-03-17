# Program to find the maximum of two numbers

try:
    number1 = int(input("Enter the first number "))
    number2 = int(input("Enter the second number "))

    # if number1 > number2:
    #     print('{0} is greater than {1}'.format(number1, number2))
    # elif number1 == number2:
    #     print('{0} is equal to {1}'.format(number1, number2))
    # else:
    #     print('{0} is greater than {1}'.format(number2, number1))

    # METHOD 2 using TERNARY OPERATOR
    # print(number1 if number1 >= number2 else number2) 


    # METHOD 3 using max function
    maximum = max(number1, number2)
    print(maximum)

except Exception as e:
    print('Caught exception -> {0}'.format(e))
