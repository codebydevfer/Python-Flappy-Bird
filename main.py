import random
import pygame

window_x = 720
window_y = 480

sky_blue = pygame.Color(135, 206, 235)
black = pygame.Color(0, 0, 0)

# circle (bird)
position_x = window_x // 5
position_y = window_y // 2
radius = 20

jump_strength = 30

pygame.init()

game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                position_y -= jump_strength
    
    position_y += 5

    game_window.fill(sky_blue)

    pygame.draw.circle(game_window, black, (position_x, position_y), radius)


    # if position_y > window_y - radius or position_y < window_y - radius:
        #set game over here

    

    pygame.display.update()
    fps.tick(30)
