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
