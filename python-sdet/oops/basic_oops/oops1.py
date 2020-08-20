def purchase_mobile(price, brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    return total_price

def purchase_shoe(price, material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    return total_price

mobile_price = purchase_mobile(20000, "Apple")
shoe_price = purchase_shoe(200,"leather")
print("The total price of mobile is = ", mobile_price)
print("The total price of shoe is = ", shoe_price)

