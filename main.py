import json

def help():
    helpprint = print("""
    addcoins: plus Your coins.
    minuscoins: minus Your coins.
    help: shows this list.
    coins: Shows how many coins do you have
    """)
    main()
    

def checkbalance():
    with open('coins.json','r') as f:
        get_balance = json.loads(f.read())
        print(f"You Have {get_balance['coins']} coins")
        main()

def addcoins():
    addcoins = get_balance()
    coinamt = int(input("Enter a amount to add coins: "))
    addcoins['coins'] += coinamt

    with open('coins.json', 'w') as f:
        json.dump(addcoins, f)
    print("Add sucessfull")
    main()

def minuscoins():
    addcoins = get_balance()
    coinamt = int(input("Enter a amount to minus coins: "))
    addcoins['coins'] -= coinamt

    with open('coins.json', 'w') as f:
        json.dump(addcoins, f)
    print("Minus sucessfull")
    main()
    
        
def get_balance():
    with open('coins.json','r') as f:
        users = json.load(f)

        return users
        

def main():
    mainFunction = input("Input a Command(Type help for help): ")
    
    if mainFunction == "help":
        help()
    elif mainFunction == "coins":
        checkbalance()
    elif mainFunction == "addcoins":
        addcoins()
    elif mainFunction == "minuscoins":
        minuscoins()
    else:
        print("Command Not Found")
        main()

main()