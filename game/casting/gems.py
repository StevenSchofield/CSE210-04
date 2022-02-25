from game.casting.fallingObject import FallingObject
""""The Gems class will inherit from falling objects 
    and will be worth a score of 5"""
class Gems(FallingObject):
    def __init__(self, score=5):
        super().__init__()
        self._score = score
        self.set_text('*')
    def getScore(self):
        return self._score