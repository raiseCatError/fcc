# Magic Square Solver
#
# Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.
#
# A magic square is a grid where every row, column, and diagonal adds up to the same number.
#

def solve_magic_square(grid):

    # Columns
    col0 = {(0,0), (1, 0), (2, 0)}
    col1 = {(0,1), (1, 1), (2, 1)}
    col2 = {(0,2), (1, 2), (2, 2)}

    # Rows
    row0 = {(0,0), (0, 1), (0, 2)}
    row1 = {(1,0), (1, 1), (1, 2)}
    row2 = {(2,0), (2, 1), (2, 2)}

    # Diagonals
    dia0 = {(0,0), (1,1), (2, 2)}
    dia1 = {(0,2), (1,1), (2, 0)}

    v0 = 0
    v1 = 0
    v2 = 0

    h0 = 0
    h1 = 0
    h2 = 0

    d0 = 0
    d1 = 0

    for i, x in enumerate(grid):
        for ii, y in enumerate(x):

            if grid[i][ii] == 0:
                
                if (i, ii) in col0:              
                    for c1, c2 in col1:
                        v0 += grid[c1][c2]
                    
                    for c1, c2 in col2:
                        v1 += grid[c1][c2]

                    if v0 != v1:
                        return "impossible"

                    variable = v0   
                    checker = 0       
                    for c1, c2 in col0:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]

                    v2 = variable + checker

                #

                elif (i, ii) in col1:
                    for c1, c2 in col0:
                        v0 += grid[c1][c2]
                    
                    for c1, c2 in col2:
                        v1 += grid[c1][c2]

                    if v0 != v1:
                        return "impossible"
                    
                    variable = v0   
                    checker = 0       
                    for c1, c2 in col1:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]

                    v2 = variable + checker

                #

                elif (i, ii) in col2:
                    for c1, c2 in col0:
                        v0 += grid[c1][c2]
                    
                    for c1, c2 in col1:
                        v1 += grid[c1][c2]

                    if v0 != v1:
                        return "impossible"

                    variable = v0   
                    checker = 0       
                    for c1, c2 in col2:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]
                    
                    v2 = variable + checker

                grid[i][ii] = variable

                # Rows
                for r1, r2 in row0:
                    h0 += grid[r1][r2]
                for r1, r2 in row1:
                    h1 += grid[r1][r2]
                for r1, r2 in row2:
                    h2 += grid[r1][r2]

                # Diagonals
                for x1, x2 in dia0:
                    d0 += grid[x1][x2]
                for x1, x2 in dia1:
                    d1 += grid[x1][x2]
                
                # Checkpoint
                if v0 == v1 == v2 == h0 == h1 == h2 == d0 == d1:
                    return variable
                else:
                    return 'impossible'

# FIXME: This square is currently more magical than I am.

# solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]])
# solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) 
# solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]])
# solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]])
# solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]])