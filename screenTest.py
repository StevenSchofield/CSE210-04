import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService

from game.shared.color import Color
from game.shared.coordinate import Coordinate

MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
HEADER_FONT_SIZE = 60
COLS = 60
ROWS = 40

WHITE = Color(255, 255, 255)

screenCast = Cast()

title = Actor()
title.set_text("GREED")
title.set_color(WHITE)
title.set_font_size(HEADER_FONT_SIZE)
title.set_position(Coordinate(round(MAX_X/4), round(MAX_Y/4)))
screenCast.add_actor("title screen", title)

start = Actor()
start.set_text("Press ENTER to start")
start.set_color(WHITE)
start.set_font_size(FONT_SIZE)
start.set_position(Coordinate(round(MAX_X/2), round(MAX_Y/2)))
screenCast.add_actor("title screen", start)

keyboard_service = KeyboardService(CELL_SIZE)
video_service = VideoService("Test", MAX_X, MAX_Y, CELL_SIZE, 12)

video_service.open_window()
while video_service.is_window_open():
    video_service.clear_buffer()
    actors = screenCast.get_all_actors()
    video_service.draw_actors(actors)
    video_service.flush_buffer()

    if keyboard_service.pressed_enter():
        video_service.close_window()
video_service.close_window()