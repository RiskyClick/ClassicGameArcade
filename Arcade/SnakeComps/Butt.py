import pygame


class Butt:
    def __init__(self, x, y, w, h, th, textColor, backColor, txt, fontSize, active):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.th = th
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        self.text = self.font.render(txt, True, textColor, backColor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x + (w / 2), y + (h / 2))
        self.textColor = textColor
        self.backColor = backColor
        self.active = active

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getW(self):
        return self.w

    def getH(self):
        return self.h

    def getTH(self):
        return self.th

    def getFont(self):
        return self.font

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = self.font.render(txt, True, self.textColor, self.backColor)

    def getTextRec(self):
        return self.textRect

    def isOver(self, mouse0, mouse1, clicked):
        if self.getX() < mouse0 < (self.getX() + self.getW()) and self.getY() < mouse1 < (self.getY() + self.getH()) and pygame.mouse.get_pressed() == clicked:
            return True
        else:
            return False

    def getButStat(self):
        return self.active

    def setButStat(self, bool):
        self.active = bool