from character import Enemy, Friendly

# Enemy instance
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Do you think I need to take a shower?")
dave.talk()
dave.set_weakness("cheese")

# Friendly instance
bob = Friendly("Bob", "A helpful bystander")
bob.set_help("The weapon you need to use is a food made from milk")
bob.offer_help()

# Fighting with the enemy
weapon = input("\nWhat will you fight with?\n >> ")
if not dave.fight(weapon):
    print("You need more health!")
    bob.give_health(10)  # Bob gives health to the player

# Check health status
print(f"Your current health is {dave.health}.")
