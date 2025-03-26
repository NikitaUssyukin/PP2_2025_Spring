import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

mouse_x, mouse_y = pygame.mouse.get_pos()

curr_x = mouse_x
curr_y = mouse_y

prev_x = mouse_x
prev_y = mouse_y

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # print("LMB pressed!")
            LMBpressed = True
            curr_x = event.pos[0]
            curr_y = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            # print("Position of the mouse:", event.pos)
            curr_x = event.pos[0]
            curr_y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # print("LMB released!")
            LMBpressed = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

    if LMBpressed:
        pygame.draw.line(screen, colorRED, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
    
    prev_x = curr_x
    prev_y = curr_y

    pygame.display.flip()
    clock.tick(60)