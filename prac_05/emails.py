"""
emails
Estimate: 20 minutes
Actual: ? minutes
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split("@")[0]
    isname = input(f"Is your name {name}? (Y/n)").lower()

    if isname == "n" or isname == "no":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

print(email_to_name)