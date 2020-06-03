import os
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        current_path = os.path.dirname(__file__)
        toResourses = os.path.join(current_path, 'Resources')
        self.image = pygame.image.load(os.path.join(toResourses, 'Tank.png'))
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] / 5), int(self.size[1] / 5)))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.activeAim = False
        self.getAimX = 0
        self.getAimY = 0

    def setActiveAim(self, bool):
        self.activeAim = bool

    def setAim(self, x, y):
        self.getAimX = x
        self.getAimY = y
