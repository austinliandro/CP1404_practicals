"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- when a variable's value cannot be used or is incorrectly assigned.
2. When will a ZeroDivisionError occur?
- when a number is attempted to be divided by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- BELOW
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Error: Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
