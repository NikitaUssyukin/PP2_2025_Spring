# The first half is just boiler-plate stuff...

import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

FPS = 5



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

    def move(self, max_x, max_y):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # checks the right border
        if self.body[0].x > max_x:
            self.body[0].x = 0
        # checks the left border
        if self.body[0].x < 0:
            self.body[0].x = max_x
        # checks the bottom border
        if self.body[0].y > max_y:
            self.body[0].y = 0
        # checks the top border
        if self.body[0].y < 0:
            self.body[0].y = max_y


    def draw(self, screen, CELL):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food, CELL):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(CELL)



class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self, screen, CELL):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, CELL):
        self.pos.x = random.randint(0, WIDTH // CELL - 1)
        self.pos.y = random.randint(0, HEIGHT // CELL - 1)



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

    def __init__(self):
        super().__init__()
        self.CELL = 30
        self.food = Food()
        self.snake = Snake()

    def draw_grid(self, screen, WIDTH, HEIGHT):
        for i in range(HEIGHT // self.CELL):
            for j in range(WIDTH // self.CELL):
                pygame.draw.rect(screen, colorGRAY, (i * self.CELL, j * self.CELL, self.CELL, self.CELL), 1)

    def draw_grid_chess(self, screen, WIDTH, HEIGHT):
        colors = [colorWHITE, colorGRAY]

        for i in range(HEIGHT // self.CELL):
            for j in range(WIDTH // self.CELL):
                pygame.draw.rect(screen, colors[(i + j) % 2], (i * self.CELL, j * self.CELL, self.CELL, self.CELL))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.dx = 1
                    self.snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.dx = -1
                    self.snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.dx = 0
                    self.snake.dy = 1
                elif event.key == pygame.K_UP:
                    self.snake.dx = 0
                    self.snake.dy = -1
        
    def Update(self):
        max_x = WIDTH // self.CELL - 1
        max_y = HEIGHT // self.CELL - 1
        self.snake.move(max_x, max_y)
        self.snake.check_collision(self.food, self.CELL)
    
    def Render(self, screen):
        screen.fill(colorBLACK)
        self.draw_grid(screen, WIDTH, HEIGHT)

        self.snake.draw(screen, self.CELL)
        self.food.draw(screen, self.CELL)

run_game(WIDTH, HEIGHT, FPS, TitleScene())