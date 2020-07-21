from room import Room
from player import Player
import inspect
import sys

# Declare all the rooms

roomitems = ['rock', 'stick', 'map', 'bag', 'key', 'gem', 'match']

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

room['outside'].items = [roomitems[0], roomitems[1], roomitems[6]]
room['foyer'].items = [roomitems[2], roomitems[3]]
room['overlook'].items = [roomitems[4]]
room['narrow'].items = []
room['treasure'].items = [roomitems[5]]

room['outside'].room_id = 'outside'
room['foyer'].room_id = 'foyer'
room['overlook'].room_id = 'overlook'
room['narrow'].room_id = 'narrow'
room['treasure'].room_id = 'treasure'

#
# Main
#
endGame = 0
print('!!!PREPARE TO START YOUR ADVENTURE!!!')

# Make a new player object that is currently in the 'outside' room.
name = input("WHAT! Is your name?!?!")
player = Player(name, room['outside'])
print(f'\nHello {player.name}!')

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
    print(f'You are in room: {player.room.name}')
    print(f'{player.room.desc}')
    #
    print(f'You are holding: {player.items}')
    print(f'You see the following items in your current room: {player.room.items}')
    print('_____________________\n')
    #
    print('Command Options:\n "N", "S", "W", "E" to attempt to move to a different room\n "Q" to quit\n "get [item]" or "drop [item]"')
    playerAction = str(input('Enter in command: ')).lower()
    # turns playerAction into an array of single words
    playerActionArr = playerAction.split(' ')
    print('\n')
    #
    if playerAction == 'q':
        print("You have given up on life, and pass away....")
        sys.exit('THE END')
    elif playerAction == 'n' or playerAction == "s" or playerAction == 'e' or playerAction == 'w':
        x1 = f'{playerAction}_to'
        if getattr(player.room, x1):
            player.moveRoom(getattr(player.room, x1))
            print(f'{player.name} moved to room: {player.room.name}')
        else:
            print('None shall pass!!! Try again')
    # checks if first word is "get"
    elif playerActionArr[0] == 'get' and len(playerActionArr) > 1:
        itemName = playerActionArr[1]
        if itemName:
            if itemName in player.room.items:
                # player picks up an item
                player.grabItem(itemName)
                print(f'You picked up {itemName}')
                # room loses an item
                room[player.room.room_id].itemRemoved(itemName)
            else:
                print(f'{itemName} is not found in this room.')
        else:
            print("invalid input, choose a proper command to proceed")
    # checks if first word is "drop"
    elif playerActionArr[0] == 'drop' and len(playerActionArr) > 1:
        itemName = playerActionArr[1]
        if itemName:
            if itemName in player.items:
                player.dropItem(itemName)
                print(f'You dropped {itemName}')
                # room gains item
                room[player.room.room_id].itemLeft(itemName)
            else:
                print(f"You are not holding {itemName}")
        else:
            print('Invalid input. Correct input is "drop [item]".')
    else:
        print('Invalid input. Try again.')
