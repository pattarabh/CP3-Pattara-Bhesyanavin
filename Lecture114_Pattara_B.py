from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

currency_rate = CurrencyRates()
convert_rate = 0
def leftClickButton_Convert(event):
    if amountInput.get() == '':
        messagebox.showerror("Error","Please input data")
    elif float(amountInput.get()) <= 0:
        messagebox.showerror("Error", "Amount should be greater than 0")
    convert_rate = float(amountInput.get())*currency_rate.get_rate(currencyselectInput.get(),currencyselectOutput.get())
    lable_amountOutput.configure(text = str(round(convert_rate,2)))

mainwindows = tk.Tk()
mainwindows.geometry('900x100')
mainwindows.configure(bg = '#000000')
mainwindows.title("Convert Currency")
#Select Input Currency
lable_currencyselectInput = tk.Label(mainwindows, text = "Select Your Input Currency",
          background = 'green', foreground ="white",
          font = ("Bahnschrift SemiBold", 15,'bold'))
lable_currencyselectInput.grid(row = 0, column = 0)

currencyselectInput = ttk.Combobox(mainwindows,width = 31,
                                   values=[
                                       "USD",
                                       "JPY",
                                       "EUR",
                                       "THB",
                                       "IDR",
                                       "BGN",
                                       "ILS",
                                       "GBP",
                                       "AUD",
                                       "CHF",
                                       "HKD"])
currencyselectInput.grid(row = 1, column = 0)
currencyselectInput.current(3)
#Select Output Currency
lable_currencyselectOutput = tk.Label(mainwindows, text = "  Select Your Output Currency ",
          background = 'red', foreground ="white",
          font = ("Bahnschrift SemiBold", 15,'bold'))
lable_currencyselectOutput .grid(row = 0, column = 2)
currencyselectOutput = ttk.Combobox(mainwindows,width = 33,
                                   values=[
                                       "USD",
                                       "JPY",
                                       "EUR",
                                       "THB",
                                       "IDR",
                                       "BGN",
                                       "ILS",
                                       "GBP",
                                       "AUD",
                                       "CHF",
                                       "HKD"])
currencyselectOutput.grid(row = 1, column = 2)
currencyselectOutput.current(0)
#Input Amount you want to convert
lable_amountInput = tk.Label(mainwindows, text = "Please Input your Amount",
          background = 'black',foreground = 'white',
          font = ("Bahnschrift SemiBold", 15,'bold'))
lable_amountInput .grid(row = 0 , column = 1)
amountInput = tk.Entry(mainwindows,width = 35,justify = 'right')
amountInput.grid(row = 1 ,column = 1)
#Output Amont after convert
lable_amountOutputtxt = tk.Label(mainwindows, text = "Convert result :",
          background = 'black',foreground = 'white',
          font = ("Bahnschrift SemiBold", 22,'bold')).grid(row = 3,column = 0)
lable_amountOutput = tk.Label(mainwindows,text = '0',width = 30,
                    font = ("Bahnschrift SemiBold", 15,'bold'))
lable_amountOutput.grid(row = 3 , column = 1)
#Convert button
button_convert = tk.Button(mainwindows,text = "Convert",width = '25',background ='#808080',
                           font = ("Bahnschrift SemiBold", 10,'bold'))
button_convert.bind('<Button-1>', leftClickButton_Convert)
button_convert.grid(row = 3 , column = 2)
mainwindows.mainloop()
