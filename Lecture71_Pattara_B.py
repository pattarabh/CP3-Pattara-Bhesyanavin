menuList =[]
prictList = []
def showbill():
    print("-My Food-")
    for food in range(len(menuList)):
        print(menuList[food],prictList[food])
while True:
    menuName= input("Please Enter menu")
    if(menuName.lower() =="exit"):
        break
    else:
        menuPrice = int(input("Price"))
        menuList.append(menuName)
        prictList.append(menuPrice)
showbill()
print('Total : '+ str(sum(prictList)))

