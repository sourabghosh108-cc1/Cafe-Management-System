# Café Management System

customer_name = input("Enter customer name: ")

menu_item = input("Enter menu item: ").strip().lower()

quantity = int(input("Enter quantity: "))

if menu_item == "cappuccino":
    price = 5.00

elif menu_item == "latte":
    price = 4.50

elif menu_item == "espresso":
    price = 3.00

else:
    print("Sorry, the selected menu item is not available.")
    exit()

total_cost = price * quantity

print(
    f"Customer {customer_name} is buying {quantity} cups of "
    f"{menu_item}. Total cost: ${total_cost:.2f}"
)
