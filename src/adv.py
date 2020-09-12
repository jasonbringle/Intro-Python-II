from room import Room
from player import Player
from weapon import Weapon

# Declare  all the rooms

sword = Weapon("Sword", "Sharp, ouch!!", 10000)

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[sword]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = ""
now = room["outside"]

while direction != "q":

    player = Player("JimBob", now, [])
    print(f"{player.name} is in the {now}")
    direction = input("\n Choose what to do! Select a direction to move... (n)orth (s)outh (e)ast (w)est, or see your (i)tems, (f)ind an item, or (g)rab an item").split(" ")
    move = str(direction[0])
    #You need to decide how to get the proper input for moving and for doing an action like picking up an item or leaving an item.
    if len(direction) == 2:
        action = direction[1]
    if action == "i":
        player.items_in_bag()
    try:
        
        if move == "n":
            if now.n_to is None:
                print("\n You cant go there! Try another way, dummy!\n")
            else:
                now = now.n_to
        if move == "s":
            if now.s_to is None:
                print("\n You cant go there! Try another way, dummy!\n")
            else:
                now = now.s_to
        if move == "e":
            if now.e_to is None:
                print("\n You cant go there! Try another way, dummy!\n")
            else:
                now = now.e_to
        if move == "w":
            if now.w_to is None:
                print("\n You cant go there! Try another way, dummy!\n")
            else:
                now = now.w_to
        if move == "q":
            print("You done playin?  Aight den.")
            break
        
    except ValueError:
        print("please enter a valid direction! (n,s,e,w)")




