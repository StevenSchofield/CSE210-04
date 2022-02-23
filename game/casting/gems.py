from game.casting.fallingObject import FallingObject
class Gems(FallingObject):
    def __init__(self, score=5):
        super().__init__()
        self._score = score
        self.set_text(['*']);
    def getScore(self):
        return self._score