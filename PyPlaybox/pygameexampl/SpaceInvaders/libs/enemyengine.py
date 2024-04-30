from typing import Type
import pygame

from libs.config import Config
from libs.enemy import Enemy


class EnemyEngine:
    def __init__(self):
        self.__enemy_list: list[Enemy] = []
        self.__config = Config()
        self.__span: int = 15

    def enemy_list_init(self):
        starting_x = (self.__config.win_w / 5) - Enemy().rect.width

        for row in range(self.__config.enemy_rows):
            enemy_row: list[Enemy] = []

            for col in range(self.__config.enemy_cols):
                enemy = Enemy()
                x = (starting_x * col) + self.__span
                y = 15 + (row * (enemy.rect.height + self.__span))

                enemy.update_position((x, y))

                enemy_row.append(enemy)

            self.__enemy_list.append(enemy_row)

    def update(self):
        for row in self.__enemy_list:
            for enemy in row:
                if enemy.alive:
                    direction = pygame.Vector2(enemy.dir)
                    new_x = enemy.vel * direction.x
                    new_y = enemy.vel * direction.y

                    enemy.x = new_x + enemy.x
                    enemy.y = new_y + enemy.y

                    if enemy.x >= self.__config.win_h - enemy.w:
                        for row in self.__enemy_list:
                            for enemy in row:
                                enemy.dir.x *= -1

                    if enemy.x <= 0:
                        for row in self.__enemy_list:
                            for enemy in row:
                                enemy.dir.x *= -1

    def draw(self):
        row: Enemy
        for row in self.__enemy_list:
            for enemy in row:
                if enemy.alive:
                    enemy.draw()

    @property
    def enemy_list(self) -> list[Enemy]:
        return self.__enemy_list
