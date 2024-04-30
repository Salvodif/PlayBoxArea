import pygame

from libs.colors import SDFColors
from libs.base_shape.square import SDFSquare


class Enemy(SDFSquare):
    def __init__(self):
        self.__vel: float = 2
        self.__dir: pygame.Vector2 = pygame.Vector2(1, 0)
        self.__alive: bool = True
        self.__color: SDFColors = SDFColors.red

        super().__init__(position=(0, 0), size=(25, 25))

    @property
    def vel(self) -> float:
        return self.__vel

    @property
    def dir(self) -> pygame.Vector2:
        return self.__dir

    @property
    def alive(self):
        return self.__alive
