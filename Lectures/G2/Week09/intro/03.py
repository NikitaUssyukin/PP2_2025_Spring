import pygame

pygame.init() # initializes all the pygame sub-modules

screen = pygame.display.set_mode((800, 480)) # creating a game window
# set_mode() takes a tuple as an argument

COLOR_RED = (255, 0, 0) # Color red in RGB
# 255 - value for red
# 0 - value for green
# 0 - value for blue
# each color component has a value between 0 and 255
# that is, 8 bits
COLOR_BLUE = (0, 0, 255)

running = True
is_red = True
while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red # flipping the value
                # True -> False and vice versa
    
    # fill the screen with a color to wipe away anything from last frame
    if is_red:
        screen.fill(COLOR_RED)
    else:
        screen.fill(COLOR_BLUE)
    
    pygame.display.flip() # updates the screen