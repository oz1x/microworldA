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
        self.xBound = 0
        self.yPos = 0
        self.yBound = 0
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

        if percepts.get('X') == 'r':
            return 'U'

        numTiles = {'N': 0, "E": 0, "S": 0, 'W': 0, 'X': 999999}


        #mapping function -- complete?
        for direction, path in percepts.items():
            if direction == 'X':
                continue
            i = 0
            if direction == 'N':
                for tile in path:
                    if self.yPos == 0:
                        self.memory[0:-1].insert(0, self.TileObj())
                        i += 1
                    self.memory[xPos][0] = self.TileObj(tile)
                self.yPos += i
            i = 0
            if direction == 'E':
                for tile in path:
                    if self.memory[xPos+1][yPos] != self.TileObj:
                        self.memory.append([self.TileObj()]*len(self.memory[0]))
                    self.memory[xPos+i][yPos] = self.TileObj(tile)
                    i += 1

            i = 0
            if direction == 'S':
                for tile in path:
                    if self.memory[xPos][yPos+1] != self.TileObj:
                        self.memory[0:-1].append(self.TileObj())
                    self.memory[xPos][yPos+i] = self.TileObj(tile)
                    i+=1

            i = 0
            if direction == 'W':
                for tile in path:
                    if self.xPos == 0:
                        self.memory.insert(0, [self.TileObj()] * len(self.memory[0]))
                        i += 1
                    self.memory[0][yPos] = self.TileObj(tile)
                self.xPos += i
            i = 0
        shortestPath = 999

        #choice function -- TODO: implement checking for if entire path is 
        #visited; if so, disregard path
        for direction in percepts:
            if direction == 'X':
                continue
            
            numTilesInPath = 0
            if direction == 'N':
                while self.memory[xPos][yPos+i].typeOfTile != 'W':
                    if self.memory[xPos][yPos+i].typeOfTile == 'r':
                        choice = direction
                        return choice
                    if self.memory[xPos][yPos+i].isVisited():
                        break
                    numTiles[direction] += 1
                    

        self.previousChoice = choice
        print("Picked direction " + choice + " with length " + str(shortest))
        
        return choice
    
