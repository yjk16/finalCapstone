# This program will allow the user to choose an option from the menu
# and view and/ or change various values from a list of Nike shoes.

# Read: https://stackoverflow.com/questions/62414396/how-to-skip-first-line-in-python-using-read-function
# to help me skip the first line of inventory.txt.
# https://www.geeksforgeeks.org/searching-a-list-of-objects-in-python/
# to help me figure out how to search for an object within a class using attributes.
# Had help from my friends Silas and Nick with error handling.
# Had help from mentor Jonathan Lloyd with things including which try/ except to use, indentations on for loops
# and the search_shoe section.
# Read different websites including geeksforgeeks.org on how to use tabulate.
# My friend Silas helped me with tabulate, especially how to install pip.
# I've changed the format of my docstrings as suggested by reviewer Chris Smit (thank you!)


# Importing relevant files and libraries.
from shoe import Shoe
from tabulate import tabulate

# Creating an empty list for shoes.
shoe_list = []


def read_shoes_data():
    """
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data.
    It will then append this object into the shoes list. One line in this file represents
    data to create one object of shoes.

    :return: shoe_list.

    :raises: FileNotFoundError, if the files are not in the same directory or not found

    :raises: IndexError, if the inventory is empty, the indexes for data will not be able to be read
    """

    shoes_data = None

    try:
        shoes_data = open("inventory.txt", "r")

        # This will skip the first line of the file.
        shoes_data.readline()

        for line in shoes_data.readlines():
            data = line.strip().split(",")
            shoe_product = Shoe(data[0], data[1], data[2], data[3], data[4])
            shoe_list.append(shoe_product)

        return shoe_list

    except FileNotFoundError:
        print("The file that you are trying to open cannot be found.")

    except IndexError:
        print("I'm afraid something has gone wrong.\nThere may not be enough data in your inventory.")

    finally:
        if shoes_data is not None:
            shoes_data.close()


def view_all():
    """
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __repr__ function,
    numbered by enumerate for easier readability.
    """

    read_shoes_data()
    for index, shoe_product in enumerate(shoe_list, 1):
        print(f"{index}. {shoe_product}")


def value_per_item():
    """
    This function will calculate the total value for each item, the formula for value being: value = cost * quantity.
    This information will be printed onto the console using tabulate to display the results.

    :raises: IndexError, if value_shoe_list is empty
    """

    value_shoe_list = []

    try:
        item_value = open("inventory.txt", "r")
        item_value.readline()

        for line in item_value.readlines():
            data = line.strip().split(",")
            value_shoes = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
            value_shoe_list.append(value_shoes)

        value_list = []

        for sneakers in value_shoe_list:
            shoe_value = sneakers.cost * sneakers.quantity
            values = [sneakers.product, shoe_value]
            value_list.append(values)

        title = ["Shoe", "Value"]
        print(tabulate(value_list, headers=title, tablefmt="simple"))

        item_value.close()

    except IndexError:
        print("I'm afraid something has gone wrong.\nYou may not have enough data in your inventory.")


def search_shoe():
    """
    This function will display the shoes then allow the user to search for a shoe by entering the SKU code of a shoe.
    The information of that shoe, including the cost and quantity, will then be displayed.
    If the SKU code entered matches one in the inventory, it will return the details of the shoe.
    Otherwise, it will return a message to explain that the shoe could not be found.
    """

    print("The shoes currently in stock are:\n")

    shoes_list = read_shoes_data()
    for index, shoe_product in enumerate(shoes_list, 1):
        print(f"{index}. {shoe_product}")

    search_sku = input("\nPlease enter the code for the shoe that you are looking for."
                       "\nRemember to include the SKU part of the code."
                       "\nE.g SKU88888:\n")

    for shoe in shoes_list:
        if search_sku == shoe.get_code():
            return f"\nThe details of the shoe you are looking for are below:\n{shoe}"
    else:
        return "\nThat shoe could not be found."


def capture_shoes():
    """
    This function will allow the user to capture data about a shoe and use this data to create a shoe object.
    It will append this object inside the shoe list and a message will be printed to say that this has been updated.

    :raises: ValueError, if the user enters anything that is not a number for the required fields
    """

    country = input("Which country is the shoe from:\n")
    code = input("What is the code for this shoe?\nRemember to prefix the number with SKU\nE.g SKU12345:\n")
    product = input("What is the product name of this shoe:\n")

    while True:
        try:
            cost = int(input("What is the cost of this shoe:\n"))
            break
        except ValueError:
            print("That was not a number...")

    while True:
        try:
            quantity = int(input("What is the quantity of this shoe:\n"))
            break
        except ValueError:
            print("That wasn't a number. Try again...")

    new_shoe = Shoe(country, code, product, cost, quantity)

    capture = open("inventory.txt", "a")
    # I'm a bit confused as I know it was suggested that I move the \n from the end of the line to the beginning
    # but when I do that, it creates a blank line as I think there is already a \n at the end of the previous line.
    # Also, after using functions re_stock() and highest_qty() a \n is automatically formed
    # so if capturing a shoe after using one of those functions, again a blank line is created.
    # I also tried moving all the '\n's to the beginning of their lines but that causes an IndexError because
    # it creates a blank line on line 2 of the file
    # between the titles (for the functions re_stock() and highest_qty()) and the shoes when rewriting them back.
    # So I did move the \n, but I've moved it back.  I hope that's ok.
    # Have I understood the comment from the review for the right section?
    capture.write(f"{country},{code},{product},{cost},{quantity}\n")
    capture.close()

    shoe_list.append(new_shoe)

    print("This has been updated.")


def re_stock():
    """
    This function will find the shoe object with the lowest quantity (the shoe that needs to be re-stocked).
    It will then ask the user if they want to add to this quantity of shoes
    and update this on the file for this shoe if they decide to add to it.
    A message will be printed to say that this has or has not been updated, depending on the user's choice.

    :raises: IndexError, if re_stock_list is empty
    """

    re_stock_list = []

    try:
        re_stocking = open("inventory.txt", "r")
        titles = re_stocking.readline()

        for line in re_stocking.readlines():
            data = line.strip().split(",")
            restock_shoe = Shoe(data[0], data[1], data[2], data[3], int(data[4]))
            re_stock_list.append(restock_shoe)

        re_stocking.close()

        from operator import attrgetter
        min_quantity = min(re_stock_list, key=attrgetter('quantity'))
        print(f"The product with the lowest quantity is: {min_quantity.product} "
              f"of which there are {min_quantity.quantity} available in stock.")

        answer = input("Would you like to restock this item?\nEnter 'y' for 'yes' and 'n' for 'no:\n").lower()

        if answer == 'n':
            print("There has been no amendment made.")

        elif answer == 'y':
            restock = int(
                input(f"Please enter the number you would like to add to the {min_quantity.product} stock:\n"))

            new_stock = min_quantity.quantity + restock
            min_quantity.change_quantity(new_stock)

            editing = open("inventory.txt", "w")
            editing.write(f"{titles}")
            for item in re_stock_list:
                editing.write(f"{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n")
            editing.close()

            print("This has now been updated.")

        else:
            print("That was not a recognised entry.")

    except IndexError:
        print("I'm afraid something has gone wrong.\nYou may not have enough data in your inventory.")


def highest_qty():
    """
    This function will determine the product with the highest quantity and print this shoe as being for sale.
    It will ask the user by what percentage they would like to reduce the shoe, update this in the inventory,
    and then display a message to inform the user.

    :raises: ValueError, if the user inputs an entry that is not a number for the required field

    :raises: IndexError, if there is not enough data in 'inventory.txt'
    """

    try:

        highest_qty_list = []

        sale = open("inventory.txt", "r")
        line_one = sale.readline()

        for line in sale.readlines():
            data = line.strip().split(",")
            high_quantity_list = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
            highest_qty_list.append(high_quantity_list)

            sale.close()

            from operator import attrgetter
            max_quantity = max(highest_qty_list, key=attrgetter('quantity'))

        while True:
            try:
                reduction_percentage = float(input(f"By what percentage would you like "
                                                   f"{max_quantity.product} to be reduced?\n"
                                                   f"Please enter just the number. E.g for 10%, enter 10:\n"))
                break

            except ValueError:
                print("That wasn't a number. Try again...")
        
        new_cost = round((float(max_quantity.cost) * ((100 - reduction_percentage) / 100)), 2)
        max_quantity.change_cost(new_cost)

        edits = open("inventory.txt", "w")
        edits.write(f"{line_one}")
        for trainer in highest_qty_list:
            edits.write(f"{trainer.country},{trainer.code},{trainer.product},{trainer.cost},{trainer.quantity}\n")
        edits.close()

        print(f"\n{max_quantity.product} is now on sale at {new_cost}R "
              f"which is a reduction of {reduction_percentage}%. This has been updated in your inventory.")

    except IndexError:
        print("I'm afraid something has gone wrong.\nYou may not have enough data in your inventory.")


def menu():
    print("\nPlease choose from one of the options below:")
    print("")
    print("\t\t1. view all shoes in the inventory")
    print("\t\t2. check the values of the shoes")
    print("\t\t3. search for a shoe to check the current cost and quantity")
    print("\t\t4. add a new shoe to the inventory")
    print("\t\t5. restock the shoe with the lowest quantity")
    print("\t\t6. check which shoe has the highest quantity and mark this as for sale")
    print("\t\t7. exit")
    print("")


while True:
    menu()
    choice = input("I choose...\n")

    if choice == '1':
        print("\nThese are the shoes currently in the inventory:\n")
        view_all()

    elif choice == '2':
        print("The values of the shoes are:\n")
        value_per_item()

    elif choice == '3':
        print(search_shoe())

    elif choice == '4':
        capture_shoes()

    elif choice == '5':
        re_stock()

    elif choice == '6':
        highest_qty()

    elif choice == '7':
        print("Thanks for using our inventory system.\nHave a nice day!")
        exit()

    else:
        print("I'm afraid there has been an incorrect entry.\nPlease try again...")
