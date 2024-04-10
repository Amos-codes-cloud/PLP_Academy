def calculate_original_price(discounted_price, discount_percent):
    original_price = discounted_price / (1 - discount_percent / 100)
    return original_price

# Prompting the user for input
discounted_price = float(input("Enter the discounted price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the original price
original_price = calculate_original_price(discounted_price, discount_percentage)

# Printing the original price
print("Original price:", original_price)
