def larget_palindrom(num_of_digits):
    
    upper_limit = (10 ** (num_of_digits)) - 1
    lower_limit = 1 + (upper_limit // 10)

    max_product = 0
    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j

            if(product < max_product):
                break

            result = product
            reversed = 0

            while(result > 0):
                reversed = (reversed * 10) + (result % 10)
                result = result // 10
            
            if(reversed == product and product > max_product):
                max_product = product
    return max_product

n = 3
res = larget_palindrom(3)
print(res)