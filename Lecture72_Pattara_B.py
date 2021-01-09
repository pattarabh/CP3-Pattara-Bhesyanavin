menuList =[]
Total = 0
def showbill():
    print("-My Food-")
    for food in range(len(menuList)):
        print(menuList[food][0],menuList[food][1],"  THB")
while True:
    menuName= input("Please Enter menu")
    if(menuName.lower() =="exit"):
        break
    else:
        menuPrice = int(input("Price"))
        menuList.append([menuName,menuPrice])
        Total += menuPrice
showbill()
print('Total : '+ str(Total)+"  THB")