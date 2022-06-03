import pygame
import MineralNodes

res = (720, 720)

speed = 5

gold = pygame.Color(255, 215, 0)
silver = pygame.Color(192, 192, 192)
bronze = pygame.Color(140, 120, 83)
black = pygame.Color(0, 0, 0)

player_color = pygame.Color(89, 203, 232)

pygame.init()
pygame.display.set_caption("Resource Gathering")
game_window = pygame.display.set_mode(res)
clock = pygame.time.Clock()

player_position = [360, 360]

direction = 'RIGHT'
change_to = direction

MineralNodes.generateCoordinates("minNode_coordinates.txt")
minerals = MineralNodes.generateNodes()

for x in range(len(minerals)):
    val = minerals[x].get_value()
    i, j = minerals[x].get_coordinates()

    if val == 10:
        pygame.draw.rect(game_window, bronze, pygame.Rect(i * 72, j * 72, 20, 20))
    elif val == 50:
        pygame.draw.rect(game_window, silver, pygame.Rect(i * 72, j * 72, 20, 20))
    else:
        pygame.draw.rect(game_window, gold, pygame.Rect(i * 72, j * 72, 20, 20))


def game_over():
    pygame.quit()
    quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP':
        player_position[1] -= 20
    if change_to == 'DOWN':
        player_position[1] += 20
    if change_to == 'LEFT':
        player_position[0] -= 20
    if change_to == 'RIGHT':
        player_position[0] += 20
    
    game_window.fill(black)

    for x in range(len(minerals)):
        val = minerals[x].get_value()
        i, j = minerals[x].get_coordinates()

        if val == 10:
            pygame.draw.rect(game_window, bronze, pygame.Rect(i * 72, j * 72, 20, 20))
        elif val == 50:
            pygame.draw.rect(game_window, silver, pygame.Rect(i * 72, j * 72, 20, 20))
        else:
            pygame.draw.rect(game_window, gold, pygame.Rect(i * 72, j * 72, 20, 20))

    pygame.draw.rect(game_window, player_color, pygame.Rect(player_position[0], player_position[1], 20, 20))
    pygame.display.update()
    clock.tick(speed)
