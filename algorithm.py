import pygame
from sudoku_grid import grid     # Import the grid from sudoku_grid.py

length = len(grid)

def isValid(ik, jk, num):
    for k in range(length):
        if grid[ik][k] == num or grid[k][jk] == num:
            return False

    x = ik // 3 * 3
    y = jk // 3 * 3
    for k in range(3):
        for l in range(3):
            if grid[x + k][y + l] == num:
                return False
    return True

def isEmpty(ik, jk):
    return grid[ik][jk] == 0

def Solve(window, buffer, font, Background_Colour):
    for i in range(length):
        for j in range(length):
            if isEmpty(i, j):
                for num in range(1, 10):
                    if isValid(i, j, num):
                        grid[i][j] = num
                        pygame.draw.rect(window, Background_Colour, ((j+1)*50 + buffer, (i+1)*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                        value = font.render(str(num), True, (0, 0, 0))
                        window.blit(value, ((j+1)*50 + 15, (i+1)*50))
                        pygame.display.update()
                        pygame.time.delay(5)  # Adjust the delay here
                        if Solve(window, buffer, font, Background_Colour):
                            return True
                        grid[i][j] = 0
                return False
    return True
