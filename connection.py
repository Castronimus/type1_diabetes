import sqlite3
import sys
import os

def get_base_dir():
    """Get the base directory of the script or the executable."""
    if getattr(sys, 'frozen', False):
        # Running as a compiled executable
        return os.path.dirname(sys.executable)
    else:
        # Running as a .py script
        return os.path.dirname(os.path.abspath(__file__))

# Get the directory where the script is running
script_dir = get_base_dir()

# Create the "data" folder inside the script's directory
data_folder = os.path.join(script_dir, "data")
db_path = os.path.join(data_folder, "diabetes.db")

# Ensure the "data" directory exists
os.makedirs(data_folder, exist_ok=True)

print(f"Script running from: {os.path.abspath(__file__)}")
print(f"Script dir: {script_dir}")
print(f"Data folder will be: {data_folder}")

class DAO:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(db_path)  # SQLite database file
            cursor = self.connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS food_cart(id INTEGER PRIMARY KEY,
                              name TEXT, carbohydrates REAL, amount REAL, measurement TEXT,
                              proteins REAL, calories REAL, fat REAL);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS food_list(name TEXT PRIMARY KEY,
                              amount REAL, measurement TEXT, equals_to_this_carb REAL,
                              equals_to_this_prot REAL, equals_to_this_calo REAL,
                              equals_to_this_fat REAL, type_of_food TEXT);""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS dates(day DATE, time TEXT, foods TEXT,
                           carbohydrates REAL, proteins REAL, calories REAL, fat REAL)""")
            
        except sqlite3.Error as ex:
            print("The program couldn't connect to the DB D:, this is the error:", ex)
            sys.exit()

    def return_table(self, name_table):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM {name_table}"
        cursor.execute(query)
        table = cursor.fetchall()
        cursor.close()
        return table

    def return_row(self, name_row):
        cursor = self.connection.cursor()
        query = f"SELECT * FROM food_list WHERE name = ?"
        cursor.execute(query, (name_row,))
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def create_food(self, new_food):
        cursor = self.connection.cursor()
        query = """INSERT INTO food_list (name,amount,measurement,equals_to_this_carb,equals_to_this_prot,
                   equals_to_this_calo,equals_to_this_fat,type_of_food) 
                   VALUES (?,?,?,?,?,?,?,?);"""
        cursor.execute(query, new_food)
        self.connection.commit()
        cursor.close()

    def add_food(self, name, carbohydrates, amount, measurement, proteins, calories, fat):
        max_id = self.biggest_id()
        if max_id is None:
            max_id = 0
        else:
            max_id += 1
        cursor = self.connection.cursor()
        query = """INSERT INTO food_cart (id,name,carbohydrates,amount,measurement,proteins,calories,fat) 
                   VALUES (?,?,?,?,?,?,?,?);"""
        cursor.execute(query, (max_id, name, carbohydrates, amount, measurement, proteins, calories, fat))
        self.connection.commit()
        cursor.close()

    def add_date(self, day, time, foods, carbohydrates, proteins, calories, fat):
        cursor = self.connection.cursor()
        query = """INSERT INTO dates (day,time,foods,carbohydrates,proteins,calories,fat) 
                   VALUES (?,?,?,?,?,?,?);"""
        cursor.execute(query, (day, time, foods, carbohydrates, proteins, calories, fat))
        self.connection.commit()
        cursor.close()    

    def biggest_id(self):
        cursor = self.connection.cursor()
        query = "SELECT MAX(id) FROM food_cart"
        cursor.execute(query)
        max_id = cursor.fetchone()
        cursor.close()
        max_id = max_id[0]
        return max_id

    def sum_column(self, name_column, day=None):
        cursor = self.connection.cursor()
        if not day:
            query = f"SELECT SUM({name_column}) FROM food_cart"
            cursor.execute(query)
        else:
            query = f"SELECT SUM({name_column}) FROM dates WHERE day = ?"      
            cursor.execute(query, (day,))
        sum_c = cursor.fetchone()
        cursor.close()
        sum_c = sum_c[0]
        return sum_c

    def find_id(self, id_tf):
        cursor = self.connection.cursor()
        query = "SELECT id FROM food_cart WHERE id = ?"
        cursor.execute(query, (id_tf,))
        id_tf = cursor.fetchone()
        cursor.close()
        return id_tf

    def delete_cart(self, d_all, id_td):
        cursor = self.connection.cursor()
        if d_all is False:
            query = "DELETE FROM food_cart WHERE id = ?"
            cursor.execute(query, (id_td,))
        else:
            query = "DELETE FROM food_cart"
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def delete_list(self, name):
        cursor = self.connection.cursor()
        query = "DELETE FROM food_list WHERE name = ?"
        cursor.execute(query, (name,))
        self.connection.commit()
        cursor.close()

    def delete_date(self, day, time):
        cursor = self.connection.cursor()
        query = "DELETE FROM dates WHERE day = ? AND time = ?"
        cursor.execute(query, (day, time))
        self.connection.commit()
        cursor.close()

    def search_name(self, name):
        cursor = self.connection.cursor()
        query = "SELECT name FROM food_list WHERE name = ?"
        cursor.execute(query, (name,))
        name_exist = cursor.fetchone()
        cursor.close()
        if name_exist is None:
            name_exist = False
        else:
            name_exist = True
        return name_exist
    
    def modify_food(self, attribute, new, name):
        cursor = self.connection.cursor()
        query = f"UPDATE food_list SET {attribute} = ? WHERE name = ?"
        cursor.execute(query, (new, name))
        self.connection.commit()
        cursor.close()

    def return_dates(self, date1, date2=None):
        cursor = self.connection.cursor()
        if date2 is None:
            query = "SELECT * FROM dates WHERE day = ?"
            cursor.execute(query, (date1,))
        else:
            query = "SELECT * FROM dates WHERE day BETWEEN ? AND ?"
            cursor.execute(query, (date1, date2))
        table = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return table
