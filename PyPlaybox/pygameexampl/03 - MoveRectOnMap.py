import pytmx
import pygame
import pygame.font
from pygame.locals import *

from shared import *

# Carica la mappa TMX
screen = pygame.display.set_mode([WORLDSIZETILEX4*TILESIZEPX, WORLDSIZETILEY4*TILESIZEPX])
tmx_map = pytmx.load_pygame(tmx_map)
image = pygame.Surface((0, 0))
w_pressed = s_pressed = a_pressed = d_pressed = False

class Player:
    def __init__(self) -> None:
        self.__x = 120
        self.__y = 120

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value

ply = Player()

# Funzione per disegnare la mappa
def draw_map():
    for layer in tmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, image in layer.tiles():
                screen.blit(image, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

def draw_player():
    if w_pressed:
        ply.y -= 1
    elif s_pressed:
        ply.y += 1
    elif a_pressed:
        ply.x -= 1
    elif d_pressed:
        ply.x += 1

    pygame.draw.rect(screen, pygame.Color("RED"), pygame.Rect(ply.x, ply.y, 30, 30))

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                w_pressed = True
            elif event.key == pygame.K_s:
                s_pressed = True
            elif event.key == pygame.K_a:
                a_pressed = True
            elif event.key == pygame.K_d:
                d_pressed = True
            elif event.key == pygame.K_q or pygame.K_ESCAPE:
                running = False
        if event.type == KEYUP:
            if event.key == pygame.K_w:
                w_pressed = False
            elif event.key == pygame.K_s:
                s_pressed = False
            elif event.key == pygame.K_a:
                a_pressed = False
            elif event.key == pygame.K_d:
                d_pressed = False

    # Disegna la mappa
    draw_map()
    draw_player()

    # Disegna la box grigio scuro trasparente
    pygame.draw.rect(screen, TRANSPARENT_GRAY, (20, 20, 200, 60))

    # Scrivi le coordinate nella box
    draw_text(screen, f'x: {ply.x:.2f}', 14, 30, 30, WHITE)
    draw_text(screen, f'y: {ply.y:.2f}', 14, 30, 50, WHITE)

    # Aggiorna la finestra di gioco
    pygame.display.flip()

# Esci dal gioco
pygame.quit()