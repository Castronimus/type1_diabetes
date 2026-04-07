from connection import DAO
import functions
from PIL import Image
from datetime import datetime

dao = DAO()

answer = None
while answer != "5":
    functions.menu()
    answer = input("\nChoose a number: ")
    if answer == "1":
        new_food = functions.create_food()
        if new_food is None:
            continue
        dao.create_food(new_food)
        print(f"{new_food[0].capitalize()} was successfully added ♦")
    elif answer == "2":
        table_food = dao.return_table("food_list")
        if not table_food:
            print("There is no food on the list!")
            print("Returning to menu...")
            continue
        while True:
            print("\nChoose the type of food you're searching for or just see all the food available:")
            print("\n1)All the food\n2)Cereal\n3)Fruit\n4)Pastry\n5)Dairy\n6)Candy\n7)Meat")
            type_food = input("\nType a number or 'q' to return to menu: ")
            if type_food == "q":
                print("Returning to menu...")
                break
            elif type_food == "1":
                filter = "all"
            elif type_food == "2":
                filter = "cereal"
            elif type_food == "3":
                filter = "fruit" 
            elif type_food == "4":
                filter = "pastry"
            elif type_food == "5":
                filter = "dairy"
            elif type_food == "6":
                filter = "candy"
            elif type_food == "7":
                filter = "meat"
            else:
                print("Please put a valid number or 'q' to return to menu")
                continue        
            display_food_list = functions.display_food_list(table_food, filter)
            if not display_food_list:
                print(f"There's no food with the {filter} category!")
                continue
            while True:
                show_image = False
                print("\nYou can type 'name_food' + show to show an image of the food, for example: \"boston_manjar show\"")
                print("This is the food available:", display_food_list)
                chosen_food = input("\nAdd a food typing its name or 'q' to go back: ").lower()
                if chosen_food == 'q':
                    break
                if " " in chosen_food:
                    food_split = chosen_food.split()
                    if len(food_split) == 2 and food_split[1] == "show":
                        chosen_food = food_split[0]
                        show_image = True
                food_row = functions.is_food_in_list(table_food, chosen_food)
                if not food_row:
                    print("That food is not in the list")
                    continue
                elif show_image:
                    try:
                        image = Image.open(f"images/{chosen_food}.PNG")
                        image.show()
                        print("I'LL SHOW THE IMAGE BECAUSE THE SECOND ARGUMENT IS show *-*")
                        print("Showing", chosen_food, "image...")
                        continue
                    except FileNotFoundError:
                        print("Image of that food doesn't exist !♣")
                        continue
                else:
                    food_data = functions.calculate_everything(food_row)
                    if food_data == 'q':
                        continue
                    dao.add_food(food_data[0], food_data[1], food_data[2], food_data[3], food_data[4], food_data[5], food_data[6])
                    print(f"{chosen_food.capitalize()} added to the cart ✓")
    elif answer == "3":
        # If there is food this will never give None, 0 is not None
        if dao.sum_column("calories") is None:
            print("There is not food in the cart !♣")
            print("Returning to menu...")
            continue
        no_food = False
        while True:
            if no_food:
                break
            cart_sum_carb = round(dao.sum_column("carbohydrates"),1)
            cart_sum_prot = round(dao.sum_column("proteins"),1)
            cart_sum_calo = round(dao.sum_column("calories"),1)
            cart_sum_fat = round(dao.sum_column("fat"),1)
            cart = dao.return_table("food_cart")
            print("\nCART:")
            print("")
            foods = []
            for food in cart:
                print(f"ID:{food[0]} | Name:{food[1]} | Amount:{food[3]} {food[4]} | Carbohydrates:{food[2]} | Proteins:{food[5]} | Calories:{food[6]} | Fat:{food[7]}")  
                foods.append(str(food[3]) + ' ' + food[4] + ' ' + food[1])            
            print(f"\nTotal carbohydrates: {cart_sum_carb}")
            print(f"Total proteins: {cart_sum_prot}")
            print(f"Total calories: {cart_sum_calo}")
            print(f"Total fat: {cart_sum_fat}")
            print("\n1)Delete specific food\n2)Delete all food\n3)Calculate")
            number = input("\nType a number or 'q' to return to menu: ")
            if number == "q":
                print("Returning to menu...")
                break
            elif number == "1":
                while True:
                    id_td = input("\nType the ID or 'q' to go back: ")
                    if id_td == 'q':
                        break
                    else:
                        try:
                            result = dao.find_id(int(id_td))
                            if result is None:
                                print("That ID doesn't exist !♣")
                            else:
                                dao.delete_cart(False, id_td)
                                print(f"ID:{id_td} was eliminated successfully  ♦")
                                if dao.sum_column("calories") is None:
                                    print("There is not food in the cart !♣")
                                    print("Returning to menu...")
                                    no_food = True
                                    break
                        except ValueError:
                            print("Type an ID! (an integer)")
                            continue
            elif number == "2":
                dao.delete_cart(True, None)
                print("All the food in the cart was eliminated successfully ♦")
                print("Returning to menu...")
                break
            elif number == "3":
                print("Total carbohydrates / 10")
                print(f"{cart_sum_carb} / 10 = {round(cart_sum_carb / 10, 1)} of insulin ✓")
                sugar_table = input("Do you want to see the sugar table?(yes): ")
                if sugar_table == "yes":
                    print("Showing table of blood sugar levels...")
                    image = Image.open("images/blood_sugar_table.PNG")
                    image.show()
                add_date = input("Do you want to record this food(s)?(yes): ")
                if add_date == "yes":
                    current_date = datetime.now()
                    date = current_date.strftime("%Y-%m-%d")
                    time = current_date.strftime("%H-%M")
                    foods = "|".join(foods)
                    dao.add_date(date,time,foods,cart_sum_carb,cart_sum_prot,cart_sum_calo,cart_sum_fat)
                    print("Food(s) recorded :D")           
    elif answer == "4":   
        while True:
            functions.other_options()
            option = input("\nChoose a number or 'q' to return to menu: ")
            if option == "q":
                print("Returning to menu...")
                break
            elif option == "1":
                functions.admin_access()
            elif option == "2":
                functions.my_foods()
    elif answer == "5":
        print("Bye")
        dao.connection.close()
    else:
        print("Choose a number from the menu !♣")
