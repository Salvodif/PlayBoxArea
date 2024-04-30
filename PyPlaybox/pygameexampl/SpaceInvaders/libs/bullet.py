import pygame

from libs.base_shape.circle import SDFCircle
from libs.colors import SDFColors


class Bullet(SDFCircle):
    def __init__(self, center: (float, float)):
        super().__init__((0, 0), (0, 0),  SDFColors.red.value)
        self.__center = center
        self.__alive = False
        self.__radius = 5
        self.__vel = -0.5

    def set_position(self, position: [int, int]) -> None:
        super().x = position[0]
        super().y = position[1]

    def draw(self):
        if self.alive:
            pygame.draw.circle(self.surface, self.color, (self.__position[0], self.__position[0]), self.__radius)

    def update(self):
        if not self.alive:
            return

        self.center = (self.__center[0] + self.__x, self.__center[1])

        if self.__center[1] - self.__radius < 0 or self.__center[1] + self.__radius > shared.SCR_H:
            print("muove il proiettile")
            self.__y *= -self.__vel
        else:
            print("distriggu il proiettile")
            self.alive = False

    def get_rect(self):
        return pygame.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius * 2, self.radius * 2)

    def check_collision_with_enemy(self, enemy):
        ball_rect = self.get_rect()
        return ball_rect.colliderect(enemy.rect)

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value):
        self.__alive = value

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y