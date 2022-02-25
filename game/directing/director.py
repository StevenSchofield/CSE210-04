from game.casting.cast import Cast


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _spawner (Spawner): For spawning objects.
    """

    def __init__(self, keyboard_service, video_service, spawner):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._spawner = spawner
        self.score = 0

        self._screen = 2
        
    def start_game(self, gameCast, startScreenCast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            if self._screen == 1:
                self._do_outputs(startScreenCast)
                if self._keyboard_service.pressed_enter():
                    self._screen = 2
            elif self._screen == 2: 
                self._get_inputs(gameCast)
                self._do_updates(gameCast)
                self._do_outputs(gameCast)
            else:
                self._video_service.close_window()
        self._video_service.close_window()

    def _get_inputs(self, cast:Cast):
        """   
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast:Cast):
        """Updates the player and all falling object's positions and handles collisions
        
        Args:
            cast (Cast): The cast of actors.
        """
        scoreBanner = cast.get_first_actor("banners")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        player = cast.get_first_actor("player")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        """
        for artifact in artifacts:
                message = artifact.get_message()
                scoreBanner.set_text(message)"""
        
        for rock in rocks:
            rock.falling(max_x, max_y)
            if player.get_position().equals(rock.get_position()):
                player.change_lives(1)
                cast.remove_actor("rocks", rock)
            if rock.get_position().get_y() > self._video_service.get_height():
                cast.remove_actor("rocks", rock)

        for gem in gems:
            rock.falling(max_x, max_y)
            if player.get_position().equals(gem.get_position()):
                self.score += gem.getScore()
                scoreBanner.set_text(f"Score: {self.score}")
                cast.remove_actor("gems", gem)
            if gem.get_position().get_y() > self._video_service.get_height():
                cast.remove_actor("gems", gem)
            
        self._spawner.spawn_object(cast)
        
    def _do_outputs(self, cast:Cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()