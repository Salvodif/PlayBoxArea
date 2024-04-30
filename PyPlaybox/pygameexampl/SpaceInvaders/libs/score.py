from abc import ABC

import pygame

from libs.config import Config
from libs.base_shape.shape import SDFShape
from libs.shared import Shared


class Score(SDFShape, ABC):
    def __init__(self):
        self.__config = Config()
        self.__shared: Shared = Shared()

        super().__init__(size=(30, 30))

        self.__score: int = 0
        self.font = pygame.font.Font(None, 22)
        self.__txt = self.font.render(f"Score: {self.__score}", True, (255, 255, 255))

    def draw(self):
        self.__shared.screen.blit(self.__txt, (self.__config.win_h - self.__txt.get_width() - 10, 10))

    @property
    def score(self, val: int) -> None:
        self.__score = val
