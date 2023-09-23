

total_price = 0

number_of_items = int(input("Enter number of items: "))

for item in range(1, number_of_items + 1):
    price = float(input(f"Enter the price of item {item}: $"))
    total_price += price

print(f"The total value for {number_of_items} items is: ${total_price:.2f}")

if price < 0:
    print("Try again! Price is not valid!")