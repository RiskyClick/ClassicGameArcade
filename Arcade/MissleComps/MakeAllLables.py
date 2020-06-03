from MissleComps.Lable import Lable

black = (0, 0, 0)

def lableGen(x, y):
    list = []
    list.append(Lable('MISSLE DEFENCE!', x / 2, y / 3, False, 'START', 50, black))
    list.append(Lable('GAME OVER!', x / 2, y / 3, False, 'GAMEOVER', 50, black))
    list.append(Lable('winner loser thinig', x / 2, y / 1.5, False, 'GAMEOVER', 32, black))
    list.append(Lable('Player 1', x / 2, 32, False, "GAMEON", 32, black))
    return list


class MakeAllLables:
    def __init__(self, x, y):
        self.listOfLables = lableGen(x, y)