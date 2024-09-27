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
        self.turn = 0
        self.previousChoice = 'X'
        self.memory = [[self.TileObj()]]
        self.xPos = 0
        self.xBound = 0
        self.yPos = 0
        self.yBound = 0
        self.backTrackStack = []
        self.flagNoNewTiles = 0
        self.opposites = {'N': 'S', 'S': 'N', 'E': 'W', 'W':'E', 'X': 'Y'}

    

    def update(self, percepts):

        print(self.memory[self.xPos][self.yPos])

        if (self.memory[self.xPos][self.yPos].isVisited() == 0):
            self.memory[self.xPos][self.yPos].setVisited()

        if percepts.get('X')[0] == 'r':
            return 'U'


        #mapping function -- complete?
        for direction, path in percepts.items():
            if direction == 'X':
                continue
            i = 1
            if direction == 'N':
                atEdge = 0
                if self.yPos == 0:
                    atEdge = 1
                for tile in path:
                    if atEdge == 1:
                        for sublist in self.memory:
                            sublist.insert(0, self.TileObj())
                        self.yPos += 1
                    self.memory[self.xPos][self.yPos-i].typeOfTile = tile

                    i += 1
            i = 1
            if direction == 'E':
                for tile in path:
                    if self.xPos+i+1 > len(self.memory):
                        self.memory.append([self.TileObj() for i in range(len(self.memory[0]))])
                    self.memory[self.xPos+i][self.yPos].typeOfTile = tile
                    i += 1

            i = 1
            if direction == 'S':
                for tile in path:
                    if self.yPos+i+1 > len(self.memory[self.xPos]):
                        for sublist in self.memory:
                            sublist.append(self.TileObj())
                    self.memory[self.xPos][self.yPos+i].typeOfTile = tile
                    i+=1

            i = 1
            if direction == 'W':
                atEdge = 0
                tilesOut = 0
                for tile in path:
                    if self.xPos - tilesOut == 0:
                        atEdge = 1
                    if atEdge == 1:
                        self.memory.insert(0, [self.TileObj() for i in range(len(self.memory[0]))])
                        self.xPos += 1
                    self.memory[self.xPos-i][self.yPos].typeOfTile = tile
                    i+=1
                    tilesOut+=1
            i = 1

        shortestPath = 999

        #choice function
        choice = 'x'
        for direction in percepts:
            if direction == 'X':
                choice = 'x'
                continue
            
            numTilesInPath = 0
            if direction == 'N':
                while self.memory[self.xPos][self.yPos-i].typeOfTile != 'w':
                    if self.memory[self.xPos][self.yPos-i].typeOfTile == 'r':
                        choice = direction
                        return choice
                    if self.memory[self.xPos][self.yPos-i].isVisited() == 0:
                        numTilesInPath += 1
                    i += 1

                if numTilesInPath < shortestPath and numTilesInPath > 0:
                    shortestPath = numTilesInPath
                    choice = direction

            i = 1
            numTilesInPath = 0
            if direction == 'E':
                while self.memory[self.xPos+i][self.yPos].typeOfTile != 'w':
                    if self.memory[self.xPos+i][self.yPos].typeOfTile == 'r':
                        choice = direction
                        return choice
                    if self.memory[self.xPos+i][self.yPos].isVisited() == 0:
                        numTilesInPath += 1
                    i += 1

                if numTilesInPath < shortestPath and numTilesInPath > 0:
                    shortestPath = numTilesInPath
                    choice = direction

            i = 1
            numTilesInPath = 0
            if direction == 'S':
                while self.memory[self.xPos][self.yPos+i].typeOfTile != 'w':
                    if self.memory[self.xPos][self.yPos+i].typeOfTile == 'r':
                        choice = direction
                        return choice
                    if self.memory[self.xPos][self.yPos+i].isVisited() == 0:
                        numTilesInPath += 1
                    i += 1

                if numTilesInPath < shortestPath and numTilesInPath > 0:
                    shortestPath = numTilesInPath
                    choice = direction
            
            i = 1
            numTilesInPath = 0
            if direction == 'W':
                while self.memory[self.xPos-i][self.yPos].typeOfTile != 'w':
                    if self.memory[self.xPos-i][self.yPos].typeOfTile == 'r':
                        choice = direction
                        return choice
                    if self.memory[self.xPos-i][self.yPos].isVisited() == 0:
                        numTilesInPath += 1
                    i += 1

                if numTilesInPath < shortestPath and numTilesInPath > 0:
                    shortestPath = numTilesInPath
                    choice = direction

                
        for direction in percepts:

            if direction == 'X':
                continue

            if direction == 'N':
                if choice == direction:
                    self.yPos -= 1

            if direction == 'E':
                if choice == direction:
                    self.xPos += 1

            if direction == 'S':
                if choice == direction:
                    self.yPos += 1

            if direction == 'W':
                if choice == direction:
                    self.xPos -= 1

        if choice == 'x':
            choice = self.opposites[self.backTrackStack.pop()]
            if choice == 'N':
                self.yPos -= 1
            if choice == 'E':
                self.xPos += 1
            if choice == 'S':
                self.yPos += 1
            if choice == 'W':
                self.xPos -= 1

            return choice
        
        self.backTrackStack.append(choice)


        self.previousChoice = choice
        
        return choice
    
