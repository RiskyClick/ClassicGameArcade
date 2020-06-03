class GameState:
    def __init__(self):
        self.gameState = 'START'

    def getGameState(self):
        return self.gameState

    def setGameState(self, newState):
        self.gameState = newState