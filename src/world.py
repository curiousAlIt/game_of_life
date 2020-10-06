#
# world.py - the world object in our game of life.
#

import numpy as np
import matplotlib.pyplot as plt

class World(object):

    def __init__(self, height, width):

        plt.ion()

        print('\n\nInitializing the world...')

        self.height = height
        self.width = width
        self.S = np.zeros([height, width], bool)

        print(f'We created a world of size {self.S.shape}')

        self.S[0, 0] = True
        self.S[height-1, 0] = True
        self.S[0, width-1] = True
        self.S[height-1, width-1] = True

        print(f'The world is initialized with these values: \n\n{self.S}\n\n')

        return

    def display_world(self):

        plt.figure()
        plt.imshow(self.S)
        title_str = f'Our world of size {self.height} by {self.width}'
        plt.title(title_str)
        plt.axis('off')
        plt.draw()
        plt.grid('on')

        return

    
