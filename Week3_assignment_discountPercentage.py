# Calculate discount
def calculate_discount():
    price = input("Enter the original price: ")
    discount_percentage = input("Enter the percentage: ")

    discount_price = float(price) * (float(discount_percentage) / 100)
    final_price = float(price) - float(discount_price)
    
    if float(discount_percentage) >= 20:
        return final_price
    else:
        return price;

print (calculate_discount());
