from game.casting.cast import Cast
from game.casting.gems import Gems
from game.casting.rocks import Rocks
from game.shared.coordinate import Coordinate
from game.shared.color import Color
import random

COLORS = [Color(0, 255, 0),
    Color(0, 0, 255),
    Color(255, 0, 0),
    Color(255, 255, 0)]

class Spawner:
    """An object that spawns actors.
    
    Attributes:
        _spawn_rate (int): controls how many objects are spawned.
    """

    def __init__(self, columns, rows, cell_size, spawn_rate=100):
        """Constructs a new Spawner with the specified spawn_rate.
        """
        self._columns = columns
        self._rows = rows
        self._cell_size = cell_size
        self._spawn_rate = spawn_rate

    def _spawn_object(self, cast:Cast):
        """Adds random objects to the cast.
        
        Args:
            cast (Cast): The cast of actors.
        """
        spawn = random.randint(0,self._spawn_rate)
        x = random.randint(1, self._columns - 1)
        y = 1
        position = Coordinate(x, y)
        position = position.scale(self._cell_size)
        if spawn > 75:
            gem = Gems()
            gem.set_color(COLORS[random.randint(0, len(COLORS)-1)])
            gem.set_position(position)
            cast.add_actor("gem", gem)
        elif spawn > 50:
            rock = Rocks()
            rock.set_position(position)
            cast.add_actor("rock", rock)