"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MIN_SALES = 0
UNDER_SALES = 1000
DISCOUNT = 0.1
SECOND_DISCOUNT = 0.15

sales = float(input("Enter sales: $"))
while sales >= MIN_SALES:
    if sales < UNDER_SALES:
        bonus = sales * DISCOUNT
    else:
        bonus = sales * SECOND_DISCOUNT
    print(f"Your bonus is ${bonus}.")
    sales = float(input("Enter sales: $"))
print("Invalid sales")