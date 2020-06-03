import os
import math
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 250])
        current_path = os.path.dirname(__file__)
        toResourses = os.path.join(current_path, 'Resources')
        self.image = pygame.image.load(os.path.join(toResourses, 'Gun.png'))
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 25), int(self.size[1] / 25)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

    def shoot(self, xStart, yStart, xEnd, yEnd):
        x_diff = xEnd - xStart
        y_diff = yEnd - yStart
        angle = math.atan2(y_diff, x_diff)
        x = float(math.cos(angle))
        y = float(math.sin(angle))
        tempX = self.rect.x + x
        tempY = self.rect.y + y
        if(tempY == self.rect.y) or (tempX == self.rect.x):
            self.rect.y += (y * 2)
            self.rect.x += (x * 2)
        else:
            self.rect.y += (y)
            self.rect.x += (x)

    def hit(self):
        if self.rect.x < 0 or self.rect.x > 1750 or self.rect.y < 0 or self.rect.y > 500:
            self.kill()
            return True
        else:
            return False