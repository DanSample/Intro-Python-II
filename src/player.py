# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def display_info(self):
        print(self.current_room)

    def move_to(self, direction):
        self.direction = direction

        possible_directions = {
            'n': 'n_to',
            's': 's_to',
            'e': 'e_to',
            'w': 'w_to'
        }
        try:
            """ Takes in direction to choose from possible_directions, then using the getattr() method
            it selects the current_room attribute and returns it with the chosen direction set as its
            default value. Then assigns it to self.current_room. When the loop starts over and it calls 
            display_info(), self.current_room is whatever room is linked to the previous room in the chosen 
            direction"""
            self.current_room = getattr(self.current_room, possible_directions[direction])
        except AttributeError:
            print("You cannot move in that direction")