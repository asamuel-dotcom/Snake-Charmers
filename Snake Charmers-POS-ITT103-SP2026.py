print("POS System")

#List of available products, price and quantity.
products = [
    ["Lotion", 250, 14],
    ["Hair Spray", 300, 9],
    ["Roll on", 200, 10],
    ["Rubbing Alcohol", 240, 12],
    ["Vase", 400, 11],
    ["Writing Book", 150, 14],
    ["Bath Soap", 200, 13],
    ["Hair Oil", 250, 9],
    ["Body Wash (S)", 400, 7],
    ["Body Wash (L)", 700, 9],
    ["Scalp Tonic", 1500, 6],
    ["Wipes", 150, 8]
]

cart = [] #Empty Cart.

#Product Selection.
choice = 0

while choice != -1:

    print("\nAvailable Products:") #This shows the products that are available for purchase.
    i = 0
    for product in products:
        print(i, product[0])
        i += 1

    choice = int(input("Enter product number or -1 to stop: ")) #This is where the cashier will enter the product number.

    if 0 <= choice <= i - 1:

        product = products[choice]
#Quantity selection.
        quantity = 0
        while quantity < 1 or quantity > product[2]:
            quantity = int(input(f"Enter quantity for {product[0]} (1-{product[2]}): "))
            if quantity < 1 or quantity > product[2]:
                print("Error! Quantity unavailable") #This will be printed if the quantity entered is unavailable.
# This adds and updates products and quantities in the cart.
        cart += [[product[0], quantity]] 
        product[2] -= quantity

        print("Product added to cart") #This will be printed when a product has been added to the cart.

    elif choice != -1:
        print("Invalid product number")

print("\nProducts in cart:") #This shows the products inside the cart without price.
for product in cart:
    print(f"{product[0]} - Quantity: {product[1]}")
#Remove items from cart
remove_product = int(input("Enter product to remove product or -1 to cancel: "))

count = 0

if 0 <= remove_product < count:
    for product in cart:
        count += 1
    removed_item = cart[remove_product]
    for product in products:
        if product[0] == removed_item[0]:
            product[2] += removed_item[1]
    del cart[remove_product]
    print(removed_item[0], "was removed from cart.")
else:
    print("Product isn't in the cart.")

#View Cart with total price
print("\nCart:")
for item in cart:
    price_per_unit = next(product[1] for product in products if product[0] == item[0])
    item_total = price_per_unit * item[1]
    print(f"{item[0]} - Quantity: {item[1]} - Total Price: {item_total}")
#Calculate subtotal
subtotal = 0

for item in cart:
    for product in products:
        if product[0] == item[0]:
            subtotal += product[1] * item[1]
print("\nSubtotal is:", subtotal)
#Calculate Tax
tax_rate = 0.10
total_price = subtotal * (1 + tax_rate)
print(f"Total price is: {total_price:.2f}")
#Calculate Discount
discount = 0

if total_price > 5000:
    discount = total_price * 0.05
    total_price -= discount
    print(f"Discount of 5% received: {discount:.2f}")
else:
    print("Not qualified for discount")
#Enter amount received
amount_received = float(input("\nEnter amount received: "))
print(f"Amount received is: {amount_received:.2f}")
#Calculate Change
change = amount_received - total_price
print(f"Change is: {change:.2f}")

#Receipt is being generated
print("GOODWILL SUPERCENTRE") #Name of Supermarket
print("=====================")

for products in cart:
    #Calculate unit price
    price_per_unit = 0
    for product in products:
        if products[0] == products[0]:
            price_per_unit = product[1]
    products_total = price_per_unit * products[1]
    print(f"{products[0]} - Quantity: {products[1]} - Total Price: {products_total:.2f}")

print("--------------------")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax (10%): {subtotal * tax_rate:.2f}")
if discount > 0:
    print(f"Discount: {discount:.2f}")
print(f"Total: {total_price:.2f}")
print(f"Amount Received: {amount_received:.2f}")
print(f"Change: {change:.2f}")
print("=====================")
print("THANK YOU FOR CHOOSING GOODWILL SUPERCENTRE!") #Thank you message
print("~COME AGAIN!~") #Thank you message continued
