import pygame


class Shared:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.screen = None
            cls._instance.clock = pygame.time.Clock()

        return cls._instance