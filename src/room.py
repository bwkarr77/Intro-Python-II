# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc, room_id='', items=[]):
        self.name = name
        self.desc = desc
        self.room_id = room_id
        self.n_to = ""
        self.s_to = ""
        self.w_to = ""
        self.e_to = ""
        self.items = items

    def itemRemoved(self, item):
        if item in self.items:
            self.items.remove(item)

    def itemLeft(self, item):
        self.items.append(item)

    def __str__(self):
        return f'name: {self.name}, description: {self.desc}, items: {self.items}'