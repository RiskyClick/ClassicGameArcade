import pygame


def text_objects(title, smallText, txtColor):
    textSurface = smallText.render(title, True, txtColor)
    return textSurface, textSurface.get_rect()

class Lable:
    def __init__(self, title, xpos, ypos, active, id, sizeFont, txtColor):
        self.largeText = pygame.font.Font('freesansbold.ttf', sizeFont)
        self.textSurf, self.textRect = text_objects(title, self.largeText, txtColor)
        self.textRect.center = (xpos, ypos)
        self.id= id
        self.active = active

    def setActive(self, bool):
        self.active = bool

    def getActive(self):
        return self.active
