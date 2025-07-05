import sqlite3
from secrets import choice

conn=sqlite3.connect("restaurant.db")

c=conn.cursor()
c.execute("PRAGMA foreign_keys=ON")
c.execute("""
    CREATE TABLE IF NOT EXISTS Menu (
      item_no integer PRIMARY KEY AUTOINCREMENT,
      name text,
      price integer,
      category text,
      portion text
      
    
    )





""")

conn.commit()

conn = sqlite3.connect("restaurant.db")

c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS orders (
      order_no integer PRIMARY KEY AUTOINCREMENT,
      item_no integer,
      quantity integer,
      total_price integer,
       
     FOREIGN KEY (item_No) REFERENCES Menu(item_No)

    )





""")

conn.commit()



conn = sqlite3.connect("restaurant.db")

c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS users (
      username text PRIMARY KEY,
      password text

    )





""")
conn.commit()

def sign_up():
    import re
    username = input("Enter new username: ")

    while True:
        password = input("Enter new password: ")
        confirm = input("Confirm password: ")

        if password != confirm:
            print("Passwords do not match. Please try again.\n")
            continue

        if (not re.search(r"[A-Za-z]", password) or
            not re.search(r"\d", password) or
            not re.search(r"[^A-Za-z0-9]", password)):
            print("Password must contain at least one letter, one number, and one symbol.\n")
            continue

        break
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Account created successfully!\n")
    except sqlite3.IntegrityError:
        print("Username already exists.\n")
    conn.close()



def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    conn = sqlite3.connect("restaurant.db")
    c=conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    user=c.fetchone()
    if user:
        print(f"Welcome, {username}\n")
        return True
    else:
        print("Login failed.\n")
        return False

def view_menu_categories():
    conn=sqlite3.connect("restaurant.db")
    c=conn.cursor()
    c.execute("SELECT DISTINCT category FROM Menu ORDER BY category")
    categories=c.fetchall()
    if not categories:
        print("No categories found")
        return
    print("\nAvailable Categories:")
    x=1
    for i in categories:
        c=i[0]
        print(f"{x}. {c}")
        x=x+1
    try:
        choice=int(input("\nEnter category number: "))
        if 1 <= choice <= len(categories):
           selected=categories[choice-1][0]
           view_category_items(selected)
        else:
            print("Invalid Choice")
    except:
        print("Invalid input")


def view_category_items(category):
    conn=sqlite3.connect("restaurant.db")
    c=conn.cursor()
    c.execute("SELECT item_no, name, price, portion FROM Menu WHERE category=?",(category,))
    items = c.fetchall()
    print(f"\n--- {category.upper()} MENU ---")
    for i in items:
        print(f"{i[0]}. {i[1]} ({i[3]} - Rs.{i[2]})")
    print("----------------------------------\n")

def add_item():
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    name = input("Enter item name : ")
    price = int(input("Enter price : "))
    category = input("Enter category : ")
    portion = input("Enter portion (Full,Half,Small,Large, etc,..) : ")
    c.execute("INSERT INTO Menu (name, price, category,portion) VALUES (?,?,?,?)", (name, price, category,portion))
    conn.commit()
    print("Item added.\n")

def update_price():
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    item_no = input("Enter item number: ")
    new_price = input("Enter new price: ")
    c.execute("UPDATE Menu SET price = ? WHERE item_No = ?", (new_price, item_no))
    conn.commit()
    print("\nPrice updated.\n")



def delete_item():
    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()
    item_no = input("Enter item number to delete: ")
    c.execute("DELETE FROM Menu WHERE item_No = ?", (item_no,))
    conn.commit()
    print("Item deleted.\n")

# ORDER FUNCTIONS
def place_order():
    view_menu_categories()
    item_id = int(input("Enter item number to order: "))
    quantity = int(input("Enter quantity: "))

    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()

    c.execute("SELECT name, price FROM Menu WHERE item_No = ?", (item_id,))
    result = c.fetchone()

    if result:
        name = result[0]
        price = result[1]
        total = price * quantity
        c.execute("INSERT INTO orders (item_No, quantity, total_price) VALUES (?, ?, ?)", (item_id, quantity, total))
        conn.commit()
        print(f"Order placed: {quantity} x {name} = Rs.{total}\n")
    else:
        print("Invalid item.")




def view_order_details():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()

    conn = sqlite3.connect("restaurant.db")
    c = conn.cursor()

    c.execute("""
        SELECT o.order_No, m.name, m.portion, o.quantity, o.total_price
        FROM orders o
        JOIN Menu m ON o.item_No = m.item_No
    """)

    orders = c.fetchall()
    if not orders:
        print("No order details found.\n")
    else:
        print("\n--- Order Details ---")
        for order in orders:
            print(f"Order No: {order[0]}, Item: {order[1]} ({order[2]}), Quantity: {order[3]}, Total: Rs.{order[4]}")
        print("----------------------\n")


def total_sales():
    conn = sqlite3.connect("restaurant.db")
    c.execute("SELECT SUM(total_price) FROM orders")
    total = c.fetchone()[0]
    if total:
        print(f"Total Sales: Rs.{total:.2f}\n")
    else:
        print("No sales yet.\n")



# MAIN MENU
while True:
    print("\nWelcome to KAUSAR Restaurant")
    print("1. Use as Customer")
    print("2. Manager Login")
    print("3. Manager Sign Up")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\nCustomer Menu:")
            print("1. View Menu")
            print("2. Place Order")
            print("3. Go Back")
            opt = input("Enter your choice: ")
            if opt == '1':
                view_menu_categories()
            elif opt == '2':
                place_order()
            elif opt == '3':
                break
            else:
                print("Invalid choice.")

    elif choice == '2':
        if login():
            while True:
                print("1. View Menu")
                print("2. Add Item")
                print("3. Update Price")
                print("4. Delete Item")
                print("5. Place Order")
                print("6. View Order Details")
                print("7. View Total Sales")
                print("8. Logout")
                opt = input("Enter your choice: ")
                if opt == '1':
                    view_menu_categories()
                elif opt == '2':
                    add_item()
                elif opt == '3':
                    update_price()
                elif opt == '4':
                    delete_item()
                elif opt == '5':
                    place_order()
                elif opt == '6':
                    view_order_details()
                elif opt == '7':
                    total_sales()
                elif opt == '8':
                    break
                else:
                    print("Invalid choice.")

    elif choice == '3':
        sign_up()
    elif choice == '4':
        print("Thank you.. Visit again.")
        break
    else:
        print("Invalid choice.")
