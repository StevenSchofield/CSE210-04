from pickle import FALSE
from game.casting.fallingObject import FallingObject
class Rocks(FallingObject):
    def __init__(self):
        super().__init__()
        self._hit = FALSE;
        self.set_text(['O'])
    def getHit(self):
        return self._hit
        
        