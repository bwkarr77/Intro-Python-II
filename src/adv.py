from room import Room
from player import Player
import inspect
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
    #
    print(f'You are holding: {player.items}\n')
    print(f'You see the following items in your current room: {player.room.items}\n')
    print('_____________________\n')
    #
    moveD = str(input('Enter in command:\n N, S, W, E to attempt to move to a different room\n "Q" to quit\n "get ['
                      'item]" or "drop [item]" : ')).lower()
    print('\n')
    #
    if moveD == 'q':
        print("You have given up on life, and pass away....")
        sys.exit('THE END')
    elif moveD == 'n' or moveD == "s" or moveD == 'e' or moveD == 'w':
        x1 = f'{moveD}_to'
        if getattr(player.room, x1):
            player.moveRoom(getattr(player.room, x1))
            print(f'{player.name} moved to room: {player.room.name}')
        else:
            print('None shall pass!!! Try again')
    else:
        print('Invalid input. Try again.')

    # elif moveD == 'get [item]':
        # pick up stuff
    # elif moveD == 'drop [item]':
        # drop stuff




