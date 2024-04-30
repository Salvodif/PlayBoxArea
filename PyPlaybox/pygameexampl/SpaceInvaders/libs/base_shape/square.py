from abc import ABC

import pygame

from libs.colors import SDFColors
from libs.base_shape.shape import SDFShape
from libs.shared import Shared


class SDFSquare(SDFShape, ABC):
    def __init__(self, position: (int, int), size: (int, int), color=SDFColors.red):
        super().__init__(size)
        self.__rect: pygame.Rect = pygame.Rect(position, size)
        self.__shared: Shared = Shared()
        self.__color: SDFColors = color

    def update_position(self, new_position: (int, int)):
        self.__rect.x = new_position[0]
        self.__rect.y = new_position[1]

    def draw(self) -> None:
        pygame.draw.rect(self.__shared.screen, self.__color.value, self.__rect)

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @property
    def x(self) -> int:
        return self.__rect.x

    @x.setter
    def x(self, val):
        self.__rect.x = val

    @property
    def y(self) -> int:
        return self.__rect.y

    @y.setter
    def y(self, val):
        self.__rect.y = val
