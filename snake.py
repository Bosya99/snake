import pygame
import random

w, h = 1000,1000
size = 50
screen = pygame.display.set_mode((1080,900))
screen.fill((255, 255, 255))
fps = pygame.time.Clock()

class Game_Object:
    def __init__(self, x, y, color):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.img = pygame.Surface((size, size))
        self.img.fill(color)
x = size * random.randrange(w//size)
y = size * random.randrange(h//size)
box = Game_Object(x, y, (0, 255, 255))

class Snake(Game_Object):
    speedx = size
    speedy = 0
    timer = 0
    def move(self):
        if self.timer == 0:
            self.hitbox.x += self.speedx
            self.hitbox.y += self.speedy
            self.timer = 5
        self.timer -= 1
    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speedx = 0
            self.speedy = -size
        if keys[pygame.K_s]:
            self.speedx = 0
            self.speedy = size
        if keys[pygame.K_a]:
            self.speedx = -size
            self.speedy = 0
        if keys[pygame.K_d]:
            self.speedx = size
            self.speedy = 0
            
snake = Snake(0, 0, (120, 0, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(box.img, box.hitbox)
    screen.blit(snake.img, snake.hitbox)
    snake.move()
    snake.control()
    pygame.display.update()
    fps.tick(60)

