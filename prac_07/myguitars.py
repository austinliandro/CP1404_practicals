"""
CP1404 Practical 7 -
Code for client to use the guitar classes.

Estimate: 20 minutes
Actual:   30 minutes
"""
import csv
from prac_07.guitar import Guitar


def get_valid_int(prompt):
    """To get a valid integer"""
    is_finished = False
    while not is_finished:
        try:
            int_number = int(input(prompt))
            is_finished = True
            return int_number
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_float(prompt):
    """To get a valid float"""
    is_finished = False
    while not is_finished:
        try:
            int_number = float(input(prompt))
            is_finished = True
            return int_number
        except ValueError:
            print("Invalid input; enter a valid number")


def main():
    """ The main code for opening the guitar class."""
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            if len(row) == 3:  # Ensure each row has three values
                name, year, cost = row
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    new_name_guitar = input("New Guitar Name: ")
    new_year_guitar = get_valid_int("New Guitar Year: ")
    new_cost_guitar = get_valid_float("New Guitar Cost: ")
    new_guitar = Guitar(new_name_guitar, new_year_guitar, new_cost_guitar)
    guitars.append(new_guitar)

    with open('guitars.csv', 'w', newline='') as out_file:
        csv_writer = csv.writer(out_file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


main()