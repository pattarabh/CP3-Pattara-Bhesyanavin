systemMenu ={'ปลาทอด':450,'เนื้ออบ':150,'ไก่ย่าง':150,'ส้มตำ':55}
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
        menuList.append([menuName,systemMenu[menuName]])
        Total += systemMenu[menuName]
showbill()
print('Total : '+ str(Total)+"  THB")