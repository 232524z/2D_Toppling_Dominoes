import numpy as np
import pandas as pd
from L_Dominoes import L
from nimber import Nimber
from game import Game

table_size = 100
L_table = L(table_size)

# Base cases for 1x and 2x Ls
for i in range(1, table_size + 1):
    L_table.set_value(1, i, i)
    L_table.set_value(2, i, i + 1)

# Runs through every dimension and calculates L value
for i in range(3, table_size + 1):
    for j in range(i, table_size + 1):

        # Array of nim values that can be reached by toppling every domino in every direction
        options = []
        for k in range(i + j - 1):
            options += L_table.find_options(i, j, k)
        L_value = Game.mex(options)
        L_table.set_value(i, j, L_value)

L_table.save_csv("L.csv")
L_table.save_image("L.png")
