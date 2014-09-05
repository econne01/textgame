import os, sys
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from game import CaveGame

if __name__ == '__main__':
    g = CaveGame()
    g.initialize()
    g.begin()
