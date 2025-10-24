import random
import pygame

window_x = 720
window_y = 480

sky_blue = pygame.Color(135, 206, 235)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 128, 0)

# circle (bird)
position_x = window_x // 5
position_y = window_y // 2
radius = 20

#pipe
pipe_width = 70
pipe_gap = 150
pipe_x1 = window_x - 400
pipe_x2 = window_x - 200
pipe_x3 = window_x - 0
pipe_height_1 = random.randint(30, 430)
pipe_height_2 = random.randint(30, 430)
pipe_height_3 = random.randint(30, 430)

pipe_speed = 5

bottom_pipe_height1 = window_y - pipe_height_1 - pipe_gap
bottom_pipe_height2 = window_y - pipe_height_2 - pipe_gap
bottom_pipe_height3 = window_y - pipe_height_3 - pipe_gap


jump_strength = 130

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

    pygame.draw.rect(game_window, green,(pipe_x1, 0, pipe_width, pipe_height_1))
    pygame.draw.rect(game_window, green,(pipe_x1, window_y - bottom_pipe_height1, pipe_width, bottom_pipe_height1))

    pygame.draw.rect(game_window, green,(pipe_x2, 0, pipe_width, pipe_height_2))
    pygame.draw.rect(game_window, green,(pipe_x2, window_y - bottom_pipe_height2, pipe_width, bottom_pipe_height2))

    pygame.draw.rect(game_window, green,(pipe_x3, 0, pipe_width, pipe_height_3))
    pygame.draw.rect(game_window, green,(pipe_x3, window_y - bottom_pipe_height3, pipe_width, bottom_pipe_height3))

    pipe_x1 -= pipe_speed
    pipe_x2 -= pipe_speed
    pipe_x3 -= pipe_speed

    if pipe_x1 + pipe_width < 0:
        pipe_x1 = window_x
        pipe_height_1 = random.randint(30, 430)
        bottom_pipe_height1 = window_y - pipe_height_1 - pipe_gap

    if pipe_x2 + pipe_width < 0:
        pipe_x2 = window_x
        pipe_height_2 = random.randint(30, 430)
        bottom_pipe_height2 = window_y - pipe_height_2 - pipe_gap

    if pipe_x3 + pipe_width < 0:
        pipe_x3 = window_x
        pipe_height_3 = random.randint(30, 430)
        bottom_pipe_height3 = window_y - pipe_height_3 - pipe_gap



    if position_y > window_y - radius or position_y < window_y - radius:
        running = False

    

    pygame.display.update()
    fps.tick(30)
