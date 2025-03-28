import pygame

pygame.init()

screen = pygame.display.set_mode((800, 480))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)

running = True
is_red = True

flip_freq = 1                                            # frequency of color flips in Hz (flips per second)

INC_FLIP_FREQ = pygame.USEREVENT + 1                     # custom event for increasing the flip frequency
FLIP_COLOR = pygame.USEREVENT + 2                        # custom event for flipping the color

pygame.time.set_timer(INC_FLIP_FREQ, 3000)               # create a timer that pushes the event INC_FLIP_FREQ into the event queue every 3000 ms
pygame.time.set_timer(FLIP_COLOR, int(1000 / flip_freq)) # create a timer that pushes the event FLIP_COLOR into the event queue every int(1000 / flip_freq) ms

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == FLIP_COLOR:
            is_red = not is_red                          # color flip
        if event.type == INC_FLIP_FREQ:
            flip_freq += 1                               # increase flip frequency
            pygame.time.set_timer(FLIP_COLOR, int(1000 / flip_freq)) # update the timer with the new frequency
    
    if is_red:
        screen.fill(colorRED)
    else:
        screen.fill(colorBLUE)
    
    pygame.display.flip()