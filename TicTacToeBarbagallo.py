#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:48:24 2024

@author: ginabarbagallo
"""


import random
empty = "-"
board = []

def start_board():
    for i in range(3):
        row = [empty for i in range(3)]
        board.append(row)
    
    print(board)

positions = {
    'A1': (0, 0), 'A2': (1, 0), 'A3': (2, 0),
    'B1': (0, 1), 'B2': (1, 1), 'B3': (2, 1),
    'C1': (0, 2), 'C2': (1, 2), 'C3': (2, 2)
    }

def look_at_board():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
#check for win or tie
def win_tie_continue(player, moves):
    if board[0][0] == board[1][1] == board[2][2] == player:
        print("The winner is player:", player)
        return True
    elif board[0][0] == board[0][1] == board[0][2] == player:
        print("The winner is player:", player)
        return True
    elif board[1][0] == board[1][1] == board[1][2] == player:
        print("The winner is player:", player)
        return True
    elif board[2][0] == board[2][1] == board[2][2] == player:
        print("The winner is player:", player)
        return True
    elif board[0][0] == board[1][0] == board[2][0] == player:
        print("The winner is player:", player)
        return True
    elif board[0][1] == board[1][1] == board[2][1] == player:
        print("The winner is player:", player)
        return True
    elif board[0][2] == board[1][2] == board[2][2] == player:
        print("The winner is player:", player)
        return True
    elif board[2][0] == board[1][1] == board[0][2] == player:
        print("The winner is player:", player)
        return True
    elif moves == 9 :
        print("The game ends in a tie")
        return True
    else:
        return False


def tic_tac_toe():
    start_board()
    players = ["X", "0"]
    moves = 0
    player = random.choice(players)
    
    
    #asking for input
    while True: 
        position = input("Choose a position:")
        
    #Checking the input is correct
        if position not in positions: 
            print("Enter the correct format A1 to C3")
            continue
        row, col = positions[position]
    #Checking input is not taken
        if board[row][col] == empty: 
            board[row][col]= player
            moves +=1
        else:
            print("That position is taken")
            continue

        if win_tie_continue(player, moves) == True:
            break
        look_at_board()
        
        #switch the player
        if player == "X": 
            player = "0"
        else:
            player = "X"
   
tic_tac_toe()
