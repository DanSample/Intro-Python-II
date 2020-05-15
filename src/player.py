# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def display_info(self):
        print(f'{self.current_room}')

    def display_items(self):
        item_list = ", ".join(str(x) for x in self.current_room.items)
        print(f'Items: {item_list}')

    def add_item(self, item):
        # self.item = item
        self.current_room.items.append(item)
        print(f"{item.name} was added to the room!")

    def drop_item(self, item):
        # self.item = item
        self.inventory.remove(item)
        self.current_room.items.append(item)
        
                
    def take_item(self, item):
        # self.item = item   
         self.inventory.append(item)
         self.current_room.items.remove(item)
         
                
    def display_inventory(self):
        item_list = ", ".join(str(x) for x in self.inventory)
        print(f'Inventory: {item_list}')