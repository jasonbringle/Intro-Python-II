# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, room_desc, items = []):
        self.room_name = room_name
        self.room_desc = room_desc
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        output = self.room_name + " " + self.room_desc
        return output
