"""
Assuming a taxicab starts at the origin point (0,0) of the two-dimensional
grid of integers, initially facing north. It then executes the given sequence
of moves, given as a string made up of the characters 'L' for turning 90
degrees left (while standing in place), 'R' for turning 90 degrees right
(while standing in place) and 'F' for moving one step forward towards its
present heading. This function should return the final position of the taxicab
in the integer grid coordinates.
"""


def taxi_zum_zum(moves):
    direct = ['Y', 'X', '-Y', '-X']*100
    x, y, z = 0, 0, 0
    for idx in moves:
        if idx == 'L':
            z -= 1
        elif idx == 'R':
            z += 1
        else:
            if direct[z] == 'Y':
                y += 1
            elif direct[z] == 'X':
                x += 1
            elif direct[z] == '-Y':
                y -= 1
            else:
                x -= 1
    return (x, y)
