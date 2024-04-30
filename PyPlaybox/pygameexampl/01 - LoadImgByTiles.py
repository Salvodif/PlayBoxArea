import pygame
from pygame.locals import *

from shared import *

image = pygame.image.load(bg_file)

img_width, img_height = image.get_size()
num_tiles_x = img_width // TILESIZEPX
num_tiles_y = img_height // TILESIZEPX
numoftiles = num_tiles_x * num_tiles_y

world = [[0 for _ in range(WORLDSIZETILEX)] for _ in range(WORLDSIZETILEY)]

worldrows = len(world)
worldcolms = len(world[0])

pygame.init()

screen = pygame.display.set_mode([WORLDSIZETILEX*TILESIZEPX, WORLDSIZETILEY*TILESIZEPX])

# Define the dimension of the surface
# Here we are making squares of side 32px
tile = pygame.Surface((TILESIZEPX,TILESIZEPX))

while True:
    for y in range(worldcolms):
        for x in range(worldrows):
            tile.blit(image, (0, 0), (y*TILESIZEPX, x*TILESIZEPX, *(TILESIZEPX, TILESIZEPX)))
            screen.blit(tile, (y*TILESIZEPX, x*TILESIZEPX))
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_q or pygame.K_ESCAPE:
                pygame.quit()

    # paint screen one time
    pygame.display.flip()
