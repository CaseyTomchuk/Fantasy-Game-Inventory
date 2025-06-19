stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}") # prints key and value for each item in inventory
        itemAsInt = int(v) 
        item_total += itemAsInt # add value to the total
    print("Total number of items: " + str(item_total))

displayInventory(stuff)