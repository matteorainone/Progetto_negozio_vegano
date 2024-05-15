from utils import *

def new_item_maker(dictionary:dict):
  """
  The function item maker helps to create the dictionary representing the new item added to the inventory
  Parameters
  dictionary: the input dictionary containing the information of the new item
  """
  item={}
  item["quantity"]=dictionary["quantity"]
  item["buying price"]=dictionary["buying price"]
  item["selling price"]=dictionary["selling price"]
  return item

def sales_data(data:dict):
    """
    The function sales data helps to create the dictionary containing the sales data added to the register file.

    Parameters:
    data (dict): A dictionary containing the data to be saved in the register file.
    """
    sales_figures={}
    sales_figures["product_name"]=data["name"]
    sales_figures["quantity"]=data["quantity"]
    sales_figures["buying price"]=data["buying price"]
    sales_figures["selling price"]=data["selling price"]
    return sales_figures

def item_list_printer(inventory:dict):
    """
    Print the list of items in an inventory with vertical alignment of product names, quantities and prices.
    
    Parameters:
    inventory (dict): the inventory dict

    Returns:
    None: This function returns nothing but directly prints the formatted output to the console.
    """
    max_len_product = len("PRODOTTO")
    max_len_quantity = len("QUANTITA'")
    max_len_price = len("PREZZO") + 2
    
    for product_name, details in inventory.items():
        max_len_product = max(max_len_product, len(product_name))
        max_len_quantity = max(max_len_quantity, len(str(details['quantity'])))
        max_len_price = max(max_len_price, len(str(details['selling price']))+2)

    header = f"{len_checker('PRODOTTO', max_len_product)} {len_checker('QUANTITA\'', max_len_quantity)} {len_checker('PREZZO', max_len_price)}"
    print(header)

    for product_name, details in inventory.items():
        product_str = len_checker(product_name, max_len_product)
        quantity_str = len_checker(str(details['quantity']), max_len_quantity)
        price_str = len_checker(f"€{details['selling price']}", max_len_price)
        print(f"{product_str} {quantity_str} {price_str}")