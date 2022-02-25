from pickle import FALSE
from game.casting.fallingObject import FallingObject
""""Rocks will inherit from falling object and 
    will have a hit function that will be activated
    when there is a collision."""
class Rocks(FallingObject):
    def __init__(self):
        super().__init__()
        self._hit = FALSE
        self.set_text('O')
    def getHit(self):
        return self._hit
        
        