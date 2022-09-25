
def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = conver_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_celsius_to_fehrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conver_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fehrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
