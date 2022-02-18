from game.casting.fallingObject import FallingObject
class Rocks(FallingObject):
    def __init__(self, hit):
        super().__init__()
        _hit = hit
    def getHit(self):
        return self._hit
        
        