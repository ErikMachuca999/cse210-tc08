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
        # wall collision
        for y in range(0, constants.MAX_Y):
            if ball.get_position().equals(Point(1, y)) or ball.get_position().equals(Point(79, y)) :
                velocity = ball.get_velocity()
                ball.set_velocity(Point(velocity.get_x()*-1, velocity.get_y()))
        
        for i in range(0, 11):
            if ball.get_position().equals(paddle.get_position()): # + Point(i, -1)):
                velocity = ball.get_velocity()
                ball.set_velocity(Point(velocity.get_x(), velocity.get_y()*-1))





        # for x in range(0, constants.MAX_X):
        #     if ball.get_position().equals(Point(x, 19)):
        #         quit()