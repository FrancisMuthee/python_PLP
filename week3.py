'''
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
 The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
   If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
Print the final price after applying the discount, or if no discount was applied, print the original price.
'''

def calculate_discount(price, discount_perrcent):
    if discount_perrcent >=20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price
    
   
# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price
print("Final price after applying the discount: ", final_price)

