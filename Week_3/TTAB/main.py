from room import Room
from character import Enemy

print("Welcome to the room")

# Creating instances of Room and description
kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("ballroom")
ballroom.set_description("A vast room")

dining_hall = Room("dining hall")
dining_hall.set_description("A large room with golden decorations")

# Linking the rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Do you think I need to take a shower?")
dave.set_weakness("cheese")

dining_hall.set_character(dave)

current_room = kitchen

while True:
    print ("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
            inhabitant.describe()
            weapon = input("\nWhat will you fight with?\n >>")
            dave.fight(weapon)
      
    command = input("> ")
    if command == "exit":
        break
    current_room = current_room.move(command)
