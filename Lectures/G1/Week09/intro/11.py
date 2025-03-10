import pygame

pygame.init() # initializes all the pygame sub-modules

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((800, 480)) # creating a game window
# set_mode() takes a tuple as an argument

COLOR_RED = (255, 0, 0) # Color red in RGB
# 255 - value for red
# 0 - value for green
# 0 - value for blue
# each color component has a value between 0 and 255
# that is, 8 bits
COLOR_BLUE = (0, 0, 255)

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

movement_speed = 10

running = True
is_red = True

# this object allows us to set the FPS
clock = pygame.time.Clock()
FPS = 60 

while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red # flipping the value

    pressed_keys = pygame.key.get_pressed()       
    if pressed_keys[pygame.K_UP]:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        circle_y += movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= movement_speed
    
    # fill the screen with a color to wipe away anything from last frame
    if is_red:
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 40)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 40)
    
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS
    # delay is 1000.0 / FPS