username = input("Username :")
password = input("Password :")
if username == "Pattara" and password == "12345":
    print("Welcome back ", username, "My Store")
    print("-"*30)
    p1 = ("1. Iphone 12 pro 128GB     THB 39,900")
    p2 = ("2. Ipad pro 128GB          THB 34,900")
    p3 = ("3. Air Pod                 THB 5,400")
    p4 = ("4. MacBook Air             THB 32,900")
    p5 = ("5. MacBook Pro             THB 52,900")
    p6 = ("6. HomePod                 THB 49,00")
    p7 = ("7. iMac                    THB 120,000")
    p8 = ("8. Applecare               THB 12,000")
    print("      Product                 Price   ")
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print(p8)
    userSelected = int(input("Please select product from product list >> :"))
    qtyInput = int(input("Please input Quantity of goods >> : "))
    if qtyInput <0 :
        print("The Quantity of goods should be greater than Zero")
        exit()
    if userSelected == 1:
        print(">>>>Product choose<<<<\n",p1," ",qtyInput," Units", "  Total price: ",39900*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 2:
        print(">>>>Product choose<<<<\n",p2," ",qtyInput," Units", "  Total price : ",34900*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 3:
        print(">>>>Product choose<<<<\n",p3," ",qtyInput," Units", "  Total price : ",5400*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 4:
        print(">>>>Product choose<<<<\n",p4," ",qtyInput," Units", "  Total price : ",32900*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 5:
        print(">>>>Product choose<<<<\n",p5," ",qtyInput," Units", "  Total price : ",52900*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 6:
        print(">>>>Product choose<<<<\n",p6," ",qtyInput," Units", "  Total price : ",49000*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 7:
        print(">>>>Product choose<<<<\n",p7," ",qtyInput," Units", "  Total price : ",120000*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    elif userSelected == 8:
        print(">>>>Product choose<<<<\n",p8," ",qtyInput," Units", "  Total price : ",12000*qtyInput)
        print("                    Thank you for buying with us")
        print("\U0001f600" * 55)
    else:
        print("Please choose number from list above thank you")
else:
    print("Your Username or Password are incorrect please retry")