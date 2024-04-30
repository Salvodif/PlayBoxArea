import string


class Config:
    def __init__(self):
        self.__win_w: int = 640
        self.__win_h: int = 480
        self.__win_title: string = "Space Invaders"
        self.__fps: int = 30
        self.__enemy_cols = 4
        self.__enemy_rows = 3

    @property
    def win_w(self) -> int:
        return self.__win_w

    @property
    def win_h(self) -> int:
        return self.__win_h

    @property
    def title(self) -> string:
        return self.__win_title

    @property
    def FPS(self) -> int:
        return self.__fps

    @property
    def enemy_cols(self) -> int:
        return self.__enemy_cols
    @property
    def enemy_rows(self) -> int:
        return self.__enemy_rows
