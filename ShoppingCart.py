# Shopping cart program

items = []
prices = []
total = 0

while True:

    item = input("Enter an item you'd like to buy (Q/q to end shopping): ")
    if item.lower() == "q":
        break
    items.append(item)

    price = float(input(f"Enter the price of {item}: $"))
    prices.append(price)

for price in prices:
    total += round(price)

print("")
print("------------YOUR CART------------")
print("Shopping cart:", items)
print(f"Cart total: ${total}")
print("Thank you for shopping!")