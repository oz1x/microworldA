# NAME(S): Dylan Andrews, Ozwin Cordes
#
# APPROACH: [WRITE AN OVERVIEW OF YOUR APPROACH HERE.]
#     Please use multiple lines (< ~80-100 char) for you approach write-up.
#     Keep it readable. In other words, don't write
#     the whole damned thing on one super long line.
#
#     In-code comments DO NOT count as a description of
#     of your approach.

import random


class AI:

    class TileObj:

        def __init__(self, tileType='w'):
            self.typeOfTile = tileType
            self.visited = 0

        def isVisited(self):
            return self.visited

        def setVisited(self):
            self.visited = 1
        
    
    def __init__(self):
        """
        Called once before the sim starts. You may use this function
        to initialize any data or data structures you need.
        """
        self.turn = 0
        self.previousChoice = 'X'
        self.memory = [[self.TileObj]]
        self.xPos = 0
        self.yPos = 0
        opposites = {'N': 'S', 'S': 'N', 'E': 'W', 'W':'E', 'X': 'Y'}

    

    def update(self, percepts):
        """
        PERCEPTS:
        Called each turn. Parameter "percepts" is a dictionary containing
        nine entries with the following keys: X, N, NE, E, SE, S, SW, W, NW.
        Each entry's value is a single character giving the contents of the
        map cell in that direction. X gives the contents of the cell the agent
        is in.

        COMAMND:
        This function must return one of the following commands as a string:
        N, E, S, W, U

        N moves the agent north on the map (i.e. up)
        E moves the agent east
        S moves the agent south
        W moves the agent west
        U uses/activates the contents of the cell if it is useable. For
        example, stairs (o, b, y, p) will not move the agent automatically
        to the corresponding hex. The agent must 'U' the cell once in it
        to be transported.

        The same goes for goal hexes (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
        """

        if (self.memory[xPos][yPos].isVisited() == 0):
            self.memory[xPos][yPos].setVisited()

        numTiles = {'N': 0, "E": 0, "S": 0, 'W': 0, 'X': 999999}

        for direction, path in percepts.items():
            if direction == 'X':
                continue
            if direction == 'N':
                if direction != opposites[self.previousChoice]:
                    for tile in path:
                        self.memory.insert(xPos, [self.TileObj()] * len(self.memory[0]))
                        self.memory[xPos+1][yPos] = self.TileObj(i)
                        if tile == 'w':
                            break
                        if tile != 'w':
                            numTiles[direction] += 1
                        if tile == 'r':
                            choice = direction
                            return choice
                    
        shortest = 999
        for direction in percepts:
            print(numTiles[direction])
            if numTiles[direction] > 0:
                if numTiles[direction] < shortest:                    
                    choice = direction
                    shortest = numTiles[direction]

        if (percepts.get('X') == 'r'):
            choice = 'U'
        self.previousChoice = choice
        print("Picked direction " + choice + " with length " + str(shortest))
        
        return choice
    
