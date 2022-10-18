"""
emails
Estimate: 20 minutes
Actual: ? minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        isname = input(f"Is your name {name}? (Y/n)").lower()
        if isname == "n" or isname == "no":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    username = email.split("@")[0]
    name = " ".join(username.split(".")).title()
    return name


main()
