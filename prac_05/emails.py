"""
CP1404 Practical - Austin Liandro
Email to name dictionary
"""


def main():
    """to have the user input their email address to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ")
        if name_confirmation.upper() != "Y" and name_confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def name_from_email(email):
    """to extract an actual name from the email address"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
