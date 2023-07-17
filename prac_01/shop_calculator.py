DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1
total_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = float(input("Price of items: "))
    total_price += price_of_items

if total_price > DISCOUNT_THRESHOLD:
    discount_price = total_price * DISCOUNT
    total_price = total_price - discount_price
print(f"Total price for {number_of_items} is ${total_price:.2f}")
