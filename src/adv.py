from room import Room
from player import Player
from item import Item

#Items

item = {
    'rock': Item("a small rock", "Doesn't look deadly, or valuable"),
    'stick': Item("a stick", "Don't run with it, it could poke out an eye"),
    'sword': Item("a broken sword", "Old and broken mid blade, may still be useful"),
    'torch': Item("a large torch", "Something much larger than a human would have to carry this"),
    'pouch': Item("a small coin purse", "Sadly it is empty")
}
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['rock']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['stick']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['sword']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['torch']),      

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['pouch']),
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

def welcome_player(player_name):
    welcome_msg = f'Welcome {player_name}!'
    return welcome_msg

def play_game(player):
    
    playing = True

    while playing:
        player.display_info()
        action = input('Which direction will you venture? ').lower()
        verb, *rest = action.split()
        item = rest[0] if len(rest) > 0 else None

        if(verb == 'q'):
            playing = False
            print(f'Thank you for playing {player.name}!')
        else:
            possible_actions = {
                "n": player.move_to,
                "s": player.move_to,
                "e": player.move_to,
                "w": player.move_to,
                "i": player.display_inventory(),
                "drop": player.drop_item,
                "take": player.take_item
            }
            try:
                """takes in the action to choose from possible_actions and then gives 
                the action to the move_to method on player"""
                if (verb == "i"):
                    possible_actions[verb]
                else:    
                    possible_actions[verb](item if item else verb) 
            except KeyError:
                print('Invalid direction, please choose a valid direction')


def main():
    player_name = input("What is your name adventurer? ")
    new_player = Player(player_name, room['outside'])
    print(welcome_player(player_name))
    play_game(new_player)


if __name__ == "__main__":
    main()