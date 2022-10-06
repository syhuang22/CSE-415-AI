'''EightPuzzleWithManhattan.py
by Angus Hsieh & James Huang
UWNetID: angush
UW NetID: sysh
Student number: 1831748
Student number: 1830445

Assignment 2, Part 2, in CSE 415, Spring 2021.'''

from EightPuzzle import *

# Calculate the heuristic by summing total Manhattan distance of 8 tiles
# Get coordinates of each tile from both initial state and goal state
# Minus the difference and sum them up to get heuristic
def h(s):
    sum = 0
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    if s == State(goal):
        return 0
    for i in range(1, 9):
        (x, y) = (0, 0)
        (gx, gy) = (0, 0)
        for j in range(3):
            for k in range (3):
                if s.b[j][k] == i:
                    (x, y) = (j, k)
                if goal[j][k] == i:
                    (gx, gy) = (j, k)
        sum += abs(gx - x) + abs(gy - y)
    return sum
