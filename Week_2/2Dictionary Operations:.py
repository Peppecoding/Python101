# Dictionary Operations:

# Create two dictionaries: inventory_1 and inventory_2, representing the stock of items in two different stores.
# Each dictionary should have items as keys and quantities as values.
inventory_1 = {'apples': 30, 'bananas': 15}
inventory_2 = {'oranges': 20, 'peaches': 10}

# Merge the two inventories into a new dictionary named total_inventory
total_inventory = {**inventory_1, **inventory_2}


# Add a new item to one of the inventories and update total_inventory
inventory_1['grapes'] = 40
total_inventory = {**inventory_1, **inventory_2}

# Print out total_inventory.
print("Total inventory:", total_inventory)
1