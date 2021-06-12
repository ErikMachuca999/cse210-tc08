import random
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"][0]

        # for brick in bricks:
        #     if ball.get_position().equals(brick.get_position()):
        #         description = brick.get_description()
        
        # ceiling collision
        for x in range(0, constants.MAX_X):
            if ball.get_position().equals(Point(x, 1)):
                velocity = ball.get_velocity()
                ball.set_velocity(Point(velocity.get_x(), velocity.get_y()*-1))
        # left wall
        # for x in range(0, constants.MAX_X):
        #     if ball.get_position().equals(Point(x, 1)):
        #         velocity = ball.get_velocity()
        #         ball.set_velocity(Point(velocity.get_x(), velocity.get_y()*-1))




        for x in range(0, constants.MAX_Y):
            if ball.get_position().equals(Point(20, x)):
                quit()