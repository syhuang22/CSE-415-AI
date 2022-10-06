'''
Name(s):
UW netid(s):
'''

from game_engine import genmoves

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxPly = 2
        self.evuF = None
        self.specialFunction = 0
        self.finalMove = None

    def nickname(self):
        # return a string representation of your UW netid(s)
        return "angush" + " " + "sysh"

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. Count the chance nodes
    # as a ply too!
    def setMaxPly(self, maxply=2):
        self.maxPly = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        # update your staticEval function appropriately
        if func is not None:
            self.evuF = func
            self.specialFunction = 1
        else:
            self.specialFunction = 0

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1, die2):
        self.expectimax(state, state.whose_move, die1, die2, self.maxPly)
        if self.finalMove is None:
            return 'p'
        return self.finalMove

    def expectimax(self, state, whoseMove, die1, die2, plyLeft):
        self.move_generator = self.GenMoveInstance.gen_moves(state, whoseMove, die1, die2)
        move_list = self.get_all_moves()
        if plyLeft == 0 or (len(move_list) == 1 and move_list[0] == 'p'):
            if plyLeft == 0:
                if self.evuF is not None:
                    return self.evuF(state)
                else:
                    return self.staticEval(state)
        if whoseMove == 0:
            maxEval = float('-inf')
            for s in move_list:
                if s[0] != 'p':
                    newVal = self.expectimax(s[1], 1, die1, die2, plyLeft - 1)
                    if newVal > maxEval:
                        maxEval = newVal
                        self.finalMove = s[0]
            return maxEval
        else:
            expcVal = 0
            for s in move_list:
                if s[0] != 'p':
                    newVal = self.expectimax(s[1], 0, die1, die2, plyLeft - 1)
                    expcVal += (1/36) * newVal
            return expcVal


    def get_all_moves(self):
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                move = next(self.move_generator)
                # print("GG", move[0])
                if move[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(move)
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append('p')
        return move_list


    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    def staticEval(self, state):
        white = 0
        red = 0
        for i in range(24):
            white += (i + 1) * state.pointLists[i].count(0)
            red += -1 * (24 - i) * state.pointLists[i].count(1)
        white += 100 * len(state.white_off) + 500 * state.bar.count(0)
        red += -100 * len(state.red_off) + 700 * state.bar.count(1)
        if len(state.white_off) == 14:
            white += 5000
        if len(state.red_off) == 14:
            red -= 5000
        if len(state.white_off) == 15:
            white += 10000
        if len(state.red_off) == 15:
            red -= 10000
        return white + red
