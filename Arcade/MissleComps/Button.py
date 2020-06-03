import pygame


def text_objects(title, smallText, txtColor):
    textSurface = smallText.render(title, True, txtColor)
    return textSurface, textSurface.get_rect()


class Button:
    def __init__(self, title, xpos, ypos, w, h, thi, active, id, sizeFont, txtColor):
        self.title = title
        self.xpos = xpos
        self.ypos = ypos
        self.w = w
        self.h = h
        self.thi = thi
        self.active = active
        self.id = id
        self.smallText = pygame.font.Font("freesansbold.ttf", sizeFont)
        self.textSurf, self.textRect = text_objects(title, self.smallText, (255, 255, 255))
        self.textRect.center = ((xpos + (w / 2)), (ypos + (h / 2)))


    def getX(self):
        return self.xpos

    def setX(self, newX):
        self.xpos = newX

    def getY(self):
        return self.ypos

    def setY(self, newY):
        self.ypos = newY

    def getW(self):
        return self.w

    def setW(self, newW):
        self.w = newW

    def getThi(self):
        return self.thi

    def setThi(self, newThi):
        self.thi = newThi

    def getH(self):
        return self.h

    def setH(self, newH):
        self.h = newH

    def getActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def clicked(self, mouse0, mouse1, clicked):
        if self.xpos < mouse0 < (self.xpos + self.w) and self.ypos < mouse1 < (self.ypos + self.h) and pygame.mouse.get_pressed() == clicked:
            return True
        else:
            return False


