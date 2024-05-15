import json

#valutare di inserirla direttamente nel main
def load_config():
    """
    Function that enables to load the parameters used by the functions
    """
    with open("config.json", "r") as file:
            vegan_params = json.load(file)
    return vegan_params

#software_params = load_config()