import re

def name_check():
    """
    A function which checks the item name insert from the user.

    """
    pattern=r"^[A-Za-z]+$"
    while True:
        item_name=input("Nome del prodotto: ")
        if re.match(pattern,item_name):
            break
        else:
            print('Inserire un nome valido, non sono ammessi numeri, caratteri speciali o campi vuoti')
    return item_name

def quantity_check():
    """
    A function which checks if the item quantity insert by the user is an integer.

    """
    while True:
        item_quantity=input("Quantità: ")
        try:
            item_quantity=int(item_quantity)
            if item_quantity > 0:
                break
            else:
                print("Inserire una quantità positiva e non nulla")
        except ValueError:
            print("Inserire un numero intero")
    return item_quantity

def selling_price_check():
    """
    A function which checks if the selling price insert by the user is a float.

    """
    while True:
        selling_price=input("Prezzo di vendita: ")
        try:
            selling_price=float(selling_price)
            if selling_price > 0:
                break
            else:
                print("Inserire un prezzo positivo")
        except ValueError:
            print("Inserire un valore numerico")
    return selling_price

def buying_price_check():
    """
    A function which checks if the buying price insert by the user is a float.

    """
    while True:
        buying_price=input("Prezzo di acquisto': ")
        try:
            buying_price=float(buying_price)
            if buying_price > 0:
                break
            else:
                print("Inserire un prezzo positivo")
        except ValueError:
            print("Inserire un valore numerico")
    return buying_price