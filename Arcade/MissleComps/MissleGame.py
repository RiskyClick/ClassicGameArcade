import pygame
from MissleComps.GameState import GameState
from MissleComps.MakeAllButtons import MakeAllButtons
from MissleComps.MakeAllLables import MakeAllLables
from MissleComps.Player import Player
from MissleComps.Projectile import Projectile


def buttonClicked(buttons, lables, frame, player):
    leftClick = (1, 0, 0)
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            player.setActiveAim(False) if player.activeAim else player.setActiveAim(True)
            player.setAim(mouse[0], mouse[1])

    for i in lables:
        if i.getActive():
            frame.blit(i.textSurf, i.textRect)


    for i in buttons:
        if i.getActive():
            frame.blit(i.textSurf, i.textRect)
            if i.clicked(mouse[0], mouse[1], leftClick):
                return i.title


def toggleButtons(listOfButtons, listOfLables, state):
    for i in listOfButtons:
        if state != i.id:
            i.setActive(False)
        else:
            i.setActive(True)

    for i in listOfLables:
        if state != i.id:
            i.setActive(False)
        else:
            i.setActive(True)


def shotsFired(tankX, tankY, all_sprites, frame, player1):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE] and len(all_sprites) < 2:
        shot = Projectile(0, 0)
        shot.rect.x = tankX
        shot.rect.y = tankY
        all_sprites.add(shot)
        count = 0
        print(len(all_sprites))

        while not shot.hit():
            all_sprites.update()
            all_sprites.draw(frame)
            pygame.display.flip()
            shot.shoot(tankX, tankY, player1.getAimX, player1.getAimY)
            count += 1
        print(len(all_sprites))


def aiming(frame, color, xPos, yPos, player):
    mouse = pygame.mouse.get_pos()
    if player.activeAim:
        pygame.draw.line(frame, color, (xPos, yPos), (mouse[0], mouse[1]), 2)
    else:
        pygame.draw.line(frame, color, (xPos, yPos), (player.getAimX, player.getAimY), 2)


class MissleGame:
    def __init__(self, frame, x, y):
        self.x = x + 1000
        self.y = y
        self.frame = pygame.display.set_mode((self.x, self.y))
        self.start(self.frame, self.x, self.y)

    def start(self, frame, frameWidth, frameHeight):
        gameState = GameState()
        buttons = MakeAllButtons(self.x, self.y)
        lables = MakeAllLables(self.x, self.y)
        all_sprites = pygame.sprite.Group()
        player1 = Player(473, 253)
        player1.rect.x = 0
        player1.rect.y = frameHeight - (253 / 5)
        all_sprites.add(player1)

        while True:
            frame.fill((150, 150, 150))
            pygame.display.update()
            toggleButtons(buttons.listOfButtons, lables.listOfLables, gameState.getGameState())

            while gameState.getGameState() == 'START':
                pygame.display.update()
                choice = buttonClicked(buttons.listOfButtons, lables.listOfLables, frame, player1)
                if choice == 'Start':
                    gameState.setGameState('GAMEON')
                    toggleButtons(buttons.listOfButtons, lables.listOfLables, gameState.getGameState())
                    frame.fill((150, 150, 150))
                if choice == 'Back':
                    return

            while gameState.getGameState() == 'GAMEON':
                frame.fill((150, 150, 150))
                choice = buttonClicked(buttons.listOfButtons, lables.listOfLables, frame, player1)
                shotsFired((player1.rect.x + 90), (player1.rect.y), all_sprites, frame, player1)
                aiming(frame, (0, 0, 255), (player1.rect.x + 90), (player1.rect.y + 12), player1)
                all_sprites.update()
                all_sprites.draw(frame)
                pygame.display.flip()

            while gameState.getGameState() == 'GAMEOVER':
                toggleButtons(buttons.listOfButtons, lables.listOfLables, gameState.getGameState())
                choice = buttonClicked(buttons.listOfButtons, lables.listOfLables, frame)
