from game.casting.actor import Actor
from game.shared.coordinate import Coordinate
class FallingObject(Actor):

    def __init__(self):
        super().__init__()
        self.message = ""
        self._position = Coordinate(0,0)
        
    def falling(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Coordinate(x, y)
    
    
