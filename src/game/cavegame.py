from game import Game
from item import Item
from location import Location

class CaveGame(Game):

    def initialize(self):
        super(CaveGame, self).initialize()

        # Setup Items here
        self.items['gold key'] = Item(
            name = 'gold key',
            description = 'A gold key. Wonder what it unlocks...'
        )

        # Setup Locations here
        self.locations['cave'] = Location(
            name = 'cave',
            description = '''
            You are at the mouth of a dark cave.
            Water is dripping from the ceiling and the air is warm and humid''',
            items = ['gold key'],
            exits = {
                'north': 'deep_cave',
                'south': 'meadow'
            }
        )
        self.locations['deep_cave'] = Location(
            name = 'deep_cave',
            description = '''
            You are deep in a cave.
            You can hear water running down the walls and the ground
            is very wet.  Strange noises can be heard somewhere deeper
            in the cave.''',
            items = [],
            exits = {
                'south': 'cave'
            }
        )
        self.locations['meadow'] = Location(
            name = 'meadow',
            description = '''
                A calm meadow. Nothing much to see.''',
            items = [],
            exits = {
                'north': 'cave'
            }
        )

        self.current_location = self.locations['cave']
