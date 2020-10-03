#
# world.py - the world object in our game of life.
#

import numpy as np

class World(object):

    def __init__(self, height, width):

        print('Initializing the world...')

        self.height = height
        self.width = width
        self.S = np.zeros([height, width], bool)

        print(f'We created a world of size {self.S.shape}')

        return
