#
# test_world.py - program to test and show how to use the world class.
#

from world import World

aw = World(3,6)
iw = World(150,250)

iw.set_to_random(0.005)
iw.display_world()

nln_aw = aw.number_of_living_neighbors()
print(nln_aw)
