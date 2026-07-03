# Cafe-Management-System

## Overview

This project demonstrates fundamental Python programming concepts through a simple Café Management System. The program allows a customer to enter their name, choose a menu item, specify a quantity, and receive a calculated total cost.

The project was developed as part of a Programming Fundamentals discussion activity and showcases the practical application of variables, data types, arithmetic operations, assignment operators, user input, and control flow.

---

## Features

* Accepts customer information through user input.
* Supports multiple café menu items.
* Calculates total purchase cost automatically.
* Uses conditional statements to validate menu selections.
* Handles unavailable menu items gracefully.
* Displays formatted output with currency values.
* Demonstrates beginner-level Python programming concepts.

---

## Programming Concepts Demonstrated

### Variables

Variables store information entered by the user and data used by the program.

Examples:

```python
customer_name = "Emma"
menu_item = "cappuccino"
quantity = 2
price = 5.00
```

### Data Types

| Data Type        | Example        | Purpose                 |
| ---------------- | -------------- | ----------------------- |
| String (`str`)   | `"Cappuccino"` | Store menu item names   |
| Integer (`int`)  | `2`            | Store quantity ordered  |
| Float (`float`)  | `5.00`         | Store item prices       |
| Boolean (`bool`) | `True`         | Store item availability |

### Arithmetic Operators

Used to calculate the customer's total cost.

```python
total_cost = price * quantity
```

### Assignment Operators

Used to assign and update values.

```python
total_cost = 0
total_cost += price * quantity
```

### Control Flow

Conditional statements allow the program to make decisions.

```python
if menu_item == "cappuccino":
    price = 5.00
elif menu_item == "latte":
    price = 4.50
else:
    print("Item not available.")
```

---

## Source Code

```python
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
```

---

## Sample Run

### Input

```text
Enter customer name: Emma
Enter menu item: cappuccino
Enter quantity: 2
```

### Output

```text
Customer Emma is buying 2 cups of cappuccino. Total cost: $10.00
```

---

## How to Run

### Requirements

* Python 3.x

### Steps

1. Download or clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd cafe-management-system
```

3. Run the program.

```bash
python cafe_management.py
```

4. Follow the on-screen prompts.

---

## Possible Future Improvements

* Add more menu items.
* Apply discounts and taxes.
* Generate customer receipts.
* Store orders in files or databases.
* Track inventory automatically.
* Create a graphical user interface (GUI).
* Support multiple customer orders in a single session.

---

## Learning Outcomes

This project demonstrates:

* User input and output
* Python variables
* Data types (`str`, `int`, `float`, `bool`)
* Arithmetic operators
* Assignment operators
* Conditional statements (`if`, `elif`, `else`)
* String manipulation methods (`strip()`, `lower()`)
* Formatted output using f-strings

---

## Author

**Sourab Ghosh**

Programming Fundamentals – Unit 1 Discussion Activity

University of the People
