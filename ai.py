

class AI:
    def __init__(self):
        """
        Called once before the sim starts.
        """
        self.turn = 0

    def update(self, percepts):
        """
        Called each turn. Parameter "percepts" is a dictionary containing
        five entries: X, N, E, S, W.
        X: single character string of what the agent is standing on.
        N: list of singel char strings of what the agent sees to the north (up).
        E: same as above but for east.
        S: same as above but for south.
        W: same as above but for west.

        Must return one of the following commands: 'N', 'E', 'S', 'W'.
        """
        # print(percepts)
        self.turn += 1
        oe = self.turn%2
        match oe:
            case 0: return 'F'
            case 1: return 'U'
            # case _: return 'F'
            # case _: return "F"
            # case 0 | 1: return "F"
            # case 2: return "R"
            # case 3 | 4: return "F"
            # case 5: return "L"
            # case 6 | 7: return "F"
            # case 8: return "R"
            # case 9 | 10 | 11 | 12 | 13: return "F"
            # case 14: return "L"
            # case 15 | 16 | 17: return "F"
            # case _: return "X"
    
