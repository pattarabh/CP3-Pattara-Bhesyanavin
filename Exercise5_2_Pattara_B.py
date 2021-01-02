print("How fast you are (km\hr)")
print("-"*15)
s = float(input("Input Distance (km) : "))
t = float(input("Input Time (hr) : "))
# s and t need to be greater than 0
if s <0 or t < 0:
    print("Data Should be greater than Zero")
    exit()
print("-"*15)
x = s/t
print("your speed are",int(s/t)," km\hr")
if x > 100:
    print("Driver slower")
else:print("you speed are ok")
print("Thank you")