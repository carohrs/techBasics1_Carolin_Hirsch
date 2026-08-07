#libraries
import pygame
import random
import os

from pygame import color

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

#fonts (for score..)
font = pygame.font.SysFont(None, 50)
font_big = pygame.font.SysFont(None, 100)
font_small = pygame.font.SysFont(None, 35)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,165,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#Classes
class Animal:
    def __init__(self, animal_name, favorite_food, start_x, start_y):
        # properties
        self.name = animal_name
        self.favorite_food = favorite_food
        self.x = start_x
        self.y = start_y
        self.speed = 5
        self.color = color
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
        pygame.draw.rect(surface, self.color, self.rect)
        # draw animal name below
        name_text = font_small.render(self.name, True, BLACK)
        surface.blit(name_text, (self.rect.x, self.rect.y + 65))

#food
class Food:
    def __init__(self, food_name, start_x, fall_speed):
        self.name = food_name
        self.x = start_x
        self.y = 0  #start at the top of the screen
        self.speed = fall_speed
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

# each food type gets its own color so you can tell them apart
        if self.name == "Banana":
            self.color = (255, 255, 0)  # yellow
        elif self.name == "Fish":
            self.color = (0, 150, 255)  # blue
        elif self.name == "Bone":
            self.color = (180, 50, 50)  # dark red
        elif self.name == "Fly":
            self.color = (50, 50, 50)  # dark grey
        elif self.name == "Carrot":
            self.color = (255, 150, 0)
        else:
            self.color = GREEN

    def fall(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        # draw food name below
        food_text = font_small.render(self.name, True, BLACK)
        surface.blit(food_text, (self.rect.x, self.rect.y + 42))

#ANIMAL OPTIONS for the start screen (name, favorite food, color)
animal_options = [
    {"name": "Monkey", "food": "Banana", "color": (210, 140, 50)},
    {"name": "Dog", "food": "Bone", "color": (160, 100, 50)},
    {"name": "Frog", "food": "Fly", "color": (50, 180, 50)},
    {"name": "Cat", "food": "Fish", "color": (180, 180, 180)}
    {"name": "Bunny", "food": "Carrot", "color": (255, 150, 0)}]

#player starts as None and gets set when character is chosen
player = None

#list of possible food types
FOOD_TYPES = ["Banana", "Fish", "Bone", "Carrot", "Fly"]

#list to store falling food
food_list = []

#timer for spawning the food
spawn_timer = 0
spawn_delay = 60 #maybe later random

#score and lives
score = 0
lives = 3

#level (difficulty)
base_fall_speed = 4
current_fall_speed = 4 #--> will increase over time

#game states
START_SCREEN = "start_screen"
PLAYING = "playing"
GAME_OVER = "game_over"
game_state = START_SCREEN #so the game starts in the start screen

#reset function
def reset_game(chosen_animal):
    global player, score, lives, food_list, spawn_timer, current_fall_speed, game_state

    score = 0
    lives = 3
    food_list = []
    spawn_timer = 0
    current_fall_speed = base_fall_speed

    #create the player with the chosen animal
    player = Animal(
        chosen_animal["name"],
        chosen_animal["food"],
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT - 100,
        chosen_animal["color"]
    )
    game_state = PLAYING


#Game loop control
running = True

while running:

    # keyboard action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            #start screen choose animal
            if game_state == START_SCREEN:
                if event.key == pygame.K_1:
                    reset_game(animal_options[0])  # Monkey
                if event.key == pygame.K_2:
                    reset_game(animal_options[1])  # Dog
                if event.key == pygame.K_3:
                    reset_game(animal_options[2])  # Frog
                if event.key == pygame.K_4:
                    reset_game(animal_options[3])  # Cat

        # if game is over, press R to restart or Q to quit
        if game_state == GAME_OVER:
            if event.key == pygame.K_r:
               game_state = START_SCREEN
               food_list = []
                if event.key == pygame.K_q:
                    running = False

    # update when playing
    if game_state == PLAYING:

    # key input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    # increase fall speed (difficulty) based on score
    current_fall_speed = base_fall_speed + (score // 5) # every 5 points, the food falls one pixel per frame faste

    #spawn new food
    spawn_timer += 1
    if spawn_timer >= spawn_delay:
        spawn_timer = 0
        random_food_name = random.choice(FOOD_TYPES)
        random_x = random.randint(0, SCREEN_WIDTH - 40)
        new_food = Food(random_food_name, random_x)
        food_list.append(new_food)

    #make it fall
    for food in food_list:
            food.fall()

    # check collision between player and food
    food_to_remove = []  # list to store food to remove

    for food in food_list:
        if player.rect.colliderect(food.rect):
            if food.name == player.favorite_food:
                score += 1
            else:
                score -= 1
                lives -= 1
            food_to_remove.append(food)  # add food to remove list
    #remove food that was caught
    for food in food_to_remove:
        food_list.remove(food)

    #remove food that has fallen off the screen (missed)
    food_list = [food for food in food_list if food.y < SCREEN_HEIGHT]

    #check game over
    if lives <= 0:
        game_state = GAME_OVER

    #Drawing
    screen.fill(BGCOLOR)

    #START SCREEN
    if game_state == START_SCREEN:
        #title
        title_text = font_big.render("Hungry Animals: Snack Drop", True, ORANGE)
        subtitle_text = font_small.render("Press 1-4 to choose your animal", True, BLACK)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 200))

        #show all 4 animals
        for i, animal in enumerate(animal_options):
            x_pos = 150 + i * 150
            y_pos= 250

            #draw animal
            pygame.draw.rect(screen, animal["color"], (x_pos, y_pos, 80, 80))
            #draw animal name below
            name_text = font.render(animal["name"], True, BLACK)
            screen.blit(name_text, (x_pos, y_pos + 90))
            #draw favorite food
            food_text = font_small.render("Loved food : " + animal["food"], True, BLACK)
            screen.blit(food_text, (x_pos, y_pos + 140))

            #draw key to press
            key_text = font.render("Press " + str(i + 1), True, RED)
            screen.blit(key_text, (x_pos, y_pos + 180))

#game state PLAYING
    if game_state == PLAYING:
#draw player & food
    player.draw(screen)
    for food in food_list:
        food.draw(screen)

    # draw score and lives text
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    lives_text = font.render("Lives: " + str(lives), True, (0, 0, 0))
    animal_text = font.render("Animal: " + player.name, True, BLACK)
    food_hint = font_small.render("Catch: " + player.favorite_food, True, BLACK)
    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 70))
    screen.blit(animal_text, (20, 120))
    screen.blit (food_hint, (20, 170))

    if game_state == GAME_OVER:
#draw game over screen
        game_over_text = font_big.render("GAME OVER", True, (200, 0, 0))
        score_text = font.render("Final Score: " + str(score), True, (0, 0, 0))
        restart_text = font.render("Press R to restart or Q to quit", True, (0, 0, 0))
        quit_text = font.render ("Press Q to Quit, True, BLACK")
# center the text
    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, 250))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 380))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 450))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 510))))

    pygame.display.flip()

    #Limit framerate
    clock.tick(FPS)

pygame.quit()