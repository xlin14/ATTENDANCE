import sqlite3

DATABASE_NAME = "dragon.db"

def view_table_data(table_name):
    """Connects to the DB and prints all data from the specified table."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # 1. Fetch the column names (fields)
        # This is important so you know what you are reading/editing
        cursor.execute(f"PRAGMA table_info({table_name});")
        column_info = cursor.fetchall()
        column_names = [info[1] for info in column_info]
        
        if not column_names:
            print(f"❌ Error: Table '{table_name}' does not exist or has no columns.")
            return

        # 2. Fetch all data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # 3. Print the results
        print(f"\n--- Data in Table: {table_name} ---")
        print(" | ".join(column_names))
        print("-" * (sum(len(c) for c in column_names) + len(column_names) * 3))

        if not rows:
            print(f"Table '{table_name}' is empty.")
            return

        for row in rows:
            # Simple way to print the data
            print(" | ".join(str(item) for item in row))
            
    except sqlite3.Error as e:
        print(f"\n❌ An SQLite error occurred while reading: {e}")
    finally:
        if conn:
            conn.close()

# -------------------------------------------------------------

def edit_field_in_table(table_name):
    """Allows the user to update a specific field in a record."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Prompt the user for the necessary data
        view_table_data(table_name) # Show data first so the user can choose the ID
        
        record_id = input("\nEnter the ID of the record you want to edit: ")
        field_name = input("Enter the NAME of the field (column) you want to change: ")
        new_value = input(f"Enter the NEW VALUE for the '{field_name}' field: ")
        
        # Ensure ID is an integer for the WHERE clause
        try:
            int(record_id)
        except ValueError:
            print("\n❌ Error: Record ID must be an integer.")
            return

        # Use a placeholder (?) for the new value to safely handle different data types
        # and prevent SQL injection.
        update_sql = f"UPDATE {table_name} SET {field_name} = ? WHERE id = ?;"

        # Execute the update command
        cursor.execute(update_sql, (new_value, record_id))
        
        # Commit the transaction to save the changes
        conn.commit()
        
        if cursor.rowcount == 0:
             print(f"\n⚠️ Warning: No record with ID {record_id} was updated.")
        else:
             print(f"\n✅ Success! Record ID {record_id} updated. The field '{field_name}' is now '{new_value}'.")
             
             # Show the updated data
             view_table_data(table_name) 

    except sqlite3.Error as e:
        print(f"\n❌ An SQLite error occurred while updating: {e}")
    finally:
        if conn:
            conn.close()

# -------------------------------------------------------------

if __name__ == "__main__":
    
    table_name = input("Enter the name of the table you want to interact with: ")
    
    # First, view the data (READ)
    print("\n--- STEP 1: READING DATA ---")
    view_table_data(table_name)

    # Second, edit a field (EDIT)
    print("\n--- STEP 2: EDITING DATA ---")
    edit_field_in_table(table_name)