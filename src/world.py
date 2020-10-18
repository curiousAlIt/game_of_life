#
# world.py - the world object in our game of life.
#

import numpy as np
import matplotlib.pyplot as plt
import random

class World(object):

    def __init__(self, height, width):

        self.DBG = False

        plt.ion()

        if self.DBG:
            print('\n\nInitializing the world...')

        self.height = height
        self.width = width
        self.S = np.zeros([height, width], bool)

        if self.DBG:
            print(f'We created a world of size {self.S.shape}')

        self.S[0, 0] = True
        self.S[height-1, 0] = True
        self.S[0, width-1] = True
        self.S[height-1, width-1] = True

        if self.DBG:
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

    def set_to_random(self, prob_of_living = 0.25):

        for row in range (0, self.height):
            for col in range (0, self.width):

                rr = random.random()

                if self.DBG:
                    print(f'In position {row, col} the random was {rr}')

                if rr < prob_of_living:
                    self.S[row, col] = True
                else:
                    self.S[row, col] = False
                # if alive
            # next column
        # next row

        return


    def number_of_living_neighbors(self):

        A = np.zeros([self.height, self.width], int)

        for r in range (0, self.height):
            for c in range (0, self.width):

                if (r==0) and (c==0):
                    A[r, c] = self.S[r, c+1] + self.S[r+1, c+1] + self.S[r+1, c]

                elif (r==0) and (c < self.width-1):
                    A[r, c] = self.S[r, c-1] + self.S[r+1, c-1] + self.S[r, c+1] + self.S[r+1, c+1] + self.S[r+1, c]

                elif r==0 and c==self.width-1:
                    A[r, c] = self.S[r, c-1] + self.S[r+1, c-1] + self.S[r+1, c]

                elif r < self.height-1 and c==0:
                    A[r, c] = self.S[r-1, c] + self.S[r-1, c+1] + self.S[r, c+1] + self.S[r+1, c+1] + self.S[r+1, c]

                elif r < self.height-1 and c < self.width - 1:
                    A[r, c] = self.S[r-1, c] + self.S[r-1, c+1] + self.S[r, c+1] + self.S[r+1, c+1] + self.S[r+1, c] + self.S[r+1, c-1] + self.S[r, c-1] + self.S[r-1, c-1]

                elif r < self.height-1 and c == self.width-1:
                    A[r, c] = self.S[r-1, c] + self.S[r+1, c] + self.S[r+1, c-1] + self.S[r, c-1] + self.S[r-1, c-1]

                elif r == self.height-1 and c==0:
                    A[r, c] = self.S[r-1, c] + self.S[r-1, c+1] + self.S[r, c+1]

                elif r==self.height-1 and c < self.width-1:
                    A[r, c] = self.S[r-1, c] + self.S[r-1, c+1] + self.S[r, c+1] + self.S[r, c-1] + self.S[r-1, c-1]

                elif r == self.height-1 and c == self.width-1:
                    A[r, c] = self.S[r-1, c] + self.S[r, c-1] + self.S[r-1, c-1]

            # next column
        # next row

        return A
        
