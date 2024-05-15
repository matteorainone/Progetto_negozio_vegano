from commands import help_command,add_command,sell_command
from model import item_list, profit_calculator


def main():
    commands_list=["aiuto","aggiungi","elenca","vendita","profitti","chiudi"]
    inventory_path="stock_inventory.json"
    register_path="accounting_ledger.json"
    while True:
        try:
            user_command=input("Inserisci un comando: ")
            if user_command.lower() not in commands_list:
                print("Comando non valido")
                help_command()
            else:
                if user_command=="aiuto":
                    help_command()
                elif user_command=="aggiungi":
                    add_command(inventory_path)
                elif user_command=="elenca":
                    item_list(inventory_path)
                elif user_command=="vendita":
                    sell_command(inventory_path,register_path)
                elif user_command=="profitti":
                    profit_calculator(register_path)
                elif user_command=="chiudi":
                    print("Bye bye")
                    break
        except Exception as e:
            print("Si è verificato un errore", e)

if __name__=="__main__":
    main()

