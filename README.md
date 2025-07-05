# 🍽️ KAUSAR Restaurant Menu System – How to Use

This is a simple restaurant menu system made using **Python** and **SQLite**. It’s designed for two types of users:

- 👨‍🍳 Managers – Can manage menu items, place orders, and track sales
- 🍽️ Customers – Can view the menu and place orders easily

No coding knowledge is required to use it. Everything works through text-based menu prompts in the terminal.

---

## 💻 How to Run the Project

1. Make sure Python 3 is installed on your system.
2. Place the files `Mini Project.py` and `restaurant.db` in the same folder.
3. Run the Python file:
   ```
   python "Mini Project.py"
   ```
4. Follow the prompts in the terminal to navigate the menu.

---

## 🔐 Login & Sign Up

- Managers must sign up first using **Option 3: Manager Sign Up**
- Password must include:
  - At least one **letter**
  - At least one **number**
  - At least one **symbol** (e.g., @, #, !)

✅ Example password: `Admin@123`

---

## 👨‍💼 Manager Features

After logging in (Option 2), the following features are available:

| Option | Description                        |
|--------|------------------------------------|
| 1      | View full menu                     |
| 2      | Add new menu item                  |
| 3      | Update item price                  |
| 4      | Delete menu item                   |
| 5      | Place an order                     |
| 6      | View all order details             |
| 7      | View total sales                   |
| 8      | Logout                             |

---

## 🧑‍🍽️ Customer Features

Use **Option 1: Use as Customer** from the main menu.

Customers can:
- View the menu by category
- Place an order
- See the final total price

---

## 🗄️ Database Structure

All data is stored in **restaurant.db**:

- `Menu` table:
  - item_no, name, price, category, portion
- `orders` table:
  - order_no, item_no, quantity, total_price
- `users` table:
  - username, password

All tables are automatically created when the program runs.

---

## 🧪 Requirements

- Python 3.x
- No external libraries required (uses built-in `sqlite3`)

---

## 🎥 Demo

📺 Watch the demo video shared with the project submission.

---

## 👨‍💻 Author

**Ajmal Habeeb**  
Mini Project | July 2025
