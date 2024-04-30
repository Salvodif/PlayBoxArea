from abc import abstractmethod

import pygame

from libs.colors import SDFColors


class SDFShape:
    def __init__(self, size: (int, int)):
        self.__size = size
        self.__movement = (False, False)

    @abstractmethod
    def draw(self):
        pass

    @property
    def w(self) -> int:
        return self.__size[0]

    @property
    def h(self) -> int:
        return self.__size[1]
