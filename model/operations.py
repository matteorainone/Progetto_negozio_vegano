import datetime
from utils import *
from .inventory_functions import *



def sell_item(item: dict, inventory_path:str):
    """
    the sell_item function is used to realize the sale of an item in the inventory. 
    If the quantity requested is greater than the quantity in stock or the requested item is not in stock, an error message will be returned.

    Parameters
    item (dict): The dictionary containing information about the sale
    inventory_path (str): the path of the inventory file
    """
    inventory = load_json_data(inventory_path)
    
    if item["name"] in inventory:
        if item["quantity"] <= inventory[item["name"]]["quantity"]:
            inventory[item["name"]]["quantity"] -= item["quantity"]
            #print(f"Vendita registrata: {item['quantity']} X {item['name']}:{item["selling price"]}\n")
        else:
            raise ValueError("Il numero di prodotti richiesti non è presente in magazzino")
    else:
        raise ValueError("Il prodotto richiesto non è presente in magazzino")

    write_json_data(inventory, inventory_path)

def add_item(item:dict,inventory_path:str):
  """
  the add_item function is used to add new products to the stock. 
  If the product you want to add is already present, its quantity will be updated; 
  otherwise, if the product is not in the stock, all the information will be added, thus including purchase and sale prices.

  Parameters
  item (dict): The dictionary containing information about the item to add
  inventory_path (str): the path of the inventory file
  """
  inventory=load_json_data(inventory_path)
  
  if item["name"] in inventory:
      inventory[item["name"]]["quantity"] += item["quantity"]
  else:
      inventory[item["name"]] = new_item_maker(item)

  write_json_data(inventory, inventory_path)
  print(f"AGGIUNTO: {item['quantity']} X {item['name']}")


def item_list(inventory_path:str):
    """
    the item_list function is used to show the list of the item stored in the stock.

    Parameters
    inventory_path (str): the path of the inventory file
    """
    inventory=load_json_data(inventory_path)
    if len(inventory)==0:
        print("Il magazzino è vuoto")
    else:
        item_list_printer(inventory)

def sales_register(data:dict,register_file:str):
    """
    This function saves sales data within the register file.
    
    Parameters:
    data (dict): the dictionary containing the sales data
    register_file (str): the register file path
    """
    register=load_register_file(register_file)
    
    now=datetime.datetime.now()
    sale_date=now.strftime("%d-%m-%Y")
    sale_hour=now.strftime("%H:%M")
    register[f"vendita del {sale_date}, ore {sale_hour}"]=sales_data(data)
    register[f"vendita del {sale_date}, ore {sale_hour}"]["total"]=register[f"vendita del {sale_date}, ore {sale_hour}"]["quantity"]*register[f"vendita del {sale_date}, ore {sale_hour}"]["selling price"]

    write_json_data(register,register_file)

def profit_calculator(register_file:str):
    """
    This function open the registry file and calculate the gross and net profits.
    
    Parameters
    register_file (str): the register file path
    """
    register=load_json_data(register_file)
    gross_profit=0
    net_profit=0
    for sale, sale_data in register.items():
        gross_profit+=sale_data["total"]
        net_profit_i=sale_data["total"]-sale_data["buying price"]*sale_data["quantity"]
        net_profit+=net_profit_i

    return print(f"Profitto: lordo=€{gross_profit}, netto=€{net_profit}")