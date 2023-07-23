MENU = "(G)et a valid score\n(P)rint\n(S)how stars\n(Q)uit"
LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT_SCORE = 90
AVERAGE_SCORE = 50


def main():
    """The function that we can call"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            choice, score = get_choice()
        elif choice == 'P':
            choice = user_score(score)
        elif choice == 'S':
            choice = show_choice(score)
        else:
            print("Invalid choice.")
            print(MENU)
            choice = input(">>> ").upper()
    print("Farewell.")


def get_choice():
    """To make the user input the score"""
    score = int(input("Your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Your score: "))
    print(MENU)
    choice = input(">>> ").upper()
    return choice, score


def user_score(score):
    """To check the score"""
    if score >= EXCELLENT_SCORE:
        message = "Excellent"
    elif score >= AVERAGE_SCORE:
        message = "Passable"
    else:
        message = "Bad"
    print(message)
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def show_choice(score):
    """to print the star"""
    for i in range(int(score)):
        print("*", end=" ")
    print()
    print(MENU)
    choice = input(">>> ").upper()
    return choice


main()
