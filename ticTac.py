import numpy as np

board = np.zeros((3, 3), dtype=int)

# print(board)

def print_board(b):
    symbols = {0: " ", 1: "X", -1: "O"}
    for i in range(3):
        row = " | ".join(symbols[val] for val in b[i])
        print(" "+ row)
        if i < 2:
            print("---+---+---")
    print()

print_board(board)