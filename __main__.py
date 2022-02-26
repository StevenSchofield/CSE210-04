import os
import random

from game.casting.actor import Actor
from game.casting.player import Player
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
HEADER_FONT_SIZE = 60
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40
SPAWN_RATE = 150


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

    # create the lives banner
    lives = Actor()
    lives.set_text("Lives: 3")
    lives.set_font_size(FONT_SIZE)
    lives.set_color(WHITE)
    lives.set_position(Coordinate(CELL_SIZE, CELL_SIZE))
    cast.add_actor("banners", lives)
    
    
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Coordinate(x, y)

    player = Player()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)


    ## setup the start screen
    startScreenCast = Cast()

    title = Actor()
    title.set_text("GREED")
    title.set_color(WHITE)
    title.set_font_size(HEADER_FONT_SIZE)
    title.set_position(Coordinate(round(MAX_X/4), round(MAX_Y/4)))
    startScreenCast.add_actor("title screen", title)

    start = Actor()
    start.set_text("Press ENTER to start")
    start.set_color(WHITE)
    start.set_font_size(FONT_SIZE)
    start.set_position(Coordinate(round(MAX_X/3), round(MAX_Y/2)))
    startScreenCast.add_actor("title screen", start)
    
    ## setup the end game screen
    endScreenCast = Cast()

    youLoose = Actor()
    youLoose.set_text("You died!")
    youLoose.set_color(WHITE)
    youLoose.set_font_size(HEADER_FONT_SIZE)
    youLoose.set_position(Coordinate(round(MAX_X/4), round(MAX_Y/4)))
    endScreenCast.add_actor("loose screen", youLoose)

    scoreDisplay = Actor()
    scoreDisplay.set_text("Your score: ")
    scoreDisplay.set_color(WHITE)
    scoreDisplay.set_font_size(FONT_SIZE)
    scoreDisplay.set_position(Coordinate(round(MAX_X/3), round(MAX_Y/2)-CELL_SIZE*2))
    endScreenCast.add_actor("loose screen score", scoreDisplay)

    tryAgain = Actor()
    tryAgain.set_text("Press ENTER to try again")
    tryAgain.set_color(WHITE)
    tryAgain.set_font_size(FONT_SIZE)
    tryAgain.set_position(Coordinate(round(MAX_X/3), round(MAX_Y/2)))
    endScreenCast.add_actor("loose screen", tryAgain)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    spawner = Spawner(COLS, ROWS, CELL_SIZE, SPAWN_RATE)
    director = Director(keyboard_service, video_service, spawner)
    director.start_game(cast, startScreenCast, endScreenCast)

if __name__ == "__main__":
    main()