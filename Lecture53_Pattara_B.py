userInput = float(input("Input your money : "))
def VatCalculation(InputMoney):
    result = InputMoney+(round(InputMoney*0.07,2))
    return result
print(VatCalculation(userInput))