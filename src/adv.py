from room import Room
from player import Player
from item import Item

#Items

items = {
     "rock": Item("rock", "Doesn't look deadly, or valuable"),
     "stick": Item("stick", "Don't run with it, it could poke out an eye"),
     "sword": Item("sword", "Old and broken mid blade, may still be useful"),
     "torch": Item("torch", "Something much larger than a human would have to carry this"),
     "purse": Item("purse", "Sadly it is empty")
}
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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

possible_actions = {
    'n': 'n_to',
    's': 's_to',
    'e': 'e_to',
    'w': 'w_to'
}

def populate_items():
    rooms = room.items()
    the_items = items.items()
    for r, item in zip(rooms, the_items):
        setattr(r[1], 'items', [item[1]])

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

def welcome_player(player_name):
    welcome_msg = f'Welcome {player_name}!'
    return welcome_msg

def play_game(player):
    
    playing = True

    while playing:
        player.display_info()
        player.display_items()
        action = input('Which direction will you venture? ').lower()
        verb, *rest = action.split()
        item = rest[0] if len(rest) > 0 else None

        if verb in ('q'):
            playing = False
            print(f'Thank you for playing {player.name}!')

        elif verb in ('n','s', 'e', 'w'):
            direction = possible_actions[verb]
            room = getattr(player.current_room, direction)
            if room != None:
                player.current_room = room
            else:
                print(f'Unable to move {verb}, try again.')

        elif verb in ('take', 'get'):
            try:
                player.take_item(items[item])
                items[item].on_take()
            except:
                print("something went wrong")

        elif verb in ('drop'):
            try:
                player.drop_item(items[item])
                items[item].on_drop()
            except:
                print("something went wrong")
                
        elif verb in ('i', 'inventory'):
            player.display_inventory()


def main():
    player_name = input("What is your name adventurer? ")
    new_player = Player(player_name, room['outside'])
    populate_items()
    print(welcome_player(player_name))
    play_game(new_player)


if __name__ == "__main__":
    main()