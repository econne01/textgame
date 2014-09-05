from game import Game
from game.character import Character

class Troll(Character):
    description = 'A tall and brooding troll. He does not seem like he ever looks pleased.'

    def speak_to(self, phrase):
        ''' Defines what the character will say when prompted with "phrase"
        '''
        self.answer('No habla english')
        self.squash()

    def squash(self):
        ''' Squash the player
        '''
        print 'The troll squashes you with his club'
        Game.gameover()
