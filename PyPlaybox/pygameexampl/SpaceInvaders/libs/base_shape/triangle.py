import pygame
from pygame import Vector2

from libs.colors import SDFColors
from libs.shared import Shared
from libs.base_shape.shape import SDFShape


class SDFTriangle(SDFShape):
    def __init__(self, base_size: (int, int), color: SDFColors):
        super().__init__(size=base_size)
        self.__shared: Shared = Shared()
        self.__color = color
        self._point_list: list[Vector2] = [Vector2() for _ in range(3)]

        self.__x_top = int

    def draw(self):
        pygame.draw.polygon(self.__shared.screen, self.__color, self._point_list)

    @property
    def color(self) -> SDFColors:
        return self.__color

    @color.setter
    def color(self, val: SDFColors):
        self.__color = val

    def get_position(self) -> list[Vector2]:
        position = self.position
        x_bottom_left = position[0] - (self.size[0] / 2)
        x_bottom_right = position[1] + (self.size[0] / 2)

        self.__x_top = (x_bottom_left + x_bottom_right) / 2
        y_bottom = self.__x_top - self.size[1]

        return [Vector2(self.__x_top, self.size[1]), Vector2(x_bottom_left, y_bottom), Vector2(x_bottom_right, y_bottom)]

    def calc_x_top(self) -> None:
        x_bottom_left = self._point_list[0]
        x_bottom_right = self._point_list[1]

        self.__x_top = (x_bottom_left + x_bottom_right) / 2


    def update_position(self, val: [Vector2, Vector2]):
        if not val[0] is None:
            x_bottom_left = val[0]
            self.position[0] = x_bottom_left
        elif not val[1] is None:
            x_bottom_right = val[0]
            self.position[1] = x_bottom_right

        self.__point_list = Vector2(x_top, self.size[1]), Vector2(x_bottom_left, y_bottom), Vector2(x_bottom_right, y_bottom)

    @property
    def top_vertex(self) -> Vector2:
        return self.__point_list[0]
