import pygame
from SnakeComps.SnakeGame import SnakeGame
from SnakeComps.Butt import Butt
from MissleComps.MissleGame import MissleGame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

X = 750
Y = 500

startSnakeGame = False

pygame.init()
startPage = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Arcade')
font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('Arcade', True, green, black)

textRect = text.get_rect()
textRect.center = (X // 2, Y // 4)

def drawGames():
    mouse = pygame.mouse.get_pos()
    xPos = X / 5
    yPos = Y / 2
    width = 110
    hight = 50
    thick = 2
    
    SNAKE = Butt(X / 5, Y / 2, width, hight, thick, green, black, "Snake", 32, True)
    pygame.draw.rect(startPage, white, (SNAKE.getX(), SNAKE.getY(), SNAKE.getW(), SNAKE.getH()), SNAKE.getTH())
    startPage.blit(SNAKE.getText(), SNAKE.getTextRec())

    MISSLE = Butt(X / 5 * 2, Y / 2, width, hight, thick, green, black, "Missle", 32, True)
    pygame.draw.rect(startPage, white, (MISSLE.getX(), MISSLE.getY(), MISSLE.getW(), MISSLE.getH()), MISSLE.getTH())
    startPage.blit(MISSLE.getText(), MISSLE.getTextRec())

    null = Butt(X / 5 * 3, Y / 2, width, hight, thick, green, black, "null", 32, True)
    pygame.draw.rect(startPage, white, (null.getX(), null.getY(), null.getW(), null.getH()), null.getTH())
    startPage.blit(null.getText(), null.getTextRec())

    if SNAKE.isOver(mouse[0], mouse[1], (1, 0, 0)):
        snakeGame = SnakeGame(startPage, X, Y)

    if MISSLE.isOver(mouse[0], mouse[1], (1, 0, 0)):
        missleGame = MissleGame(startPage, X, Y)


while True:
    startPage.fill(black)
    startPage.blit(text, textRect)
    drawGames()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
