import re
loginAmt = 5
def login():
    username = input("Username :")
    password = input("Password :")
    global loginAmt
    while username != "admin" or password != "12345":
        loginAmt -= 1
        print("login", loginAmt, "left")
        print("Wrong username or password please retry")
        username = input("Username :")
        password = input("Password :")
        if loginAmt == 1:
            print("Your Login more than 5 time")
            Email = str(input("Please provide you E-mail for reset username and password : "))
            while not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
                print("Please check you E-mail")
                Email = str(input("Please provide you E-mail for reset username and password : "))
            else:
                print("Confirm link will send to your E-mail Thank you")
            break
            return exit()
    else:
        print("Welcome to Vat and price Calculation")
        showMenu()
def showMenu():
    print("Shopja")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input("Please Selected option above>>"))
    if userSelected == 1:
        price = float(input("Price of Goods(THB) :"))
        return vatCalculation(price)
    elif userSelected == 2:
        return priceCalculation()
    else:
        return print("Please should only option 1 and 2 thank you")
        exit()
def vatCalculation(totalprice):
    if totalprice < 0:
        print("Price of product should greater than Zero")
        exit()
    vat = 7
    result = totalprice + (totalprice * (vat / 100))
    return print(result)
def priceCalculation():
    price1 = int(input("FirstProductPrice :"))
    price2 = int(input("SecondProductPrice :"))
    if price1 and price2 < 0:
        print("Price of product should greater than Zero")
        exit()
    return print("Total price include : ",vatCalculation(price1 + price2))
login()
