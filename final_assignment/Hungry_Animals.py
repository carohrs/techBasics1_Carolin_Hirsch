#libraries
import pygame
import random
import os

#start pygame
pygame.init()

#Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

#Window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Hungry Animals: Snack Drop")
clock = pygame.time.Clock()

#fonts (for score..)
font = pygame.font.SysFont(None, 50)
font_big = pygame.font.SysFont(None, 90)
font_title = pygame.font.SysFont(None, 70)
font_small = pygame.font.SysFont(None, 35)

#colors
BLACK = (0,0,0)
RED = (128,0,32)
ORANGE = (255,165,0)
ROSA = (231, 84, 128)

IMAGE_FOLDER ="images"

#load image and scale to the size
def load_image(file_name, width, height):
    path =os.path.join(IMAGE_FOLDER, file_name)
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

#background
background_image = load_image("Background.png", SCREEN_WIDTH, SCREEN_HEIGHT)

#animal images
ANIMAL_IMAGES = {
    "Monkey": load_image("Monkey.png", 120, 120),
    "Dog": load_image("Dog.png", 120, 120),
    "Frog": load_image("Frog.png", 120, 120),
    "Cat": load_image("Cat.png", 120, 120),
    "Bunny": load_image("Bunny.png", 120, 120)
}

#food images
FOOD_IMAGES = {
    "Banana": load_image("Banana.png", 50, 50),
    "Fish": load_image("Fish.png", 50, 50),
    "Bone": load_image("Bone.png", 50, 50),
    "Carrot": load_image("carrot.png", 50, 50),
    "Fly": load_image("Fly.png", 50, 50)
}

#Classes
class Animal:
    def __init__(self, animal_name, favorite_food, start_x, start_y, animal_color):
        # properties
        self.name = animal_name
        self.favorite_food = favorite_food
        self.x = start_x
        self.y = start_y
        self.speed = 8
        self.color = animal_color
        self.image = ANIMAL_IMAGES[animal_name]
        self.rect = pygame.Rect(self.x, self.y, 120, 120)  # Pygame Rect as hitbox

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
        surface.blit(self.image, (self.x, self.y))

#food
class Food:
    def __init__(self, food_name, start_x, fall_speed):
        self.name = food_name
        self.x = start_x
        self.y = 0  #start at the top of the screen
        self.speed = fall_speed
        self.image = FOOD_IMAGES[food_name]
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def fall(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

#ANIMAL OPTIONS for the start screen (name, favorite food, color)
ANIMAL_OPTIONS = [
    {"name": "Monkey", "food": "Banana", "color": (210, 140, 50)},
    {"name": "Dog", "food": "Bone", "color": (160, 100, 50)},
    {"name": "Frog", "food": "Fly", "color": (50, 180, 50)},
    {"name": "Cat", "food": "Fish", "color": (180, 180, 180)},
    {"name": "Bunny", "food": "Carrot", "color": (255, 150, 0)}]

#player starts as None and gets set when character is chosen
player = None

#list of possible food types
FOOD_TYPES = ["Banana", "Fish", "Bone", "Carrot", "Fly"]

#list to store falling food
food_list = []

#timer for spawning the food
spawn_timer = 0
SPAWN_DELAY = 60 #maybe later random

#score and lives
score = 0
lives = 3
highscore = 0

#level (difficulty)
BASE_FALL_SPEED = 4
current_fall_speed = 4 #--> will increase over time

#game states
START_SCREEN = "start_screen"
PLAYING = "playing"
PAUSED = "paused"
GAME_OVER = "game_over"
game_state = START_SCREEN #so the game starts in the start screen

#reset function
def reset_game(chosen_animal):
    global player, score, lives, food_list, spawn_timer, current_fall_speed, game_state

    score = 0
    lives = 3
    food_list = []
    spawn_timer = 0
    current_fall_speed = BASE_FALL_SPEED

    #create the player with the chosen animal
    player = Animal(
        chosen_animal["name"],
        chosen_animal["food"],
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT - 140,
        chosen_animal["color"]
    )
    game_state = PLAYING

#read the highscor from the file
def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            return int(file.read())
    else:
        return 0

#save the score if it is a new highscore
def save_highscore(new_score):
    global highscore
    if new_score > highscore:
        highscore = new_score
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))


def handle_events():
    global game_state, food_list
     # keyboard action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:

            #Q always quits the game
            if event.key == pygame.K_q:
                return False

            #start screen choose animal
            if game_state == START_SCREEN:
                if event.key == pygame.K_1:
                    reset_game(ANIMAL_OPTIONS[0])  # Monkey
                if event.key == pygame.K_2:
                    reset_game(ANIMAL_OPTIONS[1])  # Dog
                if event.key == pygame.K_3:
                    reset_game(ANIMAL_OPTIONS[2])  # Frog
                if event.key == pygame.K_4:
                    reset_game(ANIMAL_OPTIONS[3])  # Cat
                if event.key == pygame.K_5:
                    reset_game(ANIMAL_OPTIONS[4])  # Bunny

            # if game is over, press R to restart or Q to quit
            if game_state == GAME_OVER:
                if event.key == pygame.K_r:
                    game_state = START_SCREEN
                    food_list = []

            if game_state == PLAYING:
                if event.key == pygame.K_p:
                    game_state = PAUSED
            elif game_state == PAUSED:
                if event.key == pygame.K_p:
                    game_state = PLAYING

    return True


# key input for movement
def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

#spawn new food
def spawn_food():
    global spawn_timer
    spawn_timer += 1
    if spawn_timer >= SPAWN_DELAY:
        spawn_timer = 0

        #40% chance for the favorite food, otherwise random
        if random.randint(1, 10) <= 4:
            random_food_name = player.favorite_food
        else:
            random_food_name = random.choice(FOOD_TYPES)

        random_x = random.randint(0, SCREEN_WIDTH - 50)
        new_food = Food(random_food_name, random_x, current_fall_speed)
        food_list.append(new_food)

#make it fall and remove when it falls out of the screen
def move_food():
    global food_list, score

    for food in food_list:
            food.fall()
    #remove food that has fallen off the screen (missed)
    food_still_falling = []
    for food in food_list:
        if food.rect.y < SCREEN_HEIGHT:
            food_still_falling.append(food)
        else:
            #missing favorite food = - score
            if food.name == player.favorite_food:
                score -= 1

    food_list = food_still_falling


# check collision between player and food
def check_collision():
    global score, lives

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

#update when playing
def update_game():
    global current_fall_speed, game_state, score, lives

    move_player()

    #increase fall speed (difficulty) based on score
    current_fall_speed = BASE_FALL_SPEED + (score // 5) #every 5 points, increase fall speed

    spawn_food()
    move_food()
    check_collision()

    #if score below zero you lose a life
    if score < 0:
        lives -= 1
        score = 0
    #check game over
    if lives <= 0:
        save_highscore(score)
        game_state = GAME_OVER


#START SCREEN
def draw_start_screen():
    #title
    title_text = font_title.render("Hungry Animals: Snack Drop", True, ROSA)
    subtitle_text = font_small.render("Press 1-5 to choose your animal", True, BLACK)
    quit_hint = font_small.render("Press Q to quit", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(subtitle_text, (SCREEN_WIDTH // 2 - subtitle_text.get_width() // 2, 200))
    screen.blit(quit_hint, (SCREEN_WIDTH // 2 - quit_hint.get_width() // 2, 240))

    #show all 4 animals
    for i, animal in enumerate(ANIMAL_OPTIONS):
        x_pos = 40 + i * 235
        y_pos= 240

        #draw animal
        screen.blit(ANIMAL_IMAGES[animal["name"]], (x_pos, y_pos))
        #draw animal name below
        name_text = font.render(animal["name"], True, BLACK)
        screen.blit(name_text, (x_pos, y_pos + 130))
        #draw favorite food
        food_text = font_small.render("Loves : " + animal["food"], True, BLACK)
        screen.blit(food_text, (x_pos, y_pos + 180))

        #draw key to press
        key_text = font.render("Press " + str(i + 1), True, RED)
        screen.blit(key_text, (x_pos, y_pos + 230))

#game state PLAYING
def draw_playing():
    #draw player & food
    player.draw(screen)
    for food in food_list:
        food.draw(screen)

    # draw score and lives text
    score_text = font.render("Score: " + str(score), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)
    animal_text = font.render("Animal: " + player.name, True, BLACK)
    food_hint = font_small.render("Catch: " + player.favorite_food, True, BLACK)
    pause_hint = font_small.render("Press P to pause", True, BLACK)
    quit_hint= font_small.render("Press Q to quit", True, BLACK)
    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 70))
    screen.blit(animal_text, (20, 120))
    screen.blit (food_hint, (20, 170))
    screen.blit (pause_hint, (20, 210))
    screen.blit (quit_hint, (20, 240))

def draw_paused():
    #game in the background
    draw_playing()

    paused_text = font_big.render("PAUSED", True, BLACK)
    continue_text = font.render("Press P to continue", True, BLACK)
    screen.blit(paused_text, (SCREEN_WIDTH // 2 - paused_text.get_width() // 2, 300))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, 400))


def draw_game_over():
    gameover_text = font_big.render("GAME OVER", True, (200, 0, 0))
    final_score_text = font.render("Final Score: " + str(score), True, BLACK)
    highscore_text = font.render("Highscore: " + str(highscore), True, BLACK)
    restart_text = font.render("Press R to restart or Q to quit", True, BLACK)
    quit_text = font.render ("Press Q to quit", True, BLACK)
    # center the text
    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width() // 2, 250))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, 380))
    screen.blit(highscore_text, (SCREEN_WIDTH // 2 - highscore_text.get_width() // 2, 320))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 450))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 510))

#Drawing
def draw_everything():
    screen.blit(background_image, (0, 0))

    if game_state == START_SCREEN:
        draw_start_screen()

    if game_state == PLAYING:
        draw_playing()

    if game_state == PAUSED:
        draw_paused()

    if game_state == GAME_OVER:
        draw_game_over()

    pygame.display.flip()

#MAIN

def main():
    global highscore

    #load the highscore from the file
    highscore = load_highscore()

    #game loop control
    running = True

    while running:
        running = handle_events()

        if game_state == PLAYING:
            update_game()

        draw_everything()

         #Limit framerate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()