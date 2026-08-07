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

class Food:
    def __init__(self, food_name, start_x):
        self.name = food_name
        self.x = start_x
        self.y = 0  #start at the top of the screen
        self.speed = 4
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def fall(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 200, 0), self.rect)  #green square as placeholder


#Create animal (Monkey for demonstration)
player = Animal("Monkey", "Banana", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

#list of possible food typed
FOOD_TYPES = ["Banana", "Fish", "Bone", "Carrot", "Fly"]

#list to store falling food
food_list = []

#timer for spawning the food
spawn_timer = 0
spawn_delay = 60 #maybe later random

#Game loop control
running = True

while running:

    #keyboard action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Key input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    #spawn new food
    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        spawn_timer = 0
        random_food_name = random.choice(FOOD_TYPES)
        random_x = random.randint(0, SCREEN_WIDTH - 40)
        new_food = Food(random_food_name, random_x)
        food_list.append(new_food)

    # update all food items (make them fall)
    for food in food_list:
            food.fall()

    # remove food that has fallen off the screen (missed)
    food_list = [food for food in food_list if food.y < SCREEN_HEIGHT]

    #Drawing
    screen.fill(BGCOLOR)
    player.draw(screen)
    for food in food_list:
        food.draw(screen)
    pygame.display.flip()

    #Limit framerate
    clock.tick(FPS)

pygame.quit()