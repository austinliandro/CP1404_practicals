MINIMUM_CHARACTER = 0

password = input("Enter your password: ")

while len(password) <= MINIMUM_CHARACTER:
    print("The password doesn't meet a minimum length set by a variable. Please try again.")
    password = input("Enter your password: ")

print("Your new password is:","*" * len(password),)
