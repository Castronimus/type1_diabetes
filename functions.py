from connection import DAO
dao = DAO()

def menu():
    print("\n||||||Menu||||||")
    print("\n1)Create food\n2)Add Food\n3)See my cart\n4)Other options\n5)Exit")

def create_food(): 
    while True:
        print("\nCreating food!")
        name = create_name()
        if not name:
            return
        elif name == "*":
            break
        while True:
            print("\nMeasurement")
            measurement = create_measurement()
            if not measurement:
                return
            elif measurement == "*":
                break
            while True:
                print("\nAmount")
                amount = create_amount(measurement)
                if not amount:
                    return
                elif amount == "*":
                    break
                while True:
                    print("\nCarbohydrates")
                    carb = create_carbohydrates(amount,measurement)
                    if not carb:
                        return
                    elif carb == "*":
                        break
                    while True:
                        print("\nProteins")
                        prot = create_proteins(amount,measurement)
                        if not prot:
                            return
                        elif prot == "*":
                            break  
                        while True:
                            print("\nCalories")
                            cal = create_calories(amount,measurement)
                            if not cal:
                                return
                            elif cal == "*":
                                break  
                            while True:
                                print("\nFat")
                                fat = create_fat(amount,measurement)
                                if not fat:
                                    return
                                elif fat == "*":
                                    break
                                while True:
                                    type_food = create_type_of_food()
                                    if not type_food:
                                        return
                                    elif type_food == "*":
                                        break                      
                                    return [name, amount, measurement, carb, prot, cal, fat, type_food]
                                
def create_name():
    while True:
        name = input("\nType the name of the item food: ").lower().strip()
        if name == 'q':
            return
        elif name == '*':
            return "*"
        elif " " in name:
            print("You can't put whitespaces")
            continue
        name_exist = dao.return_row(name)
        if name_exist:
            print("That food name already exists, please put another one !♣")
            continue
        return name        

def create_measurement():
    while True:
        print("\n1)Gram(s)\n2)Unit(s)")
        measurement = input("\nType a number: ")
        if measurement == "q":
            return
        elif measurement == "*":
            return "*"
        elif measurement == "1":
            measurement = "gram(s)"
        elif measurement == "2":
            measurement = "unit(s)"
        else:
            print("Please choose an option!") 
            continue 
        return measurement                               

def create_amount(measurement):
     while True:
        try:
            print(f"\nV {measurement} = ?(carb/prot/cal/fat)")
            amount = input(f"\nV: ")
            if amount == 'q':
                return 
            elif amount == '*':
                return "*"
            amount = float(amount)
            if amount <= 0:
                print("The measurement can't be 0 or below!")
                continue
            return amount
        except ValueError:
            print("Please put a number !♣") 


def create_carbohydrates(amount, measurement):
     while True:
        try:
            print(f"\n{amount} {measurement} = W carbohydrates")
            carb = input("\nW: ")
            if carb == 'q':
                return
            elif carb == '*':
                return "*"
            carb = float(carb)
            print(f"\n{amount} {measurement} = {carb} Carbohydrates ♦")
            return carb
        except ValueError:
            print("Please put a number !♣")  

def create_proteins(amount, measurement):
     while True:
        try:
            print(f"\n{amount} {measurement} = X Proteins")
            prot = input("\nX: ")
            if prot == 'q':
                return 
            elif prot == '*':
                return "*"
            prot = float(prot)
            print(f"\n{amount} {measurement} = {prot} Proteins ♦")
            return prot
        except ValueError:
            print("Please put a number !♣")  

def create_calories(amount, measurement):
     while True:
        try:
            print(f"\n{amount} {measurement} = Y Calories")
            cal = input("\nY: ")
            if cal == 'q':
                return
            elif cal == '*':
                return "*"
            cal = float(cal)
            print(f"\n{amount} {measurement} = {cal} Calories ♦")
            return cal
        except ValueError:
            print("Please put a number !♣") 

def create_fat(amount, measurement):
     while True:
        try:
            print(f"\n{amount} {measurement} = Z Fat")
            fat = input("\nZ: ")
            if fat == 'q':
                return
            elif fat == '*':
                return "*"
            fat = float(fat)
            print(f"\n{amount} {measurement} = {fat} Fat ♦")
            return fat
        except ValueError:
            print("Please put a number !♣")            

def other_options():
    print("\n|||Other options|||")
    print("\n1)Admin\n2)My foods")

def admin_options():
    print("\n|||||||||Admin options|||||||||")
    print("\n1)Delete specific food of the list\n2)Modify specific food of the list")

def admin_access():
    dao = DAO()
    while True:
        password = input("Enter the pass or 'q' to go back: ")
        if password == "twice":
            print("The password is correct!")
            while True:
                admin_options()
                admin = input("\nChoose a number or 'q' to go back: ")
                if admin == "1":
                    while True:
                        food_list = dao.return_table("food_list")                        
                        if not food_list:
                            print("There is no food on the list !♣")
                            print("Returning to admin options...")
                            break
                        display_food = display_food_list(food_list, "all")
                        print("\nThis is the food in list:", display_food)
                        delete = input("\nType the name of the food you want to delete or 'q' to go back: ").lower().strip()
                        if delete == 'q':
                            break
                        else:
                            result = is_food_in_list(food_list, delete)
                            if result is False:
                                print("That food name doesn't exist in the list")
                                continue
                            while True:
                                sure = input(f"Are you sure you want to delete the food {result[0].capitalize()}?(yes/no):").lower()
                                if sure == "yes":
                                    dao.delete_list(result[0])
                                    print(f"{result[0].capitalize()} was successfully deleted of the list")
                                    break
                                elif sure == "no":
                                    print("Ok! going back to the list...")
                                    break
                                else:
                                    print("Choose an option please")
                elif admin == "2":
                     while True:
                        food_list = dao.return_table("food_list")
                        display_food = display_food_list(food_list, "all")
                        if not food_list:
                            print("There is no food on the list !♣")
                            print("Returning to admin options...")
                            break
                        print("\nThis is the food in list:", display_food)
                        food_modify = input("\nType the name of the food you want to modify or 'q' to go back: ").lower().strip()
                        if food_modify == 'q':
                            break
                        else:
                            food = dao.return_row(food_modify)
                            if not food:
                                print("That food name doesn't exist in the list")
                                continue
                            while True:
                                food = dao.return_row(food_modify)
                                print("\nModyfing", food[0])
                                print(f"\nAmount and measurement:{food[1]} {food[2]}|Carbohydrates:{food[3]}|Proteins:{food[4]}|Calories:{food[5]}|Fat:{food[6]}|Type:{food[7].capitalize()}")
                                print("\nWhat do you want to modify?")
                                print("\n1)Name\n2)Amount\n3)Measurement\n4)Carbohydrates\n5)Proteins\n6)Calories\n7)Fats\n8)Type of food")
                                modify = input("\nChoose a number or 'q' to go back: ")
                                if modify == "q":
                                    break  
                                elif modify == "1":
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_name = create_name()
                                        if new_name is None or new_name == '*':
                                            break
                                        dao.modify_food("name",new_name,food[0])
                                        food_modify = new_name
                                        print(f"Name changed to {new_name} successfully!")
                                        break
                                elif modify == "2":
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_amount = create_amount(food[2])
                                        if new_amount is None or new_amount == '*':
                                            break
                                        elif new_amount == food[1]:
                                            print(f"The food already had {new_amount} amount !♣")
                                            continue                                        
                                        dao.modify_food("amount",new_amount,food[0])
                                        print(f"Amount changed to {new_amount} successfully!")
                                        break
                                elif modify == '3':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_measurement = create_measurement()
                                        if new_measurement is None or new_measurement == '*':
                                            break
                                        elif new_measurement == food[2]:
                                            print(f"The food already had {new_measurement} measurement !♣")
                                            continue
                                        dao.modify_food("measurement",new_measurement,food[0])
                                        print(f"Measurement changed to {new_measurement} successfully!")
                                        break
                                elif modify == '4':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_carbohydrates = create_carbohydrates(food[1],food[2])
                                        if new_carbohydrates is None or new_carbohydrates == '*':
                                            break
                                        elif new_carbohydrates == food[3]:
                                            print(f"The food already had {new_carbohydrates} carbohydrates !♣")
                                            continue
                                        dao.modify_food("equals_to_this_carb",new_carbohydrates,food[0])
                                        print(f"Carbohydrates changed to {new_carbohydrates} successfully!")
                                        break   
                                elif modify == '5':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_proteins = create_proteins(food[1],food[2])
                                        if new_proteins is None or new_proteins == '*':
                                            break
                                        elif new_proteins == food[4]:
                                            print(f"The food already had {new_proteins} proteins !♣")
                                            continue                                        
                                        dao.modify_food("equals_to_this_prot",new_proteins,food[0])
                                        print(f"proteins changed to {new_proteins} successfully!")
                                        break
                                elif modify == '6':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_calories = create_calories(food[1],food[2])
                                        if new_calories is None or new_calories == '*':
                                            break
                                        elif new_calories == food[5]:
                                            print(f"The food already had {new_calories} calories !♣")
                                            continue                                   
                                        dao.modify_food("equals_to_this_calo",new_calories,food[0])
                                        print(f"Calories changed to {new_calories} successfully!")
                                        break     
                                elif modify == '7':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_fat = create_fat(food[1],food[2])
                                        if new_fat is None or new_fat == '*':
                                            break
                                        elif new_fat == food[6]:
                                            print(f"The food already had {new_fat} fat !♣")
                                            continue
                                        dao.modify_food("equals_to_this_fat",new_fat,food[0])
                                        print(f"Fat changed to {new_fat} successfully!")
                                        break                   
                                elif modify == '8':
                                    while True:
                                        print("Type 'q' or '*' to go back")
                                        new_type_food = create_type_of_food()
                                        if new_type_food is None or new_type_food == '*':
                                            break
                                        elif new_type_food == food[7]:
                                            print(f"The food already had {new_type_food} as type of food !♣")
                                            continue
                                        dao.modify_food("type_of_food",new_type_food,food[0])
                                        print(f"type_food changed to {new_type_food} successfully!")
                                        break   
                                else:
                                    print("Please choose a number !♣")                                                                                                                                                                             
                elif admin == "q":
                    break
        elif password == 'q':
            return
        else:
            print("Incorrect password   !♣")

def date_information(just_date):
    while True:
        try:
            dates = dao.return_dates(just_date)
            if not dates:
                print("There is no foods registered that day !♣︎")
                break 
            print("\nDate:",just_date)
            print("")
            for date in dates:
                print(f"{date[1]}: {date[2]} = Carb:{date[3]}|Prot:{date[4]}|Cal:{date[5]}|Fat:{date[6]}")
            print("\nTotal Calories:",round(dao.sum_column("calories",just_date),2))
            print("Total Proteins:",round(dao.sum_column("proteins",just_date),2))    
            print("Total Carbohyrates:",round(dao.sum_column("carbohydrates",just_date),2))    
            print("Total Fat:",round(dao.sum_column("fat",just_date),2))    
            back = input("\n'q' to go back: ")
            if back == "q":
                return
        except Exception:
            print("Please type a valid date (e.g. 2024-02-14)")
            break
        
def my_foods():
    from datetime import datetime, timedelta
    # Get the current date including all, even the time
    all_date_info = datetime.now()
     # Extract just the date from all_date_info (e.g. 01/01/2024)
    just_date_today = all_date_info.strftime("%Y-%m-%d")
    # To Extract just the day from all_date_info use: just_day = all_date_info.strftime("%A") (e.g. Sunday, Monday...)
    while True:
        print("\nMy foods ◘")
        print("\n1)Today\n2)Week\n3)Date")
        choice = input("\nChoose a number or 'q' to go back: ")
        if choice == "q":
            break     
        elif choice == "1":
            while True:
                hours = []
                dates = dao.return_dates(just_date_today)
                if not dates:
                    print("There is no foods registered today !♣︎")
                    break 
                print("\nToday is",just_date_today)
                print("")
                for date in dates:
                    hours.append(date[1])
                    print(f"{date[1]}: {date[2]} = Carb:{date[3]}|Prot:{date[4]}|Cal:{date[5]}|Fat:{date[6]}")
                print("\nTotal Calories:",round(dao.sum_column("calories",just_date_today),2))
                print("Total Proteins:",round(dao.sum_column("proteins",just_date_today),2))    
                print("Total Carbohyrates:",round(dao.sum_column("carbohydrates",just_date_today),2))    
                print("Total Fat:",round(dao.sum_column("fat",just_date_today),2))    
                del_hour = input("\nType the hour of a register to delete it(e.g. 14-11) or 'q' to go back: ")
                if del_hour == "q":
                    break
                elif del_hour in hours:
                    dao.delete_date(just_date_today,del_hour)
                    print(f"Register(s) of today with the hour {del_hour} deleted sucessfully ♦")
                else:
                    print("Put a valid hour! (e.g 08-59)")    
        elif choice =="2":
            dates_week = []
            monday = all_date_info
            while monday.strftime("%A") != "Monday":
                dates_week.append(monday)  
                monday = monday - timedelta(days=1)
            dates_week.append(monday)
            dates_week.reverse()
            monday = monday.strftime("%Y-%m-%d")
            # Now we have monday and the actual date(just_date_today) now we just need an SQL statement
            while True:
                try:
                    print("\nPick a day of the current week")
                    print("\n1)Monday\n2)Tuesday\n3)Wednesday\n4)Thursday\n5)Friday\n6)Saturday\n7)Sunday")
                    pick = input("\nType a day or 'q' to go back: ")
                    if pick == "q":
                        break
                    elif pick == "1":
                        information = date_information(dates_week[0].strftime("%Y-%m-%d"))
                    elif pick == "2":
                        information = date_information(dates_week[1].strftime("%Y-%m-%d"))
                    elif pick == "3":
                        information = date_information(dates_week[2].strftime("%Y-%m-%d"))
                    elif pick == "4":
                        information = date_information(dates_week[3].strftime("%Y-%m-%d"))
                    elif pick == "5":
                        information = date_information(dates_week[4].strftime("%Y-%m-%d"))
                    elif pick == "6":
                        information = date_information(dates_week[5].strftime("%Y-%m-%d"))
                    elif pick == "7":
                        information = date_information(dates_week[6].strftime("%Y-%m-%d"))
                    else:
                        print("Type a day or 'q' to go back please")
                except IndexError:
                    print("That day of the week doesn't exist yet !♣")
        elif choice == "3":
            # I have to validate it
            while True:
                #try:
                type_date = input("\nType a date (e.g. 2024-03-19) or 'q' to go back: ")
                if type_date == "q":
                    break
                date_information(type_date)
        else:
            print("Please choose a number")

def create_type_of_food():
    while True:                                                
        print("\nType of food:")
        print("\n1)Cereal\n2)Dairy\n3)Fruit\n4)Pastry\n5)Candy\n6)Meat")
        type_of_food = input("\nChoose a number: ")
        if type_of_food == 'q':
            return
        elif type_of_food == '*':
            return 'break'
        elif type_of_food == "1":
            type_food = "cereal"
        elif type_of_food == "2":
            type_food = "dairy"
        elif type_of_food == "3":
            type_food = "fruit"
        elif type_of_food == "4":
            type_food = "pastry"
        elif type_of_food == "5":
            type_food = "candy"
        elif type_of_food == "6":
            type_food = "meat"
        else:
            print("Please choose an option")
            continue
        print("\nThen the type of food is",type_food.capitalize())         
        return type_food



def display_food_list(table_food, filter):
    list_food = []
    for food in table_food: 
        if food[7] == filter or filter == "all":
            list_food.append(food[0])
    list_food.sort()
    return "|".join(list_food)
   

def is_food_in_list(table_food, chosen_food):
    for food in table_food:
        if food[0] == chosen_food:
            return food
    return False

def calculate_everything(chosen_food):
    while True:
        try:
            # chosen_food is a food object from the food_list table, which contains name, amount, measurement, equals_to_this_carb, etc...
            # How many gram(s)/unit(s) of name_food 
            amount = input(f"\nHow many {chosen_food[2]} of {chosen_food[0]} or 'q' to return to the list of food: ")
            if amount == 'q':
                return 'q'
            calculate_carb = round(float(amount) * chosen_food[3] / chosen_food[1], 1)          
            calculate_prot = round(float(amount) * chosen_food[4] / chosen_food[1], 1)
            calculate_calo = round(float(amount) * chosen_food[5] / chosen_food[1], 1)
            calculate_fat = round(float(amount) * chosen_food[6] / chosen_food[1], 1)
            print(f"This adds {calculate_carb} carbohydrates")
            print(f"This adds {calculate_prot} proteins")
            print(f"This adds {calculate_calo} calories")
            print(f"This adds {calculate_fat} fat")
            return [chosen_food[0], calculate_carb, amount, chosen_food[2], calculate_prot, calculate_calo, calculate_fat]
        except ValueError:
            print("Please put a number  !♣")
            continue
