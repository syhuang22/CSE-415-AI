'''EightPuzzleWithHamming.py
by Angus Hsieh & James Huang
UWNetID: angush
UW NetID: sysh
Student number: 1831748
Student number: 1830445

Assignment 2, Part 2, in CSE 415, Spring 2021.'''


from EightPuzzle import *

# Calculate heuristic by Hamming distance
# Count the number of tiles out of place except the void tile
def h(s):
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    if s == State(goal):
        return 0
    sum = 0
    for i in range(3):
        for j in range(3):
            value = s.b[i][j]
            if value != 0 and value != goal[i][j]:
                sum += 1
    return sum
