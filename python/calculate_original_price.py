def calculate_original_price(discounted_price, discount_percent):
    original_price = discounted_price / (1 - discount_percent / 100)
    return original_price

discounted_price = float(input("Enter the discounted price: "))
discount_percentage = float(input("Enter the discount percentage: "))

original_price = calculate_original_price(discounted_price, discount_percentage)

print("Original price:", original_price)
