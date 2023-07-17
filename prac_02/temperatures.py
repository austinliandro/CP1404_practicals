"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """To call the function that we want."""
    menu, choice = user_input()
    user_choices(menu, choice)


def user_choices(menu, choice):
    """The function for the user to convert celsius to fahrenheit or otherwise."""
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def user_input():
    """The function to ask the user for choices"""
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    return menu, choice


main()
