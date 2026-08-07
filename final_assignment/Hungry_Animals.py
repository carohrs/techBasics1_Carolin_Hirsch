#libraries
import pygame
import random
import os

#start pygame
pygame.init()

#Constants
SCREEN_WIDTH = 1200
Sceen_HEIGHT = 800
FPS = 60
BGCOLOR = (255,255,255)

#Window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Hungry Animals: Snack Drop")
clock = pygame.time.Clock()

#Classes
class Animal:
    def __init__(self, animal_name, favorite_food, start_x, start_y):
        # properties
        self.name = animal_name
        self.favorite_food = favorite_food
        self.x = start_x
        self.y = start_y
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, 60, 60)  # Pygame Rect as hitbox

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:  # so it doesn't go off the screen
            self.x = 0
        self.rect.x = self.x

    def move_right(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH - self.rect.width:  # so it doesn't go off the screen again
            self.x = SCREEN_WIDTH - self.rect.width
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 165, 0), self.rect)  # orange rectangle as placeholder


#Create the player animal (Monkey for demonstration)
player = Animal("Monkey", "Banana", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

#Game loop control
running = True

while running:

    #Event handling later
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Key input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    #Drawing
    screen.fill(BGCOLOR)
    player.draw(screen)
    pygame.display.flip()

    #Limit framerate
    clock.tick(FPS)

pygame.quit()