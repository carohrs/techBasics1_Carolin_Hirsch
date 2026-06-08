#I used the code from the exercise and uploaded a new image (cat.png)


# importing required library
import pygame
import random  #for random number generation

class Cat:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.speed = random.randint(1,5)

    def move(self, screen_width):
        x, y = self.position


        if x < screen_width:
            x += self.speed
        else:
            x = 0

        self.position =(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.position)
# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255)

# activate the pygame library
pygame.init()

# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
# use convert_alpha() for png images
img = pygame.image.load("cat.png").convert_alpha()

# scale down the dino
img = pygame.transform.scale(img, (100,100))

# option: tint your image if you want
# img.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)

cats = []
for i in range(5):

    random_y = random.randint(0,200)
    new_cat = Cat(img,(i * 100, random_y))
    cats.append(new_cat)

# Init the clock
clock = pygame.time.Clock()

flag = True

while flag:
    # ticking the clock
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # paint the screen with background color
    screen.fill(BACKGROUND_COLOR)

    for cat in cats:
        cat.move(SCREEN_WIDTH)
        cat.draw(screen)

    # refresh the display
    pygame.display.flip()

pygame.quit()
exit(0)