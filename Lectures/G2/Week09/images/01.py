import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

running = True
is_red = True

x = 30
y = 30

image = pygame.image.load("ball.png")

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += 1
    if keys[pygame.K_LEFT]: 
        x -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_UP]:
        y -= 1
        
    screen.fill(white)

    screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)