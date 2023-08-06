"""
CP1404 Practical - Austin Liandro
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MAX_NUMBER = 45
MIN_NUMBER = 1


def main():
    number_quick_pick = get_valid_quick_pick_number()
    picking_number(number_quick_pick)


def get_valid_quick_pick_number():
    """ Get the valid  number of quick pick number """
    number_quick_pick = int(input("How many quick picks? "))
    while number_quick_pick < 0:
        print("Number of quick pick can not less than 0")
        number_quick_pick = int(input("How many quick picks? "))
    return number_quick_pick


def picking_number(number_quick_pick):
    """ Processing the picking number """
    for line in range(number_quick_pick):
        rand_numbers = []
        for rand_number in range(NUMBERS_PER_LINE):
            rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while rand_number in rand_numbers:
                rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            rand_numbers.append(rand_number)
        rand_numbers.sort()
        print(" ".join(f"{rand_number:2}" for rand_number in rand_numbers))


main()
