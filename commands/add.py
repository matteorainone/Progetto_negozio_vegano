from model import add_item
from input import new_item_info

def add_command(inventory_path:str):
    """
    A function used to manage the add command required from the user.

    Args:
        inventory_path (str): the path of the inventory json file.
    """
    item=new_item_info()
    add_item(item,inventory_path)