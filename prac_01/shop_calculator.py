"""
Shop Calculator

A shop requires a small program that would allow them to quickly work out
the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of
each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that
total before the amount is displayed on the screen.

pseudocode:

total_price = 0
get number_of_items
until number_of_items > 0
    get number_of_items
repeat number_of_items times
    get item_price
    total_price = total_price + item_price
if total_price > 100
    total_price = total_price - (total_price * 0.1)
display total_price
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range (number_of_items):
    item_price = float(input("Price of item: $"))
    while item_price < 0:
        print("Invalid price")
        item_price = float(input("Price of item: %"))
    total_price += item_price
if total_price > 100:
    total_price -= (total_price * 0.1)
print(f"Total price for {number_of_items} is ${total_price:.2f}")
