import sqlite3
import sys

# --- Database Setup ---
def initialize_db():
    """Creates the database and table if they do not exist."""
    try:
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                expiry_date TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    finally:
        if conn:
            conn.close()

# --- CRUD Functions ---

def add_medicine():
    print("\n--- ADD NEW MEDICINE ---")
    name = input("Enter Medicine Name: ")
    try:
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
        
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medicines (name, price, quantity, expiry_date) VALUES (?, ?, ?, ?)", 
                       (name, price, qty, expiry))
        conn.commit()
        print(f"Success! {name} added to inventory.")
    except ValueError:
        print("Error: Price and Quantity must be numbers.")
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
    finally:
        if conn: conn.close()

def view_inventory():
    print("\n--- CURRENT INVENTORY ---")
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    
    if not rows:
        print("Inventory is empty.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<8} {'Expiry':<12}")
        print("-" * 60)
        for row in rows:
            # row index: 0=id, 1=name, 2=price, 3=qty, 4=expiry
            print(f"{row[0]:<5} {row[1]:<20} ${row[2]:<9.2f} {row[3]:<8} {row[4]:<12}")
    conn.close()

def search_medicine():
    print("\n--- SEARCH MEDICINE ---")
    search_term = input("Enter medicine name to search: ")
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    # Using SQL LIKE for partial matches
    cursor.execute("SELECT * FROM medicines WHERE name LIKE ?", ('%' + search_term + '%',))
    rows = cursor.fetchall()
    
    if not rows:
        print("No medicines found matching that name.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<8} {'Expiry':<12}")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} ${row[2]:<9.2f} {row[3]:<8} {row[4]:<12}")
    conn.close()

def update_medicine():
    view_inventory()
    print("\n--- UPDATE MEDICINE ---")
    try:
        med_id = int(input("Enter the ID of the medicine to update: "))
        new_price = float(input("Enter New Price: "))
        new_qty = int(input("Enter New Quantity: "))
        
        conn = sqlite3.connect('pharmacy.db')
        cursor = conn.cursor()
        # Check if ID exists first
        cursor.execute("SELECT * FROM medicines WHERE id=?", (med_id,))
        if cursor.fetchone() is None:
            print("Error: ID not found.")
        else:
            cursor.execute("UPDATE medicines SET price=?, quantity=? WHERE id=?", (new_price, new_qty, med_id))
            conn.commit()
            print("Medicine updated successfully.")
    except ValueError:
        print("Invalid input. Please enter numbers for ID, Price, and Quantity.")
    finally:
        if conn: conn.close()

def delete_medicine():
    view_inventory()
    print("\n--- DELETE MEDICINE ---")
    try:
        med_id = int(input("Enter the ID of the medicine to delete: "))
        confirm = input(f"Are you sure you want to delete ID {med_id}? (y/n): ")
        
        if confirm.lower() == 'y':
            conn = sqlite3.connect('pharmacy.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medicines WHERE id=?", (med_id,))
            if cursor.rowcount == 0:
                print("Error: ID not found.")
            else:
                conn.commit()
                print("Medicine deleted successfully.")
    except ValueError:
        print("Invalid ID format.")
    finally:
        if conn: conn.close()

# --- Main Program Flow ---
def main():
    initialize_db()
    while True:
        print("\n=== PHARMACY MANAGEMENT SYSTEM ===")
        print("1. Add Medicine")
        print("2. View Inventory")
        print("3. Search Medicine")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            search_medicine()
        elif choice == '4':
            update_medicine()
        elif choice == '5':
            delete_medicine()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()