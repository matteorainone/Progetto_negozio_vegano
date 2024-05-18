from utils import load_json_data
from .values_control import *

def new_item_info():
    item={
        "name":name_check(),
        "quantity":quantity_check(),
        "buying price":buying_price_check(),
        "selling price":selling_price_check()       
    }
    return item

def sale_info():
    item={
        "name":name_check(),
        "quantity":quantity_check()
    }
    return item

def info_builder(inventory_path:str):
    item_name=name_check()
    inventory=load_json_data(inventory_path)
    if item_name in list(inventory.keys()):
        item={
            "name":item_name,
            "quantity":quantity_check()
        }
    else:
        item={
            "name":item_name,
            "quantity":quantity_check(),
            "buying price":buying_price_check(),
            "selling price":selling_price_check()
        }
    return item