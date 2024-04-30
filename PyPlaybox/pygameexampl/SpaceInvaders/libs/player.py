import pygame
from pygame import Vector2

from libs.config import Config
from libs.colors import SDFColors
from libs.base_shape.triangle import SDFTriangle


class Player(SDFTriangle):
    def __init__(self):
        config: Config = Config()

        self.__size = (25, 25)
        center = ((config.win_w / 2) - self.__size[0], config.win_h - self.__size[1] - 10)

        super().__init__(base_size=self.__size, color=SDFColors.white.value)

        self.dir: pygame.Vector2 = pygame.Vector2()
        self.movement = (False, False)

    def update(self):
        self.x[1][1] += (self.movement[1] - self.movement[0]) * 5

    def top_vertex(self) -> Vector2:
        return super().x[0]
