from room import Room
from player import Player
from actions import Actions
import sys

# Declare all the rooms

roomitems = ['rock', 'stick', 'map', 'bag', 'key', 'gem', 'match']

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [roomitems[0], roomitems[1], roomitems[6]]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [roomitems[2], roomitems[3]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", roomitems[4]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [roomitems[5]]),
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
endGame = 0
print('!!!PREPARE TO START YOUR ADVENTURE!!!')

# Make a new player object that is currently in the 'outside' room.
name = input("WHAT! Is your name?!?!")
player = Player(name, room['outside'])
print(f'Hello {player.name}!')

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
commands = "E = Expect Room\n V = View Items on You\n M = Move"

while endGame < 1:
    print(f'\nYou are in room: {player.room.name}\n')
    print(f'{player.room.desc}\n')

    print("How do you want to proceed?\n")
    action = input('Commands: \n')
    print(Actions(action).M())
    if action.upper() == 'Q':
        endGame = 1
    elif action.upper() == 'E':
        print("E entered")
    elif action.upper() == 'V':
        print("V entered")
    elif action.upper() == 'M':
        print('M entered')
    else:
        print('Wrong action entered')
