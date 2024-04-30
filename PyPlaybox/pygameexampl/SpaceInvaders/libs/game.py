import pygame
import sys

from libs.config import Config
from libs.colors import SDFColors
from libs.enemy import Enemy
from libs.enemyengine import EnemyEngine
from libs.player import Player
from libs.bullet import Bullet
from libs.score import Score
from libs.shared import Shared


class Game:
    def __init__(self):
        self.__config: Config = Config()
        self.__shared: Shared = Shared()

        pygame.init()
        pygame.display.set_caption(self.__config.title)

        self.__shared.screen = pygame.display.set_mode((self.__config.win_h, self.__config.win_h))
        self.__clock = pygame.time.Clock()
        self.__running: bool = True

        self.__eng_enemy: EnemyEngine = EnemyEngine()
        self.__eng_enemy.enemy_list_init()

        self.__ply = Player()
        # bullet_center = (self.__ply.pos_top_vertex()[0] + (self.__ply.w / 2), self.__ply.y - (self.__ply.h / 2))
        # self.bullet = Bullet(center=bullet_center)
        self.__score = Score()
        self.__text_surface: pygame.Surface = None

        self.hovered_enemy = None
        self.__info_font: pygame.font.Font = pygame.font.Font(None, 12)
        self.__mouse_x, self.__mouse_y = 0, 0
        self.__info_text = ""

    def clear_scr(self):
        self.__shared.screen.fill(SDFColors.black.value)

    def check_keyboard(self):
        is_mouse_over_enemy = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.__mouse_x, self.__mouse_y = pygame.mouse.get_pos()
                    for row_idx, row in enumerate(self.__eng_enemy.enemy_list):
                        for col_idx, enemy in enumerate(row):
                            enemy_rect = enemy.rect
                            if enemy_rect.collidepoint(self.__mouse_x, self.__mouse_y):
                                self.hovered_enemy = (row_idx, col_idx, enemy.x, enemy.y)
                                is_mouse_over_enemy = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self.__running = False

        if is_mouse_over_enemy:
            self.__info_text = f"Posizione: {self.hovered_enemy}"
        else:
            self.hovered_enemy = None

            #     if event.key == pygame.K_a:
            #         self.ply.movement[0] = True
            #         return
            #     if event.key == pygame.K_d:
            #         self.ply.movement[1] = True
            #         return
            #     if event.key == pygame.K_SPACE:
            #         if not self.bullet.alive:
            #             self.create_bullet()
            #         return
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_a:
            #         self.ply.movement[0] = False
            #         return
            #     if event.key == pygame.K_d:
            #         self.ply.movement[1] = False
            #         return

    def create_bullet(self) -> None:
        # fai partire il proiettile dal centro del giocatore
        # position = (self.ply.x + (self.ply.w / 2), self.ply.y - (self.ply.h / 2))
        # self.bullet.set_position((position[0], position[1]))
        # self.bullet.alive = True
        pass

    def update(self):
        self.__eng_enemy.update()
        # self.__ply.update()
        # self.__bullet.update()

        self.__eng_enemy.draw()
        self.__ply.draw()
        # self.bullet.draw()

        self.__score.draw()
        self.__text_surface = self.__info_font.render(self.__info_text, True, (255, 255, 255))
        self.__shared.screen.blit(self.__text_surface, (self.__mouse_x - 25, self.__mouse_y + 25))
        self.__clock.tick(self.__config.FPS)

        pygame.display.flip()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    @property
    def running(self):
        return self.__running
