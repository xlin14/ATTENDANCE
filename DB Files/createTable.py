import sqlite3

# Define the database file name directly
DATABASE_NAME = "dragon.db"

def create_table_in_dragon_db():
    """
    Connects to 'dragon.db' and creates a new table with a 
    user-specified name and a standard schema.
    """
    
    # 1. Get the desired table name from the user
    table_name = input("Enter the desired name for the new table in 'dragon.db': ")
    
    # Simple validation for table name (best practice for dynamic SQL)
    if not table_name.replace('_', '').isalnum():
        print("Error: Table name can only contain alphanumeric characters and underscores.")
        return

    # 2. Define the SQL command to create the table
    # We use f-strings to securely insert the table name into the command.
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT,
        level INTEGER
    );
    """

    conn = None
    try:
        # Connect to the database file
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Execute the SQL command
        cursor.execute(create_table_sql)
        
        # Commit the transaction to make the changes permanent
        conn.commit()
        
        print(f"\n✅ Success! Table '{table_name}' created in database '{DATABASE_NAME}'.")
        print("\nTable Schema (Example for 'dragon.db'):")
        print("-------------")
        print("| id (INTEGER PRIMARY KEY) |")
        print("| name (TEXT NOT NULL)     |")
        print("| type (TEXT)              |")
        print("| level (INTEGER)          |")
        print("-------------")

    except sqlite3.Error as e:
        print(f"\n❌ An SQLite error occurred: {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table_in_dragon_db()
    