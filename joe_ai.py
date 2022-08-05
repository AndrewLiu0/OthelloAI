#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
An AI player for Othello. This is the template file that you need to  
complete.

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time
import math

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

# computes the utility of a final game board state (in the format described above). 
# The utility is the number of disks of player color minus the number of disks of the opponent. 
# Hint: The function get_score(board) returns a tuple (number of dark disks, number of light disks).


# 1 is dark 2 is light
def compute_utility(board, color): 
    utility = 0

    if color == 1:
        utility = abs(get_score(board)[0] - get_score(board)[1])
    else: 
        utility = abs(get_score(board)[1] - get_score(board)[0])
    return utility




############ MINIMAX ###############################

def minimax_min_node(board, color):
    opp_color = 1 if color == 2 else 2
    color = opp_color
    if (len(get_possible_moves(board,color)) == 0):
        return compute_utility(board,color)
    else:
        possibleMoves = get_possible_moves(board,color)
        possibleMin = [] 
        for moves in possibleMoves:
            boardAfterMove = play_move(board,color,moves[0],moves[1])
            possibleMin.append(minimax_max_node(boardAfterMove,color))
        possibleMin.sort()
        return possibleMin[0]


def minimax_max_node(board, color):
    opp_color = 1 if color == 2 else 2
    if (len(get_possible_moves(board,color)) == 0):
        return compute_utility(board,color)
    else:
        possibleMoves = get_possible_moves(board,color)
        possibleMax = [] 
        for moves in possibleMoves:
            boardAfterMove = play_move(board,color,moves[0],moves[1])
            possibleMax.append(minimax_min_node(boardAfterMove,color))
        possibleMax.sort()
        return possibleMax[-1]

        
        

    
def select_move_minimax(board, color):
    GLOBAL_MAX = -math.inf
    GLOBAL_MAX_MOVE = (0,0)
    cornerMoves = getCornerMoves(board, color)
    previousUtility = -math.inf;
    if len(cornerMoves) != 0:
         for element in cornerMoves:
             if (compute_utility(play_move(board, color, element[0], element[1]), color) > previousUtility):
                 previousUtility = compute_utility(play_move(board, color, element[0], element[1]), color)                 
                 GLOBAL_MAX_MOVE = (element[0], element[1])
    else:
        for moves in get_possible_moves(board,color):
            boardAfterMove = play_move(board,color,moves[0],moves[1])
            min_node = minimax_min_node(boardAfterMove, color)
            if(min_node > GLOBAL_MAX):                
                GLOBAL_MAX = min_node
                GLOBAL_MAX_MOVE = moves

    print("now playing", GLOBAL_MAX_MOVE, file = sys.stderr)
    return GLOBAL_MAX_MOVE


def getCornerMoves(board, color):
    possibleMoves = get_possible_moves(board, color)
    cornerMoves = []
    for element in possibleMoves:
        if (element[0] == 0 and element[1] == 0):
            cornerMoves.append(element)
        elif (element[0] == 0 and element[1] == 3):
            cornerMoves.append(element)
        elif (element[0] == 3 and element[1] == 3):
            cornerMoves.append(element)
        elif (element[0] == 3 and element[1] == 0):
            cornerMoves.append(element) 
    return cornerMoves   
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Joe AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()