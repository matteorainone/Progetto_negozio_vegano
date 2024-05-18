from model import add_item
from input import info_builder

def add_command(inventory_path:str):
    """
    A function used to manage the add command required from the user.

    Args:
        inventory_path (str): the path of the inventory json file.
    """
    item=info_builder(inventory_path)
    add_item(item,inventory_path)