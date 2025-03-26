# The first half is just boiler-plate stuff...

import pygame
from color_palette import *

pygame.init()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

        


class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    font_large = pygame.font.SysFont("Comic Sans MS", 72, True)
    font_small = pygame.font.SysFont("Comic Sans MS", 36, True)
    text_game_name = font_large.render("SNAKE", True,colorBLACK)
    text_intro = font_small.render("Press ENTER", True,colorBLACK)

    def __init__(self):
        super().__init__()
        self.font_large = pygame.font.SysFont("Comic Sans MS", 72, True)
        self.font_small = pygame.font.SysFont("Comic Sans MS", 36, True)
        self.text_game_name = self.font_large.render("SNAKE", True,colorBLACK)
        self.text_intro = self.font_small.render("Press ENTER", True,colorBLACK)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(MenuScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill((255, 0, 0))

        screen_rect = screen.get_rect()
        text_game_name_rect = self.text_game_name.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2 - 50))
        text_intro_rect = self.text_intro.get_rect(center = (screen_rect.width // 2, screen_rect.height // 2))
        screen.blit(self.text_intro, text_intro_rect)
        screen.blit(self.text_game_name, text_game_name_rect)
        # For the sake of brevity, the title scene is a blank red screen
        

class MenuScene(SceneBase):

    def __init__(self):
        super().__init__()
        self.menu_items = ["Play", "Continue", "Options", "Quit"]
        self.active_index = 0
        self.font = pygame.font.SysFont("sfpro", 60)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.active_index == 0:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(GameScene())
                elif event.key == pygame.K_RETURN and self.active_index == 3:
                    self.Terminate()
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1

    def Update(self):
        pass
    
    def Render(self, screen):
        screen.fill(colorGREEN)
        for i, item in enumerate(self.menu_items):
            text = item
            if i == self.active_index:
                text = '+' + text

            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (60, i * 60 + 60))

class GameScene(SceneBase):

    CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


    

run_game(400, 300, 60, TitleScene())