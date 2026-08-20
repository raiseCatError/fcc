# Magic Square Solver
#
# Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.
#
# A magic square is a grid where every row, column, and diagonal adds up to the same number.
#

def solve_magic_square(grid):

    # Grid
    # grid = [
    #     [2, 7, 6], 
    #     [9, 0, 1], 
    #     [4, 3, 8]
    #     ]

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

    s = 0
    s2 = 0
    
    r = 0
    r2 = 0

    # Gosh, I need to freakin add a way to store the 0,and then check every row/column/diagonal, goanna do it later if this bruteforce works lmao

    # Update: decided to scratch this, and rebuild code lmaoo this is horrendus to look at...


    for i, x in enumerate(grid):
        for ii, y in enumerate(x):

            if grid[i][ii] == 0:

                if (i, ii) in col0:              
                    for c1, c2 in col1:
                        s += grid[c1][c2]
                    
                    for c1, c2 in col2:
                        s2 += grid[c1][c2]

                    if s != s2:
                        return "impossible"

                    variable = s   
                    checker = 0       
                    for c1, c2 in col0:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]

                    if variable + checker == s:
                        return variable
                    elif variable + checker != s:
                        return "impossible"

                elif (i, ii) in col1:
                    for c1, c2 in col0:
                        s += grid[c1][c2]
                    
                    for c1, c2 in col2:
                        s2 += grid[c1][c2]

                    if s != s2:
                        return "impossible"
                    
                    variable = s   
                    checker = 0       
                    for c1, c2 in col1:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]

                    if variable + checker == s:
                        return variable
                    elif variable + checker != s:
                        return "impossible"

                elif (i, ii) in col2:
                    for c1, c2 in col0:
                        s += grid[c1][c2]
                    
                    for c1, c2 in col1:
                        s2 += grid[c1][c2]

                    if s1 != s2:
                        return "impossible"

                    variable = s   
                    checker = 0       
                    for c1, c2 in col2:
                        variable -= grid[c1][c2]
                        checker += grid[c1][c2]

                    if variable + checker == s:
                        return variable
                    elif variable + checker != s:
                        return "impossible"

# solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]])
solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) 
# solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]])
# solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]])
# solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]])


