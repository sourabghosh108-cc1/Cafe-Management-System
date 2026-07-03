# ☕ Cafe Management System

A simple Python-based Cafe Management System that demonstrates fundamental programming concepts such as variables, data types, arithmetic operations, assignment operators, user input, conditional statements, and formatted output.

This project was developed as part of the **Programming Fundamentals (CS 1101)** coursework and simulates a basic café ordering system where customers can select menu items, enter quantities, and receive a calculated bill.

---

## 🚀 Repository

[GitHub Repository](https://github.com/sourabghosh108-cc1/Cafe-Management-System?utm_source=chatgpt.com)

---

## 📖 Features

* Customer order processing
* Menu item selection
* Quantity-based billing
* Automatic total cost calculation
* Input validation for unavailable menu items
* Formatted receipt-style output
* Beginner-friendly Python code

---

## 🛠 Technologies Used

* Python 3
* Command Line Interface (CLI)

---

## 📂 Project Structure

```text
Cafe-Management-System/
│
├── cafe_management.py
├── Cafe_Management_System.exe
├── README.md
└── screenshots/
```

---

## 📥 Installation

### Method 1: Download the Windows Executable

If you do not want to install Python, you can use the pre-built executable.

Download:

[Google Drive Download (EXE)](https://drive.google.com/file/d/1njesBGrv3Lg3NDQ7Kn8iMDAxEgYtr9s5/view?usp=sharing&utm_source=chatgpt.com)

### Steps

1. Download the executable.
2. Extract it if it is inside a ZIP archive.
3. Double-click the `.exe` file.
4. Follow the on-screen instructions.

No Python installation is required.

---

## 📥 Installation from GitHub

### Clone the Repository

```bash
git clone https://github.com/sourabghosh108-cc1/Cafe-Management-System.git
```

Move into the project folder:

```bash
cd Cafe-Management-System

chmod +x *
```

---

## 🐍 Python Installation

### Windows

Download Python from:

[Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

Verify installation:

```bash
python --version
```

or

```bash
py --version
```

---

### Ubuntu / Debian

Install Python:

```bash
sudo apt update
sudo apt install python3
```

Verify:

```bash
python3 --version
```

Run the application:

```bash
python3 cm.py
```

---

### Fedora

Install Python:

```bash
sudo dnf install python3
```

Verify:

```bash
python3 --version
```

Run:

```bash
python3 cm.py
```

---

### Arch Linux

Install Python:

```bash
sudo pacman -S python
```

Verify:

```bash
python --version
```

Run:

```bash
python cm.py
```

---

## ▶ Running the Program

After cloning the repository:

```bash
python cm.py
```

or

```bash
python3 cm.py
```

---

## 💻 Example

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

## 📚 Programming Concepts Demonstrated

### Variables

```python
customer_name = "Emma"
quantity = 2
price = 5.00
```

### Data Types

| Data Type        | Example      | Usage             |
| ---------------- | ------------ | ----------------- |
| String (`str`)   | "Cappuccino" | Menu item name    |
| Integer (`int`)  | 2            | Quantity ordered  |
| Float (`float`)  | 5.00         | Item price        |
| Boolean (`bool`) | True         | Item availability |

### Arithmetic Operators

```python
total_cost = price * quantity
```

### Assignment Operators

```python
total_cost += price * quantity
```

### Conditional Statements

```python
if menu_item == "cappuccino":
    price = 5.00
elif menu_item == "latte":
    price = 4.50
else:
    print("Item not available")
```

---

## 🔮 Future Improvements

* Multiple item orders
* Discount support
* GST/Tax calculation
* Inventory management
* Receipt generation
* Database integration
* GUI using Tkinter
* Web version using Flask

---

## 🎓 Learning Outcomes

This project demonstrates:

* Python Basics
* User Input and Output
* Variables
* Data Types
* Arithmetic Operations
* Assignment Operators
* Conditional Statements
* String Manipulation
* Formatted Output
* Problem Solving

---

## 👨‍💻 Author

**Sourab Ghosh**

University of the People

Course: CS 1101 – Programming Fundamentals

---

## 📜 License

This project is intended for educational and learning purposes. Feel free to use, modify, and improve it for personal learning.
