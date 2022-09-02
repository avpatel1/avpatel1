def add():
    num = int(input("Please enter, How many items you would like to add? "))
    dicst = dict(input("Please enter, name of item and how many of it you want to add.: ").split() for _ in range(num))
    for key, value in dicst.items():
         if key in dicscount.keys():
            dicscount[key] = dicscount[key] + int(value)
         else:
            dicscount[key] = 0
            dicsprice[key] = 0
            print("Sorry, Currently, We do not carry this item. We will try to add this item into inventory shortly.")

def remove():
    num = int(input("Please enter, How many items you would like to remove? "))  
    dicst = dict(input("Please enter, name of item and how many of it you want to remove.: ").split() for _ in range(num))
    for key, value in dicst.items():
        if key in dicscount.keys():
            if dicscount[key] >= int(value):
                dicscount[key] = dicscount[key] - int(value)
            else:
                print("Sorry, You can't have negative number of ", key)
        else:
            dicscount[key] = 0
            dicsprice[key] = 0
            print("Sorry, Currently, We do not carry this item. We will try to add this item into inventory shortly.")

def increase():
    num = int(input("Please enter, Price of how many iteam you would like to increase? "))
    dicst = dict(input("Please enter, name of item and by how much you would like to increase its price.: ").split() for _ in range(num))
    for key, value in dicst.items():
         if key in dicsprice.keys():
            dicsprice[key] = dicsprice[key] + int(value)
         else:
            dicscount[key] = 0
            dicsprice[key] = 0
            print("Sorry, Currently, We do not carry this item. We will try to add this item into inventory shortly.")

def decrease():
    num = int(input("Please enter, Price of how many iteam you would like to decrease? "))  
    dicst = dict(input("Please enter, name of item and by how much you would like to decrease its price.: ").split() for _ in range(num))
    for key, value in dicst.items():
        if key in dicsprice.keys():
            if dicsprice[key] >= int(value):
                dicsprice[key] = dicsprice[key] - int(value)
            else:
                print("Sorry, You can't have negative price for ", key)
        else:
            dicscount[key] = 0
            dicsprice[key] = 0
            print("Sorry, Currently, We do not carry this item. We will try to add this item into inventory shortly.")

def empl():
    afinal = True
    while afinal == True:
        final = input("Please enter, Would you like a final list of inventory? (Yes or No): ")
        if (final == "Yes") or (final == "No"):
            afinal = False
        else:
            afinal = True
    aoption = True
    while aoption == True:
        option = input("Please enter, Do you want to update count, price, or both of items in the inventory?: ")
        if option == "count":
            aoption = False
            aduty = True
            while aduty == True:
                duty = input("Please enter, Are you adding or removing items or both from inventory?: ")
                if duty == "adding":
                    add()
                    aduty = False
                elif duty == "removing":
                    remove()
                    aduty = False
                elif duty == "both":
                    add()
                    remove()
                    aduty = False
                else:
                    aduty = True
                    print("Please enter correct Input?")
        elif option == "price":
            aoption = False
            aduty = True
            while aduty == True:
                duty = input("Please enter, Are you increasing, decreasing or both of the items?: ")
                if duty == "increasing":
                    aduty = False
                    increase()
                elif duty  == "decreasing":
                    aduty = False
                    decrease()
                elif duty == "both":
                    increase()
                    decrease()
                    aduty = False
                else:
                    aduty = True
                    print("Please enter correct Input?")
        elif option == "both":
            aoption = False
            aduty = True
            while aduty == True:
                duty = input("Please enter, Are you adding or removing items or both from inventory?: ")
                if duty == "adding":
                    add()
                    aduty = False
                elif duty == "removing":
                    remove()
                    aduty = False
                elif duty == "both":
                    add()
                    remove()
                    aduty = False
                else:
                    aduty = True
                    print("Please enter correct Input?")
            aoption = False
            aduty = True
            while aduty == True:
                duty = input("Please enter, Are you increasing, decreasing or both of the items?: ")
                if duty == "increasing":
                    aduty = False
                    increase()
                elif duty  == "decreasing":
                    aduty = False
                    decrease()
                elif duty == "both":
                    increase()
                    decrease()
                    aduty = False
                else:
                    aduty = True
                    print("Please enter correct Input?")
        else:
            aoption = True
    if final == "Yes":
        inve()

def cust():
    order = int(input("Please enter, Which items and how many of them you would like to purchase? "))
    dicst = dict(input("Enter key and value: ").split() for _ in range(order))
    summ = 0
    for key, value in dicst.items():
        if key in dicscount.keys():
            if int(value) <= dicscount[key]:
                dicscount[key] = dicscount[key] - int(value)
                summ = summ + int(value)*dicsprice[key]
            else:
                print("Sorry, We currently do not have  ", value, " ", key)
                print("Currently, We only have ", dicscount[key], " ", key, )
                aorder2 = True
                while aorder2 == True:
                    order2 = input(" Would you like to buy this many?(Yes or No): ")
                    if (order2 == "Yes") or (order2 == "No"):
                        aorder2 = False
                    else:
                        aorder2 = True
                if order2 == "Yes":
                    dicscount[key] = dicscount[key] - dicscount[key]
                    summ = summ + dicscount[key]*dicsprice[key]
                
        else:
            dicsprice[key] = 0 
            dicscount[key] = 0
            print("Sorry, We currently do not carry this item. We will try to add this item into inventory shortly.")

    print("Total of your today's order is $", summ)

def inve():
    for key, value in dicscount.items():
        print(key, ' : ', value, '  ', dicsprice[key])


dicscount = {
    "Apple": 0,
    "Banana": 5,
    "Berries": 10,
    "Grapes": 15,
    "Orange": 20
}
dicsprice = {
    "Apple": 2.89,
    "Banana": 1.15,
    "Berries": 1.73,
    "Grapes": 1.55,
    "Orange": 1.99
}

awho = True
while awho == True:
    who = input("Please enter, Are you a Customer or Employee or just Inventory check ?: ")
    if who == "Customer":
        cust()
        awho = False
    elif who == "Employee":
        empl()
        awho = False
    elif who == "Inventory":
        inve()
        awho = False
    else:
        awho = True