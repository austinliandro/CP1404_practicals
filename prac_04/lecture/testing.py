PASSWORD = "thor123"

password_input = input("Enter password: ")

if password_input in PASSWORD:  # it will say correct even only some PASSWORD is being input
    print("yes")
else:
    print("no")

if password_input == PASSWORD:   # need to fill the password correctly to print yes
    print("yes")
else:
    print("no")



tex
