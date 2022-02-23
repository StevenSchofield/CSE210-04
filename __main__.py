import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director
from game.directing.spawner import Spawner

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.coordinate import Coordinate


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40
SPAWN_RATE = 100


def main():
    
    # create the cast
    cast = Cast()

    # create the score banner
    score = Actor()
    score.set_text("Score: 0")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Coordinate(CELL_SIZE, 0))
    cast.add_actor("banners", score)
    
    
    x = int(MAX_X / 2)
    y = int(MAX_Y - 2)
    position = Coordinate(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)

    """
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.randint(33, 126))
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Coordinate(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)"""
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    spawner = Spawner(COLS, ROWS, SPAWN_RATE)
    director = Director(keyboard_service, video_service, spawner)
    director.start_game(cast)


if __name__ == "__main__":
    main()