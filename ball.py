import pygame
from pygame.sprite import Sprite

from random import choice, randint


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ball(Sprite):

    def __init__(self, ai_settings, screen, paddles, cp):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.paddles = paddles

        self.cp = cp

        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()

        self.reset()

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        elif self.rect.top <= 0:
            return True
        elif self.rect.bottom >= screen_rect.bottom:
            return True

    def paddle_hitH(self):
        paddleT = self.paddles.paddleT
        paddleB = self.paddles.paddleB

        c_paddleT = self.cp.c_paddleT
        c_paddleB = self.cp.c_paddleB

        if self.rect.top <= paddleT.bottom:
            return True
        elif self.rect.bottom >= paddleB.top:
            return True
        elif self.rect.top <= c_paddleT.bottom:
            return True
        elif self.rect.bottom >= c_paddleB.top:
            return True

    def paddle_hitV(self):
        paddleR = self.paddles.paddleR
        paddleL = self.cp.c_paddleL

        if self.rect.right >= paddleR.left:
            return True
        elif self.rect.left < paddleL.right:
            return True

    def update(self):
        self.centerH += (self.speedH * self.ai_settings.ball_directionH)
        self.centerV += (self.speedV * self.ai_settings.ball_directionV)

        self.rect.centerx = self.centerH
        self.rect.centery = self.centerV

    def reset(self):
        self.rect.centery = 300
        self.rect.centerx = 600

        self.centerH = float(self.rect.centerx)
        self.centerV = float(self.rect.centery)

        speed = randint(50, 101)

        self.speedH = 1 + (speed/100)
        self.speedV = 1 + (speed/100)

        direction = (-1, 1)

        self.ai_settings.ball_directionH = choice(direction)
        self.ai_settings.ball_directionV = choice(direction)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
