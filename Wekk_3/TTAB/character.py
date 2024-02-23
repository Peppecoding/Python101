class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.health = 100  # Initial health

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        self.health -= 5  # Decrease health by 5 points
        if self.health <= 0:
            print(f"{self.name} has lost the fight and has no health left.")
            return False
        else:
            print(f"{self.name} fought bravely and now has {self.health} health left.")
            return True


class Enemy(Character):

    # Enemigoo
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakeness = item_weakness

    def get_weakeness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakeness:
            print(f"You fend {self.name} off with {combat_item}")
            return True
        else:
            print(f"Your {combat_item} is useless")
            print(f"{self.name} cruses you, puny adventurer")
            return False

class Friendly(Character):
    # Friendly
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.help = None

    def set_help(self, help_clue):
        self.help = help_clue

    def offer_help(self):
        if self.help:
            print(f"[{self.name} offers a clue]: {self.help}")
        else:
            print(f"{self.name} has no advice to offer right now.")