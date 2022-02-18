from game.casting.gems import Gems
from game.casting.rock import Rocks
from game.shared.coordinate import Coordinate
import random

class Spawner:
    """An object that spawns actors.
    
    Attributes:
        _spawn_rate (int): controls how many objects are spawned.
    """

    def __init__(self, columns, rows, cell_size, spawn_rate):
        """Constructs a new Spawner with the specified spawn_rate.
        """
        self._columns = columns
        self._rows = rows
        self._cell_size = cell_size
        self._spawn_rate = spawn_rate

    def _spawn_object(self, cast):
        """Adds random objects to the cast.
        
        Args:
            cast (Cast): The cast of actors.
        """
        spawn = random.randint(0,100)
        x = random.randint(1, self._columns - 1)
        y = random.randint(1, self._rows - 1)
        position = Coordinate(x, y)
        position = position.scale(self._cell_size)
        if spawn > 75:
            gem = Gems()
            cast.add_actor("gem", gem)
            cast.set
        elif spawn > 50:
            rock = Rocks()
            cast.add_actor("rock", rock)