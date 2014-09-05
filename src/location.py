
class Location(object):
    # A list of item names in this location
    items = []

    # An array of congruent locations where a player
    # could go from here
    exits = {}

    # Information describing this place
    name = ''
    description = ''

    def __init__(self, name, description, items=[], exits={}, **kwargs):
        self.name = name
        self.description = description
        self.items = items
        self.exits = exits
