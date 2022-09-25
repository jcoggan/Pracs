MIN_LENGTH = 10

def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Password: ")
    return password


main()
