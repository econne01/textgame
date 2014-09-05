from player import Player

class Game(object):
    ''' Abstract base class for a text-based game
        To implement: extend initalize method to
        instantiate some locations and items for the game
    '''
    items = {}
    locations = {}
    current_location = None
    player = None

    def initialize(self):
        ''' Declare the player and any locations or items
        '''
        self.player = Player()

    def begin(self):
        ''' Starts the game and a potentially endless
            sequence of turns
        '''
        self.look()
        self.new_turn()

    def new_turn(self):
        ''' Take an input command from user and try
            to parse it if command is allowed,
            otherwise alert user of available actions
        '''
        print '\n'
        command = raw_input('What should you do? ' + '\n')
        command = command.strip().lower()

        if command == '':
            print 'Please enter a command'

        # Handle exiting game
        elif command.split()[0] == 'exit':
            return

        # Handle change of location
        elif command in self.current_location.exits:
            self.change_location(command)
            self.look()

        # Handle picking up an item
        elif command.split()[0].lower() == 'pickup':
            item = ' '.join(command.split()[1:])
            self.pickup(item)

        # Handle dropping an item
        elif command.split()[0].lower() == 'drop':
            item = ' '.join(command.split()[1:])
            self.drop(item)

        # Handle looking around
        elif command.split()[0].lower() == 'look':
            item = ' '.join(command.split()[1:])
            self.look(item)

        # Handle checking item inventory
        elif command.split()[0].lower() == 'inventory':
            self.inventory()

        # Handle default case (unknown action)
        else:
            print 'You can\'t perform that action now. Your possible actions are {actions}'.format(
                actions = ', '.join(
                    ['look <item>', 'pickup <item>', 'drop <item>', 'inventory']
                    + self.current_location.exits.keys()
                    + ['exit']
                )
            )

        self.new_turn()

    def change_location(self, direction):
        ''' Move the player to a congruent location on the game's
            board map
            Example directions include north, south, east, west
        '''
        if direction in self.current_location.exits:
            self.current_location = self.locations[self.current_location.exits[direction]]
        else:
            print 'You cannot go {direction}'.format(direction=direction)

    def look(self, item_name=''):
        ''' Inspect the current location or a particular item
        '''
        if item_name:
            if item_name in self.player.items or item_name in self.current_location.items:
                print self.items[item_name].description
            else:
                print 'You can\'t look at {item_name} now.'.format(item_name=item_name)
        else:
            description = self.current_location.description
            if self.current_location.items:
                description += '\n' + 'There is a {items_list}'.format(
                    items_list = ', '.join([self.items[item].name for item in self.current_location.items])
                )
            description += '\n' + 'Exits: ' + ', '.join(self.current_location.exits)
            print description

    def drop(self, item_name):
        ''' Drop an item (if player is carrying it) in the
            current location
        '''
        if item_name in self.items and item_name in self.player.items:
            self.player.items.remove(item_name)
            self.current_location.items.append(item_name)
            print 'You have dropped the {item_name}'.format(item_name = item_name)
        else:
            print 'You do not have a {item_name}'.format(item_name = item_name)

    def pickup(self, item_name):
        ''' Pickup an item (if in current location) and add
            to players items
        '''
        if item_name in self.items and item_name in self.current_location.items:
            self.current_location.items.remove(item_name)
            self.player.items.append(item_name)
            print 'You have picked up the {item_name}'.format(item_name = item_name)
        else:
            print 'There is no {item_name} here'.format(item_name = item_name)

    def inventory(self):
        ''' Print out all items the player is carrying
        '''
        items = ', '.join(self.player.items)
        if items:
            print 'You have {items}'.format(items=items)
        else:
            print 'You do not have any items'
