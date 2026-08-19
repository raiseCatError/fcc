# Bucket Fill 2

# Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid the target color.

# Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
# Cells are connected horizontally and vertically (not diagonally).
# 

def bucket_fill(grid, target_color):

    visited = set()
    counter = 0

    def fill(i, j, original_color):
        if i < 0 or i >= len(grid):
            return

        if j < 0 or j >= len(grid[i]):
            return

        if (i, j) in visited:
            return

        if grid[i][j] != original_color:
            return

        # # Below
        # if i + 1 < len(grid):
        #     if (i + 1, j) not in visited and grid[i + 1][j] == original_color:
        #         visited.add((i + 1, j))
        #         grid[i + 1][j] = target_color
        # # Above
        # if i - 1 >= 0:
        #     if (i - 1, j) not in visited and grid[i - 1][j] == original_color:
        #         visited.add((i - 1, j))
        #         grid[i - 1][j] = target_color

        # # Right
        # if j + 1 < len(grid[i]):
        #     if (i, j + 1) not in visited and grid[i][j + 1] == original_color:
        #         visited.add((i, j + 1))
        #         grid[i][j + 1] = target_color

        # # Left
        # if j - 1 >= 0:
        #     if (i, j - 1) not in visited and grid[i][j - 1] == original_color:
        #         visited.add((i, j - 1))
        #         grid[i][j - 1] = target_color

        
        # if (i, j) not in visited and grid[i][j] == original_color:
        #     visited.add((i, j))
        #     grid[i][j] = target_color


        visited.add((i, j))
        grid[i][j] = target_color

        fill(i + 1, j, original_color)
        fill(i - 1, j, original_color)
        fill(i, j + 1, original_color)
        fill(i, j - 1, original_color)
                

    for i, x in enumerate(grid):
    # print('i',i)
        for j, y in enumerate(x):
            # print('x',x,'y',y,'i',i,'j',j)
            if (i, j) not in visited and grid[i][j] != target_color:
                # grid[i][j] = target_color
                counter += 1
                original_color = grid[i][j]
                fill(i, j, original_color)
                


    # print(visited)
    print(counter)

    return counter

bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R")

bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P")

bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y")

bucket_fill([["R", "R"], ["R", "R"]], "G")
