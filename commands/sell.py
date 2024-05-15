from model import sell_item, sales_register
from input.values_control import *
from input import sale_info
from utils import load_json_data

def sell_command(inventory_path:str,register_path:str):
    """
    The function used to manage the sell command required by the user.

    Args:
        inventory_path (str): the path of the inventory json file
        register_path (str): the path of the register json file
    """
    inventory=load_json_data(inventory_path)
    status=False
    item=sale_info()
    cart={}
    while status is False:
        try:
            si_status=False
            sell_item(item,inventory_path)
            item["selling price"]=inventory[item["name"]]["selling price"]
            item["buying price"]=inventory[item["name"]]["buying price"]
            sales_register(item,register_path)
            si_status=True
        except Exception as e:
            print(e)
        if si_status is True:
            if item["name"] in cart:
                cart[item["name"]]["quantity"]+=item["quantity"]
            else:
                cart[item["name"]]={
                    "quantity":item["quantity"],
                    "selling price":item["selling price"]
                }
        new_product=input("Aggiungere un altro prodotto ? (si/no): ")
        if new_product.lower() == "si":
            item=sale_info()
            continue
        elif new_product.lower()=="no":
            status=True
        else:
            print("Valore non riconosciuto, vendita terminata")
            break
    print("VENDITA REGISTRATA")
    if cart:
        total=0
        for item, item_data in cart.items():
            item_data['total']=item_data['quantity']*item_data['selling price']
            total+=item_data['total']
            print(f"- {cart[item]['quantity']} X {item}:€{item_data['selling price']}")
        print(f"Totale: €{total}")
    else:
        print("Il carrello è vuoto, nessuna vendita effettuata")