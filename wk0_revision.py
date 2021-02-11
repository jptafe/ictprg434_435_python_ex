#!/usr/bin/python
chocoprice = 1.5

def Input_choc():
    print("how many bars: ")
    qty = input()
    return qty

def Calc_choc(chocPrice_param, qty):
    if qty.isnumeric():
        qty = int(qty)
        if qty >= 20:
            total_price = ( chocPrice_param * qty) * .9
        else:
            total_price = chocPrice_param * qty
    return str(total_price)

quantity_return = Input_choc()
print_value = Calc_choc(chocoprice, quantity_return)
print("this is the total: " + str(print_value))
