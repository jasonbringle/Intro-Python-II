# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        output = f"{self.name}, is in {self.current_room}. "
        return output
    def items_in_bag(self):
        if len(items) != 0:
            print(self.items)
        else:
            print("You don't have any items in your bag.  Git SOME!")
