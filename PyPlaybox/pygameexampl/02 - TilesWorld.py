import pytmx
import pygame
from pygame.locals import *

from shared import *

# Carica la mappa TMX
screen = pygame.display.set_mode([WORLDSIZETILEX4*TILESIZEPX, WORLDSIZETILEY4*TILESIZEPX])
tmx_map = pytmx.load_pygame(tmx_map)
image = pygame.Surface((0, 0))

# Funzione per disegnare la mappa
def draw_map():
    for layer in tmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_q or pygame.K_ESCAPE:
                running = False

    # Disegna la mappa
    draw_map()

    # Aggiorna la finestra di gioco
    pygame.display.flip()

# Esci dal gioco
pygame.quit()
