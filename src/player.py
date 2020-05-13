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

        possible_direction = {
            'n': 'n_to',
            's': 's_to',
            'e': 'e_to',
            'w': 'w_to'
        }
        try:
            self.current_room = getattr(self.current_room, possible_direction[direction])
        except AttributeError:
            print("You cannot move in that direction")