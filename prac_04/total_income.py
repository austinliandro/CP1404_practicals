"""
CP1404 Practical - Austin Liandro
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_number = int(input("How many months? "))

    for month in range(1, months_number + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report based on incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()