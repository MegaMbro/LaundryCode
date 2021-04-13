import csv
import sys

 
def menu():
    option = ""
    while option != "Q":
        print("\nA: Add New Customer")
        print("B: View Customers")
        print("C: Add New Order")
        print("D: View Orders")
        print("E: Laundry Checks (Employees Only)")
        print("F: Delivery Date")
        print("Q: Quit\n")
 
        option = (input("Select an Option: ")).upper()
        if option == "A":
            addNewCustomer()
        elif option == "B":
            viewCustomers()
        elif option == "C":
            addNewOrder()
        elif option == "D":
            viewOrders()
        elif option == "E":
            laundrychecks()
        elif option == "F":
            DeliveryDate()
        elif option == "Q":
            print("Program ending...")
            sys.exit()
        else:
            print("Error, invalid option")

def DeliveryDate():
    OrderDays = int(input(print("How many days ago did you place the order?")))
    if OrderDays == 0:
        print("Your order has not been dispatched yet")
    elif OrderDays <= 3:
        print("Your order is on it's way and should arrive soon")
    elif OrderDays == 4:
        print("Your order is running slightly late")
    elif OrderDays >= 5:
        print("Your order is later than expected, please contact customer services about your delivery")


def laundrychecks():
    LinenReplacement = int(input("Enter the amount of linens that are damaged and need replacing: "))
    LinenOrder = LinenReplacement * 50
    print("The total amount to replace the linens is: £",LinenOrder)
    print("Do you wish to complete the order of new linens? (Yes) or (No)")
    Answer = input()
    if Answer == "Yes":
        print("Order has been placed")
    elif Answer == "No":
        print("Start again")
        menu()
    else:
        print("Error, invalid option")


def addNewCustomer():
    customerName = input("Please enter your name: ")
    customerAddress = input("Enter your address: ")
    print(customerName)
    print(customerAddress)
    print ("Is this information correct?\nPlease answer Yes/No")
    Answer = input()
    if Answer == "Yes":
        saveCustomer(customerName, customerAddress)
    elif Answer == "No":
        print("Start again")
        addNewCustomer()
    else:
        print("Error, invalid option")

 

def saveCustomer(customerName, customerAddress):
    with open('customer_file.csv', mode='a') as employee_file:
        writer = csv.writer(employee_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([customerName, customerAddress])

 

def viewCustomers():
    print("Name:  Address: ")
    with open('customer_file.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))


def addNewOrder():
    DateOrdered = input("Please enter the date when you ordered the linens:\n__/__/____\n")
    LinenX = int(input("Please enter the number of linens you have ordered: "))
    LinenDamage =int(input("How many linens are damaged: "))
    LinenDamageCost = LinenDamage * 50
    LinenCost = 5
    LinenOrder = LinenX * LinenCost
    LinenTotal = LinenOrder + LinenDamageCost
    print("The Total cost for your order is: £",LinenTotal,)
    if LinenDamage != 0:
        print("The charge for damaged linens has been added to your total order.\nThere were ", LinenDamage, "damaged linens in your order")
    print("Are the order details correct? (Yes) or (No):")
    OrderDetailsCheck = input()
    if OrderDetailsCheck == "Yes":
        saveOrder(LinenTotal, LinenDamage, DateOrdered)
    elif OrderDetailsCheck == "No":
        print("Start Again")
        addNewOrder()
    else:
        print("Error, invalid option")


def saveOrder(LinenTotal, LinenDamage, DateOrdered):
    with open('Order_file.csv', mode='w') as Order_file:
        writer = csv.writer(Order_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Total Cost:", LinenTotal,  "Amount of Linens Damaged:", LinenDamage, "Date:", DateOrdered])

def viewOrders():
    print("Order Total:  Linens Damaged: Order Date: ")
    with open('Order_file.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(' '.join(row))


userType = input("Are you a customer (C) or and employee (E): ")
if userType == "E":
    username = input("Enter a username: ")
    password =input("Enter a password: ")
    if (username == "Admin") and (password == "Password"):
        print("Correct Details, logging in...")
        menu()
    else:
        print("Incorrect Details, access denied!")
elif userType == "C":
    customerMenu()
else:
    print("Invalid Option")
     

 


#Main Block
menu()