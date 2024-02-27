class Item:
    def __init__(self, name, description):  # Add a default value for description
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Removed the duplicate get_description method
    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def display_item(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")

# Instantiate items with both name and description
sword = Item("Sword", "You got the hero sword")
key = Item("Key", "You got the Master Key")  # The name should be "Key" not "key" based on your description
shield = Item("Shield", "You got the Zelda shield")  # The name should be "Shield" not "shield" based on your description


sword.display_item()

