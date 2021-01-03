userInput = int(input("Number for * :"))
for i in range(userInput):
    print(" "*(userInput-i),"*"*(i+(1*(i+1))))