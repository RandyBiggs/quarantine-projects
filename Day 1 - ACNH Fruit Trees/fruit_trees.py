import time

# {Name, Native, Quantity}
trees = [{"name": "Apple", "native": False, "quantity": 0}, {"name": "Pear", "native": False, "quantity": 0},
         {"name": "Peach", "native": False, "quantity": 0}, {"name": "Cherry", "native": False, "quantity": 0},
         {"name": "Coconut", "native": False, "quantity": 0}, {"name": "Orange", "native": False, "quantity": 0}]

# Total value of fruit divided by 72 hours (Assuming trees refresh every 3 days)
native_value = 300
foreign_value = 1500
coconut_value = 500


def print_intro():
    print("\n[Animal Crossing: New Horizons - Fruit Tree Calculator]\n")
    time.sleep(1.3)
    print("Use this calculator to determine the passive income you would receive from a given number of fruit trees"
          " on your island. \nType one of the following options below:\n")


def get_menu_choice():
    menu_choice = input("[Native Fruit]  [Set Quantity]  [Help]  [Calculate]\n\n")
    return menu_choice


def set_native():
    choice = input("Which fruit is native to your island?\n").lower()
    if choice[-1] == 's':
        choice = choice[0:-1]
    while choice not in [t["name"].lower() for t in trees]:
        print("Unrecognized input. Please try again.")
        choice = input().lower()
        if choice[-1] == 's':
            choice = choice[0:-1]
    for t in trees:
        if t["name"].lower() == choice.lower():
            t["native"] = True
            print("\nSet {} as your island's Native Fruit!\n".format(choice.title()))


def set_quantity():
    fruit = input("Which fruit tree quantity are you updating?\n").lower()
    if fruit[-1] == 's':
        fruit = fruit[0:-1]
    quant = int(input("How many {} trees?\n".format(fruit)))
    for tree in trees:
        if tree["name"].lower() == fruit:
            tree["quantity"] = quant


def print_help():
    print("Menu options should be typed as they appear. Capitalization does not matter, but spelling does.\n\n"
          "[Native Fruit]: Used to define which fruit is native to your island for value calculations\n"
          "[Set Quantity]: Used to specify how many of the type of tree you will be collecting\n"
          "[Calculate]: Calculate the total Bells per 3 Days\n"
          "[Quit] Exit the application\n\n")


def calculate_income():
    income = 0
    for tree in trees:
        if tree["native"]:
            print(tree["name"] + ": " + str(native_value * tree["quantity"]) + " Bells")
            income += native_value * tree["quantity"]
        else:
            income += foreign_value * tree["quantity"]
            print(tree["name"] + ": " + str(foreign_value * tree["quantity"]) + " Bells")
    print("You will earn a total of: {} Bells every 3 Days!".format(income))
    return income


def __main__():
    print_intro()
    choice = get_menu_choice().lower()
    while not choice == 'quit':
        if choice == 'calculate':
            calculate_income()
        elif choice == 'native fruit':
            set_native()
        elif choice == 'set quantity':
            set_quantity()
        elif choice == 'help':
            print_help()
        else:
            print("Unrecognized input. Try again or enter 'Help' for more information.\n")
        time.sleep(0.5)
        choice = get_menu_choice().lower()


__main__()
