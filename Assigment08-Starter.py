
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SDanh,8.29.2020,Implemented Product & IO Classes
# SDanh,8.30.2020,Implemented File Processor Class & Menu
# SDanh,8.31.2020,Added exception handling and proper heading documentation for classes.
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        getName: -> product_name
        getPrice: -> product_price
        setName(product_name): sets product name
        setPrice(product_price): sets product price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SDanh,8.29.2020,Implemented properties & methods
    """
    product_name = ""
    product_price = 0.0

    def __init__(self, product_name, product_price):
        self.product_name = str(product_name)
        self.product_price = float(product_price)

    def __str__(self):
        string_representation = "(" + self.product_name +  ", $" + str(self.product_price) + ")"
        return string_representation

    def getName(self):
        return self.product_name
    def getPrice(self):
        return self.product_price
    def setName(self, product_name):
        self.product_name = str(product_name)
    def setPrice(self, product_price):
        self.product_price = str(product_price)

    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): saves list of product objects to selected file

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_product_objects.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                line.strip("\n")
                product_name, product_price = line.split(",")
                newProduct = Product(product_name, product_price)
                list_of_product_objects.append(newProduct)
            file.close()
        except FileNotFoundError as e:
            print(e.__str__())
            print(file_name + " doesn't exist!")
        except BaseException:
            print("Unknown Error!")
        return list_of_product_objects

    # TODO: Add Code to process data to a file
    def save_data_to_file(file_name, list_of_product_objects):
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                line = product.getName() + "," + str(product.getPrice()) + "\n"
                file.write(line)
            file.close()
        except FileNotFoundError as e:
            print(e.__str__())
            print(file_name + " doesn't exist!")
        except BaseException:
            print("Unknown Error!")
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Input & Output:
        properties:
            menu_display: (string) displays list of possible options.
        methods:
            print_menu: prints menu_display
            get_choice: -> user's inputted choice
            print_data: prints list of Product objects
            new_data: -> name and value of new product
        changelog: (When,Who,What)
            SDanh,8.29.2020, Created code_stubs
            <Your Name>,<Today's Date>,Modified code to complete assignment 8
        """
    menu_display = "MAIN MENU: |1-Print |2-Add |3-Save |4 - Quit|"
    # TODO: Add code to show menu to user
    def print_menu(self):
        print(self.menu_display)
    # TODO: Add code to get user's choice
    def get_choice(self):
        user_choice = input("INPUT: ")
        return user_choice
    # TODO: Add code to show the current data from the file to user
    def print_data(self,lstData):
        lstData = list(lstData)
        for product in lstData:
            print(product)
    # TODO: Add code to get product data from user
    def new_data(self):
        try:
            new_product_name = str(input("Product Name: "))
            new_product_price = float(input("Product Price: "))
        except ValueError as e:
            print(e.__str__())
            print("String for Name & Number for Price!!!")
        return new_product_name, new_product_price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
myIO = IO()

# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
while True:
# Show user a menu of options
    myIO.print_menu()
# Get user's menu option choice
    choice = myIO.get_choice()
    # Show user current data in the list of product objects
    if choice == '1':
        print("Printing...")
        myIO.print_data(lstOfProductObjects)
        continue
    # Let user add data to the list of product objects
    elif choice == '2':
        print("Adding...")
        try:
            product_name, product_price = myIO.new_data()
            newProduct = Product(product_name, product_price)
            lstOfProductObjects.append(newProduct)
        except UnboundLocalError as e:
            print(e.__str__())
            print("Bad Entry. Canceling...")
        continue
    # let user save current data to file and exit program
    elif choice == '3':
        print("Saving...")
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue
    # Quitting Program
    elif choice == '4':
        print("Closing...")
        break
    # Wrong input
    else:
        print("WRONG INPUT!!")
        continue

# Main Body of Script  ---------------------------------------------------- #

