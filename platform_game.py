import pygame
import sys
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.moveY = 0
        self.x = x
        self.y = y
        self.index = 0
        self.direction = "right"
        self.jump_count = 0
        self.right_jump_image = pygame.image.load("graphics/jump.png").convert_alpha()
        self.right_files = ["graphics/player_walk_1.png", "graphics/player_walk_2.png"]
        self.right_images = [pygame.image.load(filename).convert_alpha() for filename in self.right_files]
        self.pics = [[pygame.image.load("graphics/player_stand.png")],[pygame.transform.flip(img, True, False) for img in self.right_images],[pygame.transform.flip(self.right_jump_image,True,False)], [pygame.image.load(filename).convert_alpha() for filename in self.right_files],[self.right_jump_image]]
        self.image = self.pics[0][0]
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def jump(self):
        if self.count < 10:
            y -= 3
            self.count += 1

pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255) 
PURPLE = '#800080'

clock = pygame.time.Clock()



count = 0
# Main game loop
running = True
while running:
    count += 1
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)
   
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()
