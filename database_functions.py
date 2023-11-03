import sqlite3
def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE user(name TEXT NOT NULL, current_balance REAL NOT NULL);")
    cursor.execute("CREATE TABLE movements (category TEXT NOT NULL, description TEXT NOT NULL, value REAL NOT NULL, data TEXT NOT NULL, recurring_expense INTEGER)")
    
    conn.commit()
    cursor.close()

    

def insert_user(name_user, current_balance):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO user(name, current_balance)"
                   "VALUES('" + name_user + "', '" + str(current_balance) + "');")
    conn.commit()
    cursor.close()


def check_balance():
    results = {"balance": None, "total_expense": None, "largest_expense": None}
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Execute the query to retrieve the current balance
    cursor.execute("SELECT current_balance FROM user")
    
    # Fetch the first row if available
    row = cursor.fetchone()
    
    if row:
        # If there is a row, set the balance value
        results["balance"] = row[0]
    
    # Initialize total_expenses list and largest_expense to None
    total_expenses = []
    largest_expense = None
    
    # Execute the query to retrieve total expenses
    cursor.execute("SELECT value FROM movements WHERE category = 'g' ORDER BY value DESC")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    for row in rows:
        # Append each value to the total_expenses list
        total_expenses.append(row[0])
        
        # Update largest_expense if it's None or greater than the current value
        if largest_expense is None or row[0] > largest_expense:
            largest_expense = row[0]
    
    # Set the total_expense and largest_expense values
    results["total_expense"] = total_expenses
    results["largest_expense"] = largest_expense
    
    cursor.close()
    return results


def check_movements():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, description, value , data, category FROM movements")
    movements = cursor.fetchall()
    return movements


def select_and_fill_edit(rowid):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, description, value, data, recurring_expense FROM movements WHERE rowid = " + str(rowid))
    movements = cursor.fetchall()
    return movements


def edit_expense(rowid, name_user, value, data, recurring_expense):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movements SET description = '" + name_user + "', value = " + str(value) + ","
                   " data = '" + data + "', recurring_expense = " + str(recurring_expense) + " WHERE rowid = " + str(rowid))
    conn.commit()
    conn.close()


def search_movements(search):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, description, value, data , category  FROM movements WHERE description = '" + search + "'")
    movements = cursor.fetchall()
    return movements


def delete_expense(rowid):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, value FROM movements WHERE rowid = '" + str(rowid) + "'")
    result = cursor.fetchall()
    category = result[0][0]
    value = result[0][1]
    cursor.execute("SELECT current_balance FROM user")
    current_balance = cursor.fetchall()[0][0]
    if category == "f":
         new_balance = current_balance - float(value)
    else:
        new_balance = current_balance + float(value)
    cursor.execute("UPDATE user SET current_balance = " + str(new_balance))
    cursor.execute("DELETE FROM movements WHERE rowid = '" + str(rowid) + "'")
    conn.commit()
    conn.close()


def insert_expense(name, value, data, recurring_expense):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO movements(category, description, value, data, recurring_expense)"
                   "VALUES('g', '" + name + "', " + str(value) + ", '" + data + "', " + str(recurring_expense) + ")")
    cursor.execute("SELECT current_balance FROM user")
    current_balance = cursor.fetchall()[0][0]
    new_balance = current_balance - float(value)
    cursor.execute("UPDATE user SET current_balance = " + str(new_balance))
    conn.commit()
    conn.close()


def add_funds(name, value, data):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO movements(category, description, value, data)"
                   "VALUES('f', '" + name + "', " + str(value) + ", '" + data + "')")

    cursor.execute("SELECT current_balance FROM user")
    current_balance = cursor.fetchall()[0][0]
    new_balance = current_balance + float(value)
    cursor.execute("UPDATE user SET current_balance = " + str(new_balance))

    conn.commit()
    conn.close()


