stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}") # prints key and value for each item in inventory
        itemAsInt = int(v) 
        item_total += itemAsInt # add value to the total
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    tempDict = {value: addedItems.count(value) for value in addedItems} #value is the number of times the item appears in loot
    print(tempDict)

addToInventory(stuff, dragonLoot) # stuff is existing inventory, dragonLoot is what is added
#displayInventory(stuff)

# LIST TO DICTIONARY
#The addToInventory() function should return a dictionary that represents the updated inventory
# gold coin: 3 dagger: 1 ruby: 1