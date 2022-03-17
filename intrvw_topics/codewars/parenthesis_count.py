# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parenthesis(string):
    count = 0
    flag = True
    for i in string:
        print(i)
        if i == '(':
            count = count + 1
        if i == ')':
            count = count - 1
        if count < 0:
            flag = False
            break
    if count == 0 and flag == True:
        return True
    else:
        return False

str = "hi())("
res = valid_parenthesis(str)
print(res)
