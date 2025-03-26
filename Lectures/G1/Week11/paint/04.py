import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

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

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_figure(figure_index):
    if figure_index == 0:   # Line
        pygame.draw.line(screen, colorRED, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
    elif figure_index == 1: # Rectangle
        pygame.draw.rect(screen, colorRED, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)

figures = ['Line', 'Rectangle']

figure_index = 0

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
            prev_x = event.pos[0]
            prev_y = event.pos[1]
        if event.type == pygame.MOUSEMOTION:
            # print("Position of the mouse:", event.pos)
            curr_x = event.pos[0]
            curr_y = event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # print("LMB released!")
            LMBpressed = False
            draw_figure(figure_index)
            base_layer.blit(screen, (0, 0))
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
            if event.key == pygame.K_UP:
                figure_index += 1
                if figure_index >= len(figures):
                    figure_index = 0
            if event.key == pygame.K_DOWN:
                figure_index -= 1
                if figure_index < 0:
                    figure_index = len(figures) - 1

    screen.blit(base_layer, (0, 0))

    if LMBpressed:
        draw_figure(figure_index)

    pygame.display.flip()
    clock.tick(60)