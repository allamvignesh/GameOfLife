import pygame
# from pygame.locals import *
import random

pygame.init()

size = (750, 600)
display = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
done = False

grid = [[random.choice([0, 1]) for _ in range(30)] for _ in range(30)]
run = False


def make_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[j][i]:
                rect = pygame.Surface((18, 18))
                rect.fill((255, 255, 255))
                display.blit(rect, (j*20, i*20))


def next_tick():
    temp = [list(i) for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = find_neighbors(i, j, temp)
            if temp[i][j] == 0 and neighbors == 3:
                grid[i][j] = 1
            elif temp[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                grid[i][j] = 0
            else:
                grid[i][j] = temp[i][j]


def find_neighbors(x, y, temp):
    total = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            row = x+i
            col = y+j
            if col > len(temp[0])-1:
                col = 0
            if row > len(temp)-1:
                row = 0
            total += temp[row][col]
    return total-temp[x][y]


def draw_grid():
    for i in range(len(grid)+1):
        pygame.draw.line(display, (51, 51, 51), ((i * 20), 0), (i * 20, 600), 2)
    for j in range(len(grid[0])+1):
        pygame.draw.line(display, (51, 51, 51), (0, (j * 20)), (600, j * 20), 2)


# noinspection PyArgumentList
def draw_buttons():
    global run

    start = pygame.Surface([100, 60])
    start.fill((46, 179, 55))
    display.blit(start, (620, 20))
    mouse_pos = pygame.mouse.get_pos()

    if 620 < mouse_pos[0] < 620+100 and 20 < mouse_pos[1] < 20+60:
        pygame.draw.rect(display, (255, 255, 255), (620, 20, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = True

    stop = pygame.Surface([100, 60])
    stop.fill((173, 35, 35))
    display.blit(stop, (620, 100))

    if 620 < mouse_pos[0] < 620+100 and 100 < mouse_pos[1] < 100+60:
        pygame.draw.rect(display, (255, 255, 255), (620, 100, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
            
    reset = pygame.Surface([100, 60])
    reset.fill((0, 0, 200))
    display.blit(reset, (620, 180))

    if 620 < mouse_pos[0] < 620+100 and 180 < mouse_pos[1] < 180+60:
        pygame.draw.rect(display, (255, 255, 255), (620, 180, 100, 60), 5)
        if pygame.mouse.get_pressed()[0]:
            run = False
            resetGrid()

def resetGrid():
    global grid
    grid = [[random.choice([0, 1]) for _ in range(30)] for _ in range(30)]
    
while not done:
    display.fill(0)

    make_grid()
    if run:
        next_tick()
    draw_grid()

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not run:
                mouse_pos = pygame.mouse.get_pos()

    pygame.display.flip()
    clock.tick(10)
