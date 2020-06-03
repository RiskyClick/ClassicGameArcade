class Dot:
    def __init__(self, x, y, w, h, head):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.head = head
        self.direction = 'RIGHT'

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, num):
        self.x = num

    def setY(self, num):
         self.y = num

    def isHead(self):
        return self.head

    def getDir(self):
        return self.direction

    def setDir(self, newDir):
        self.direction = newDir