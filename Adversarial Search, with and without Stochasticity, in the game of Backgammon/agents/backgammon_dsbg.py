'''
Name(s): Angus Hsieh
UW netid(s): angush
'''

from game_engine import genmoves
import math
W = 0
R = 1

class BackgammonPlayer:
    def __init__(self):
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxPly = 2
        self.evuF = None
        self.pruning = False
        self.numberOfStates = 0
        self.alphaBetaCutoff = 0
        self.specialFunction = 0
        self.finalMove = None
        # feel free to create more instance variables as needed.

    # return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # return a string representation of your UW netid(s)
        return "angush" + " " + "sysh"

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # use the prune flag to indiciate what search alg to use
        self.numberOfStates = 0
        self.alphaBetaCutoff = 0
        if prune is True:
            self.pruning = True
        else:
            self.pruning = False

    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        return self.numberOfStates, self.alphaBetaCutoff

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
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
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1=1, die2=6):
        self.finalMove = None
        # return a move for the current state and for the current player.
        # Hint: you can get the current player with state.whose_move
        if self.pruning is False:
            minimax = self.miniMax(state, state.whose_move, die1, die2, self.maxPly)
            if self.finalMove is None:
                return 'p'
            return self.finalMove
        else:
            alphapruning = self.alphaPruning(state, state.whose_move, die1, die2, float('-inf'), float('inf'), self.maxPly)
            if self.finalMove is None:
                return 'p'
            return self.finalMove

    def miniMax(self, state, whoseMove, die1, die2, plyLeft):
        self.numberOfStates += 1
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
                    newVal = self.miniMax(s[1], 1, die1, die2, plyLeft - 1)
                    if newVal > maxEval:
                        maxEval = newVal
                        self.finalMove = s[0]
            return maxEval
        else:
            minEval = float('inf')
            for s in move_list:
                if s[0] != 'p':
                    newVal = self.miniMax(s[1], 0, die1, die2, plyLeft - 1)
                    if newVal < minEval:
                        minEval = newVal
                        self.finalMove = s[0]
            return minEval

    def alphaPruning(self, state, whoseMove, die1, die2, alpha, beta, plyLeft):
        self.numberOfStates += 1
        self.move_generator = self.GenMoveInstance.gen_moves(state, whoseMove, die1, die2)
        move_list = self.get_all_moves()
        if plyLeft == 0 or (len(move_list) == 1 and move_list[0] == 'p'):
            if self.evuF is not None:
                return self.evuF(state)
            else:
                return self.staticEval(state)
        if whoseMove == W:
            maxEval = float('-inf')
            for s in move_list:
                newVal = self.alphaPruning(s[1], 1, die1, die2, alpha, beta, plyLeft - 1)
                if newVal > maxEval:
                    maxEval = newVal
                    self.finalMove = s[0]
                alpha = max(alpha, maxEval)
                if beta <= alpha:
                    self.alphaBetaCutoff += 1
                    break
            return maxEval
        else:
            minEval = float('inf')
            for s in move_list:
                newVal = self.alphaPruning(s[1], 0, die1, die2, alpha, beta, plyLeft - 1)
                if newVal < minEval:
                    minEval = newVal
                    self.finalMove = s[0]
                beta = min(beta, minEval)
                if beta <= alpha:
                    self.alphaBetaCutoff += 1
                    break
            return minEval

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
