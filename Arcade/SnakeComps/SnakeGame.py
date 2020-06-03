import pygame
import random
import time
from itertools import cycle
from SnakeComps.Butt import Butt
from SnakeComps.Dot import Dot


def drawSnake(theSnake, frame):
    for i in theSnake:
        if i.isHead():
            pygame.draw.rect(frame, (255, 255, 255), (i.getX(), i.getY(), 10, 10))
        else:
            pygame.draw.rect(frame, (0, 255, 0), (i.getX(), i.getY(), 10, 10))


def drawDot(theDot, frame):
    pygame.draw.rect(frame, (0, 255, 0), (theDot.getX(), theDot.getY(), 10, 10))


def moveTheSnake(theSnake):
    snakeSize = len(theSnake)
    theSnake = reversed(theSnake)
    theSnakeCycle = cycle(theSnake)
    nextElement = next(theSnakeCycle)

    while 0 < snakeSize:
        snakeSize -= 1
        thisElement, nextElement = nextElement, next(theSnakeCycle)

        if thisElement.isHead():
            NESW = handleEvent(thisElement)
            if NESW == None:
                NESW = thisElement.getDir()

            if NESW == 'UP':
                thisElement.setY(thisElement.getY() - 11)
                thisElement.setDir('UP')

            if NESW == 'DOWN':
                thisElement.setY(thisElement.getY() + 11)
                thisElement.setDir('DOWN')

            if NESW == 'LEFT':
                thisElement.setX(thisElement.getX() - 11)
                thisElement.setDir('LEFT')

            if NESW == 'RIGHT':
                thisElement.setX(thisElement.getX() + 11)
                thisElement.setDir('RIGHT')
        else:
            thisElement.setX(nextElement.getX())
            thisElement.setY(nextElement.getY())


def handleEvent(thisElement):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and thisElement.getDir() != 'RIGHT':  # left arrow turns left
                return 'LEFT'
            elif event.key == pygame.K_RIGHT and thisElement.getDir() != 'LEFT':  # right arrow turns right
                return 'RIGHT'
            elif event.key == pygame.K_UP and thisElement.getDir() != 'DOWN':  # up arrow goes up
                return 'UP'
            elif event.key == pygame.K_DOWN and thisElement.getDir() != 'UP':  # down arrow goes down
                return 'DOWN'


def hit(theSnake, theDot):
    tailX = theSnake[len(theSnake) - 1].getX()
    tailY = theSnake[len(theSnake) - 1].getY()

    dotX = theDot.getX() - theSnake[0].getX()
    dotY = theDot.getY() - theSnake[0].getY()

    if dotX < 0:
        dotX *= -1
    if dotY < 0:
        dotY *= -1

    for i in theSnake:
        if not i.isHead():
            bodyX = i.getX() - theSnake[0].getX()
            bodyY = i.getY() - theSnake[0].getY()
            if bodyX < 0:
                bodyX *= -1
            if bodyY < 0:
                bodyY *= -1
            if bodyX < 10 and bodyY < 10:
                    return 'GAMEOVER'

    if dotX < 10 and dotY < 10:
        theSnake.append(Dot((tailX), (tailY), 10, 10, False))
        return 'NEWDOT'


def wallFlip(theSnake, xframe, yframe):
    snakeX = theSnake[0].getX()
    snakeY = theSnake[0].getY()

    if snakeX < 0:
        theSnake[0].setX(xframe)
    if snakeX > xframe:
        theSnake[0].setX(0)
    if snakeY < 0:
        theSnake[0].setY(yframe)
    if snakeY > yframe:
        theSnake[0].setY(0)


def activeButtons(startButton, title, goBack, GameOver, score, newGame, backToMenu,  frame):
    if startButton.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (startButton.getX(), startButton.getY(), startButton.getW(), startButton.getH()),
                         startButton.getTH())
        frame.blit(startButton.getText(), startButton.getTextRec())
    if title.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (title.getX(), title.getY(), title.getW(), title.getH()),
                         title.getTH())
        frame.blit(title.getText(), title.getTextRec())
    if goBack.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (goBack.getX(), goBack.getY(), goBack.getW(), goBack.getH()),
                         goBack.getTH())
        frame.blit(goBack.getText(), goBack.getTextRec())
    if GameOver.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (GameOver.getX(), GameOver.getY(), GameOver.getW(), GameOver.getH()),
                         GameOver.getTH())
        frame.blit(GameOver.getText(), GameOver.getTextRec())
    if score.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (score.getX(), score.getY(), score.getW(), score.getH()),
                         score.getTH())
        frame.blit(score.getText(), score.getTextRec())
    if newGame.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (newGame.getX(), newGame.getY(), newGame.getW(), newGame.getH()),
                         newGame.getTH())
        frame.blit(newGame.getText(), newGame.getTextRec())
    if backToMenu.getButStat():
        pygame.draw.rect(frame, (0, 255, 0),
                         (backToMenu.getX(), backToMenu.getY(), backToMenu.getW(), backToMenu.getH()),
                         startButton.getTH())
        frame.blit(backToMenu.getText(), backToMenu.getTextRec())




class SnakeGame:
    def __init__(self, frame, X, Y):
        self.frame = frame
        self.x = X
        self.y = Y
        self.score = 0
        self.start()

    def start(self):
        running = True
        w = 110
        h = 50
        th = 2
        green = (0, 255, 0)
        black = (0, 0, 0)
        self.frame.fill((0, 0, 0))
        startButton = Butt((self.x / 2) - (w / 2), (self.y / 2) - (h / 2), w, h, th, green, black, 'Start', 32, True)
        title = Butt((self.x / 2) - (w / 2), (self.y / 4) - (h / 2), w, h, 0, green, black, 'SNAKE!', 50, True)

        goBack = Butt(0, (self.y - h), w, h, th, green, black, 'Back', 32, True)
        GameOver = Butt((self.x / 2) - (w / 2), (self.y / 4) - (h / 2), w, h, 0, (255, 0, 0), black, 'GAMEOVER!', 50, False)

        score = Butt(0, 0, w / 1.5, h / 2, 1, green, black, 'Score: 0', 16, False)
        newGame = Butt((self.x / 2) - (w / 2) - 50, (self.y / 2) - (h / 2), w + 100, h, th, green, black, 'New Game?', 32, False)
        backToMenu = Butt(0, (self.y - h), w, h, th, green, black, 'Menu', 32, False)

        while True:
            mouse = pygame.mouse.get_pos()
            activeButtons(startButton, title, goBack, GameOver, score, newGame, backToMenu,  self.frame)

            if goBack.isOver(mouse[0], mouse[1], (1, 0, 0)) and goBack.getButStat() or backToMenu.isOver(mouse[0], mouse[1], (1, 0, 0)) and backToMenu.getButStat():
                return

            if newGame.isOver(mouse[0], mouse[1], (1, 0, 0)) and newGame.getButStat():
                self.score = 0;
                self.start();

            if startButton.isOver(mouse[0], mouse[1], (1, 0, 0)) and startButton.getButStat():
                self.frame.fill((0, 0, 0))
                theSnake = []
                score.setButStat(True)
                startButton.setButStat(False)
                goBack.setButStat(False)
                title.setButStat(False)

                for i in range(1, 6):
                    if i == 1:
                        theSnake.append(Dot((self.x / 2) + (-11 * i), (self.y / 2), 10, 10, True))
                    else:
                        theSnake.append(Dot((self.x / 2) + (-11 * i), (self.y / 2), 10, 10, False))

                x = random.randint(self.x / self.x, self.x)
                y = random.randint(self.y / self.y, self.y)
                theDot = Dot(x, y, 10, 10, False)

                moveTimer = time.time()
                speed = 1

                while running:
                    activeButtons(startButton, title, goBack, GameOver, score, newGame, backToMenu, self.frame)

                    pygame.display.update()
                    drawSnake(theSnake, self.frame)

                    drawDot(theDot, self.frame)
                    wallFlip(theSnake, self.x, self.y)

                    isHit = hit(theSnake, theDot)

                    if isHit == 'NEWDOT':
                        speed += 1
                        del theDot
                        x = random.randint(self.x / self.x, self.x)
                        y = random.randint(self.y / self.y, self.y)
                        theDot = Dot(x, y, 10, 10, False)
                        self.score += 1
                        score.setText("Score: " + str(self.score))

                    if isHit == 'GAMEOVER':
                        GameOver.setButStat(True)
                        newGame.setButStat(True)
                        backToMenu.setButStat(True)
                        running = False

                    if (time.time() - moveTimer) > (1 / speed):
                        moveTimer = time.time()
                        moveTheSnake(theSnake)
                        self.frame.fill((0, 0, 0))

            pygame.display.update()
            handleEvent(None)

    def showSnake(self, frame, color, size):
        for i in range(0, size):
            pygame.draw.rect(frame, color, (500 + (i * 5), 500, 5, 5))

    def genDot(self, frame, color, xpos, ypos, newDot):
        pygame.draw.rect(frame, color, (xpos, ypos, 10, 10))
        if newDot:
            self.setNewDot()

    def setNewDot(self):
        self.frame.fill(self.backgroundColor)
        self.randoX = random.randint(1, 1000)
        self.randoY = random.randint(1, 1000)
        self.makeNewDot = False
