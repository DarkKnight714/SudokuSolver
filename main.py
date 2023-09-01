import pygame
from sudoku_grid import grid  # Import the grid from sudoku_grid.py
from algorithm import Solve  # Import the Solve function from algorithm.py

WIDTH = 550
Background_Colour = (245, 251, 250)
buffer = 5


def draw_grid(window):
    # Draw the Sudoku grid
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        else:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

def draw_initial_values(window, font):
    # Fill in initial values
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] != 0:
                value_board = font.render(str(grid[i][j]), True, (52, 31, 151))
                window.blit(value_board, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))

    window.fill(Background_Colour)

    pygame.display.set_caption("Sudoku Solver")

    # Initialize your font
    font = pygame.font.SysFont('Comic Sans MS', 35)

    draw_grid(window)
    draw_initial_values(window, font)

    # Call solve from sudoku.py
    from algorithm import Solve
    Solve(window,buffer,font, Background_Colour)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
