def vat_calculator(price):
    return price + (price * 7/100)


user_input = int(input("Enter a price"))

result = vat_calculator(user_input)

print(result)
