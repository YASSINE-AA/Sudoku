
from random import choice
from ntpath import join
from boards_available import *
from app_class import *
import sys

# Solver
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = '0'
    return False

            

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

# Checks if user input is valid
def valid_to_place(bo, num, pos, row, col):
    # Check row
    for i in range(len(bo[0])):
        if bo[row][col] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[row][col] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if isinstance(bo[i][j], str): # This must be the dumbest way of doing things but hey, it works!
                return (i, j)  # row, col
    return None


# Converts boards to strings
def converter():
    board_converted = ''
    for x in range(9):
        for z in range(9):
            board_converted += str(board_used[x][z]) 
    return board_converted

def convert_on_demand(board):
    board_converted_on_demand = ''

    for x in range(9):
        for z in range(9):
            board_converted_on_demand += str(board[x][z]) 
    return board_converted_on_demand


def solve_converter():
    board_converted_solved = ''
    for x in range(9):
        for z in range(9):
            board_converted_solved += str(board_solved[x][z]) 
    return board_converted_solved

