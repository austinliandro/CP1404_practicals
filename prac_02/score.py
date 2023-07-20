LOWEST_SCORE = 0
HIGHEST_SCORE = 100
AVERAGE_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    score = get_user_scores()
    user_scores(score)


def user_scores(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("Invalid score")
    elif score >= EXCELLENT_SCORE:
        print("Excellent")
    elif score >= AVERAGE_SCORE:
        print("Passable")
    else:
        print("Bad")


def get_user_scores():
    score = float(input("Enter score: "))
    return score


main()
