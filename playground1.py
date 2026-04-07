# def uwu():
#     while True:
#         name = input("OWO?: ")
#         if name  == "OWO":
#             print("OWOOOOOOOOOOOOOOOOOOOOOOOO")
#         elif name == "uwu":
#             return
#         elif name == "owito":
#             break
        
# owito = uwu()

# print(owito)

# twice = [("Nay", 28), ("JY", 27), ("Momo", 27)]
twice = []

def name_list(list):
    names = []
    for person in list:
        names.append(person[0])
    names.sort()
    return "|".join(names)    

print(name_list(twice))

if name_list(twice) == False:
    print("UWU")
else:
    print("xd")    






