from MissleComps.Button import Button

black = (0, 0, 0)

def buttonGen(x, y):
    list = []
    list.append(Button('New Game', x / 2 - 50, y / 2, 100, 50, 2, False, 'GAMEOVER', 32, black))
    list.append(Button('Start', x / 2 - 50, y / 1.5, 100, 50, 2, False, 'START', 32, black))
    list.append(Button('Back', 0, y - 50, 100, 50, 2, False, 'START', 16, black))
    list.append(Button('Menu', 0, y - 50, 100, 50, 2, False, 'GAMEOVER', 16, black))
    list.append(Button('G', 0, y / 4, 50, 50, 2, False, 'GAMEON', 16, black))
    list.append(Button('B', 0, y / 4 + 50, 50, 50, 2, False, 'GAMEON', 16, black))
    list.append(Button('M', 0, y / 4 + 100, 50, 50, 2, False, 'GAMEON', 16, black))
    list.append(Button('G', x - 50, y / 2, 50, 50, 2, False, 'GAMEON', 16, black))
    list.append(Button('B', x - 50, y / 2 + 50, 50, 50, 2, False, 'GAMEON', 16, black))
    list.append(Button('M', x - 50, y / 2 + 100, 50, 50, 2, False, 'GAMEON', 16, black))
    return list


class MakeAllButtons:
    def __init__(self, x, y):
        self.listOfButtons = buttonGen(x, y)