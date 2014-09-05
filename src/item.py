
class Item(object):
    # Information describing this place
    name = ''
    description = ''

    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description

