# NAME(S): [PLACE YOUR NAME(S) HERE]
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

    def __init__(self):
        """
        Called once before the sim starts. You may use this function
        to initialize any data or data structures you need.
        """
        self.memory = [[self.TileObj]]
        self.lastDirection = 'X'
        self.currentDirection = 'X'
        self.xPos = 0
        self.yPos = 0
        
        self.opposites = {
            'X': 'X',
            'N': 'S',
            'S': 'N',
            'E': 'W',
            'W': 'E'
        }
    

        print("Thus begins the trials and tribulations of robot friend")

        self.turn = 0

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
        # 1. pick random directtion
        # 2. go direction until split
        # 3. pick random direction based on open options
        # 4. return to 2
        #x = input("Direction: ")
        #return x

        currentShortestPath = ['', 999]

        # on top of goal
        if percepts['X'][0] == 'r':
            print("YIPPPE")
            return('U')

        # TODO: add way to check if agent does not need to expand memory
        for key, values in percepts.items():
            if key == 'X':
                continue
            if key == 'N':
                for i in values:
                    self.memory[0:-1].insert(0, self.TileObj())
                    self.memory[xPos][0] = self.TileObj(i)
                    self.yPos += 1
            if key == 'E':
                for i in values:
                    self.memory.insert(xPos, [self.TileObj()]*len(self.memory[0]))
                    self.memory[xPos][yPos+1] = self.TileObj(i)
            if key == 'S':
                for i in values:
                    self.memory[0:-1].insert(yPos, self.TileObj)
                    self.memory[xPost+1][yPos] = self.TileObj(i)
            if key == 'W':
                for i in values:
                    self.memory.insert(0, [self.TileObj()]*len(self.memory[0]))
                    self.memory[0][yPos] = self.TileObj(i)
                    self.xPos += 1
                


        # start looking for shortest path if starting or in front of a wall
        if self.currentDirection == 'X' or percepts[self.currentDirection][0] == "w":
            wallCount = 0
            # for loop to find shortest path that is not a wall
            for key, values in percepts.items():
                
                # will go directly towards the goal 
                if values[-1] == 'r':
                    currentShortestPath[0] = key
                    currentShortestPath[0] = len(values)
                    break
                
                # ignore the 'X' percept, wall and last direction it came from
                if values[0] == 'w' or key == 'X' or key == self.opposites[self.lastDirection]:
                    if values[0] == 'w': wallCount += 1 
                    continue 
                
                # campare if direction is shorter than other paths
                if len(values) < currentShortestPath[1]:
                    currentShortestPath[0] = key
                    currentShortestPath[1] = len(values)
            
            # happens if in a space where last direction is only direction
            if currentShortestPath[0] == '':
                self.currentDirection = self.opposites[self.lastDirection]
            else:
                self.currentDirection = currentShortestPath[0]
                self.lastDirection = self.currentDirection
            # goes back further
            if wallCount >= 3:
                self.lastDirection = self.opposites[self.lastDirection]

            self.memory[0] = self.memory[1]
            self.memory[1] = self.currentDirection
            print(currentShortestPath)
        
        return self.currentDirection

        #return random.choice(['N', 'S', 'E', 'W'])
    
