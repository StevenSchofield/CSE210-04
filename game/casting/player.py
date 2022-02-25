from game.casting.actor import Actor


# cast = Cast()
# player = Actor()
# player.set_text("#")
# cast.add_actor("robots", player)
# change = 0

class Player(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 3

    def decrease_lives(self, decrease = 1):

        self._lives -= decrease
        return self._lives

