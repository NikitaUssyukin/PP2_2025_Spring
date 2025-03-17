import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

clock = pygame.time.Clock()

_sound_library = dict()
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:
        play_sound("bonk.mp3")
        
    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)