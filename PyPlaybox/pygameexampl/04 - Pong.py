import random

import pygame
import sys
from typing import TypedDict

racket_w = 15
racket_h = 60
scr_w = 640
scr_h = 480
title = "Pong"


class Ball:
    def __init__(self, surface, center: tuple[float, float], radius, color, dir: pygame.Vector2):
        self.center = center
        self.radius = radius
        self.color = color
        self.vel = 1
        self.dir = dir
        self.surface = surface
        self.is_moving = False

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (int(self.center[0]), int(self.center[1])), self.radius)

    def move(self):

        if not self.is_moving:
            return

        # Aggiungi la velocità alla posizione corrente della palla
        self.center = (self.center[0] + self.dir.x * self.vel, self.center[1] + self.dir.y * self.vel)

        # Controlla se la palla tocca i bordi superiori dello schermo e in caso contrario cambia la direzione
        if self.center[1] - self.radius < 0 or self.center[1] + self.radius > scr_h:
            self.dir.y *= -1

    def get_rect(self):
        # Calcola il rettangolo circoscritto del cerchio
        return pygame.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius * 2, self.radius * 2)

    def check_collision_with_player(self, player):
        ball_rect = self.get_rect()
        return ball_rect.colliderect(player.rect)

    def check_collision_with_enemy(self, enemy):
        ball_rect = self.get_rect()
        return ball_rect.colliderect(enemy.rect)

    def reset_and_rest(self):
        self.center = (scr_w // 2, scr_h // 2)
        self.dir = pygame.Vector2(0, 0)
        self.is_moving = False


class Player:
    def __init__(self, surface, init_x_pos):
        self.movement = [False, False]
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(init_x_pos, (480 - 60) // 2, racket_w, racket_h)
        self.movement = [False, False]
        self.surface = surface

    def move(self):
        self.rect.y += (self.movement[1] - self.movement[0]) * 5

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def move_towards_ball(self, ball):
        # Muovi il giocatore nemico verso l'alto o il basso per seguire la palla
        if ball.center[1] < self.rect.centery:
            self.rect.y -= 5
        elif ball.center[1] > self.rect.centery:
            self.rect.y += 5

        # Limita il movimento del giocatore nemico entro i bordi dello schermo
        self.rect.y = max(0, min(self.rect.y, scr_h - racket_h))


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.ply = Player(self.screen, 15)
        self.enemy = Player(self.screen, scr_w - racket_w - 15)
        init_ball_direction = pygame.Vector2(5, -3)
        self.ball = Ball(self.screen, (320, 240), 10, (255, 0, 0), init_ball_direction)

        self.score = 0
        self.font = pygame.font.Font(None, 22)

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (scr_w - score_text.get_width() - 10, 10))

    def run(self):

        while True:
            self.screen.fill((0, 0, 0))

            self.ball.move()
            self.ply.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_w:
                        self.ply.movement[0] = True
                    if event.key == pygame.K_s:
                        self.ply.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        if not self.ball.is_moving:
                            self.ball.is_moving = not self.ball.is_moving
                            self.ball.dir = pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.ply.movement[0] = False
                    if event.key == pygame.K_s:
                        self.ply.movement[1] = False

            self.enemy.move_towards_ball(self.ball)

            if self.ball.check_collision_with_player(self.ply):
                self.ball.dir.x *= -1
                self.score += 10

            if self.ball.check_collision_with_enemy(self.enemy):
                self.ball.dir.x *= -1

            self.ball.draw()
            self.ply.draw()
            self.enemy.draw()

            self.draw_score()

            self.check_ball(self.ball)

            pygame.display.flip()
            self.clock.tick(60)

    def check_ball(self, ball):
        # controlla se la palla è uscita dallo schermo
        # se è uscita riposiziona la palla al centro e aspetta che
        # l'utente prema spazio per ricominciare a giocare
        if self.ball.center[0] - self.ball.radius < 0 or self.ball.center[0] + self.ball.radius > scr_w:
            self.ball.reset_and_rest()


Game().run()
