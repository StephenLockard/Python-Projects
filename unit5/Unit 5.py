from tkinter import *

# generate user input fields
fields = ('Pennies', 'Nickels', 'Dimes', 'Quarters', 'Half Dollars', 'Dollar Coins', 'Pennies $', 'Nickels $',
          'Dimes $', 'Quarters $', 'Half Dollars $', 'Dollar Coins $', 'Total $')


# create app window
def app_window(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=10, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=10, pady=10)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def total_value(entries):

    p = (float(entries['Pennies'].get()))
    n = (float(entries['Nickels'].get()))
    d = (float(entries['Dimes'].get()))
    q = (float(entries['Quarters'].get()))
    hd = (float(entries['Half Dollars'].get()))
    dollar_coin = (float(entries['Dollar Coins'].get()))

    value_positive = 1

    if p < 0:
        entries['Pennies'].delete(0, END)

        entries['Pennies'].insert(0, 'Negative money?')
        p = 0
        value_positive = 0
    if n < 0:
        entries['Nickels'].delete(0, END)
        entries['Nickels'].insert(0, 'Negative money?')
        n = 0
        value_positive = 0
    if d < 0:
        entries['Dimes'].delete(0, END)
        entries['Dimes'].insert(0, 'Negative money?')
        d = 0
        value_positive = 0
    if q < 0:
        entries['Quarters'].delete(0, END)
        entries['Quarters'].insert(0, 'Negative money?')
        q = 0
        value_positive = 0
    if hd < 0:
        entries['Half Dollars'].delete(0, END)
        entries['Half Dollars'].insert(0, 'Negative money?')
        hd = 0
        value_positive = 0
    if dollar_coin < 0:
        entries['Dollar Coins'].delete(0, END)
        entries['Dollar Coins'].insert(0, 'Negative money?')
        dollar_coin = 0
        value_positive = 0
    if value_positive == 0:
        q = n = p = d = 0
    quarters = .25 * q
    pennies = 0.01 * p
    dimes = 0.1 * d
    nickels = 0.05 * n
    half_dollars = 0.5 * hd
    dollar_coins = 1 * dollar_coin
    money_value = quarters + pennies + dimes + nickels + half_dollars + dollar_coins

    entries['Pennies $'].delete(0, END)
    entries['Pennies $'].insert(0, pennies)
    entries['Nickels $'].delete(0, END)
    entries['Nickels $'].insert(0, nickels)
    entries['Dimes $'].delete(0, END)
    entries['Dimes $'].insert(0, dimes)
    entries['Quarters $'].delete(0, END)
    entries['Quarters $'].insert(0, quarters)
    entries['Half Dollars $'].delete(0, END)
    entries['Half Dollars $'].insert(0, dimes)
    entries['Dollar Coins $'].delete(0, END)
    entries['Dollar Coins $'].insert(0, dimes)
    entries['Total $'].delete(0, END)
    entries['Total $'].insert(0, money_value)


# run app window
if __name__ == '__main__':
    root = Tk()
    root.wm_title("Coin Counter")
    w = Label(root, text="Enter your coin quantities")
    w.pack()
    entries = app_window(root, fields)
    b1 = Button(root, text='Compute', command=(lambda e=entries: total_value(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
