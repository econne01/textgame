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
        '''
                        Deepest-Cave
        Cave-Floor      Deep-Cave
        Cave-Entrance   Lakefront       Lake
        Cave-Front      Hut
        Meadow
        '''
        self.locations['cave_attic'] = Location(
            name = 'cave_attic',
            description = '''
            You are balanced on a narrow ledge high above the cave floor.
            The ground is slippery.''',
            exits = {
                'down': 'cave_floor',
            }
        )
        self.locations['cave_floor'] = Location(
            name = 'cave_floor',
            description = '''
            You are in the depths of the cave.
            A waterfall runs down the far wall.''',
            exits = {
                'south': 'cave_entrance',
                'east': 'deep_cave',
            }
        )
        self.locations['cave_entrance'] = Location(
            name = 'cave_entrance',
            description = '''
            You are in the mouth of a dark cave.
            Water is dripping from the ceiling and the air is warm and humid''',
            items = ['gold key'],
            exits = {
                'north': 'cave_floor',
                'south': 'cave_front',
                'east': 'lake_front',
            }
        )
        self.locations['lake_front'] = Location(
            name = 'lake_front',
            description = '''
            The cave opens up into a cavern. The ceiling is covered with stalagmites.
            Next to you is a dark lake.''',
            items = [],
            exits = {
                'west': 'cave_entrance',
                'north': 'deep_cave',
            }
        )
        self.locations['lake'] = Location(
            name = 'lake',
            description = '''
            You dive into the lake, which is surprisingly warm.
            The water is calm.''',
            exits = {
                'west': 'lake_front',
            }
        )
        self.locations['deep_cave'] = Location(
            name = 'deep_cave',
            description = '''
            You are deep in a cave.
            You can hear water running down the walls and the ground
            is very wet.  Strange noises can be heard somewhere deeper
            in the cave.''',
            exits = {
                'south': 'lake_front',
                'west': 'cave_floor',
            }
        )
        self.locations['cave_front'] = Location(
            name = 'cave_front',
            description = '''
            You stand before a dark cave. A rumble echoes from inside.''',
            exits = {
                'north': 'cave_entrance',
                'east': 'hut_front',
                'south': 'meadow',
            }
        )
        self.locations['hut_front'] = Location(
            name = 'hut_front',
            description = '''
            There is a creaky looking hut here. Smoke is pouring out of the chimney and it smells like ginger tea''',
            exits = {
                'west': 'cave_front',
                'inside hut': 'hut_inside',
            }
        )
        self.locations['hut_inside'] = Location(
            name = 'hut_inside',
            description = '''
            You are inside a small hut. A pot on the stove bubbles over and hisses.''',
            exits = {
                'outside': 'hut_front',
            }
        )
        self.locations['meadow'] = Location(
            name = 'meadow',
            description = '''
                A calm meadow. Nothing much to see.''',
            items = [],
            exits = {
                'north': 'cave_front'
            }
        )

        self.current_location = self.locations['cave_entrance']
