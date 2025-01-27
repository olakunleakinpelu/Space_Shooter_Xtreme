import pygame
import random

from os import path
from constant import *

## defines the sprite for bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        if direction < 0: 
            self.image = bullet_img 
        else:
            self.image = ebullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        if direction == 0:
            print("CANT DO")
        else:
            self.rect.bottom = y 
            self.rect.centerx = x
            self.speedy = direction

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0 or self.rect.bottom > HEIGHT:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop
