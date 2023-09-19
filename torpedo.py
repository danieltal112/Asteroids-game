#############################################################
# FILE   : torpedo.py
# WRITER : OREN EYAL, oreneyal15
# WRITER : DANIEL TAL, danieltal
# EXERCISE : intro2cs1 ex10 2021
#############################################################
class Torpedo:
    """this class creates a torpedo for the game asteroids"""
    __TORPEDO_RADIUS = 4

    def __init__(self, x_location, y_location, x_speed, y_speed,
                 direction, life_cycle):
        self.__x_speed = x_speed
        self.__y_speed = y_speed
        self.__x_location = x_location
        self.__y_location = y_location
        self.__direction = direction
        self.__life_cycle = life_cycle

    def get_location(self):
        """returns the location of the torpedo"""

        return self.__x_location, self.__y_location

    def get_x_speed(self):
        """returns the speed of the torpedo on the x line"""

        return self.__x_speed

    def get_y_speed(self):
        """returns the speed of the torpedo on the y line"""

        return self.__y_speed

    def get_direction(self):
        """returns the torpedoes direction"""
        return self.__direction

    def set_new_location(self, new_x, new_y):
        """sets a new location to the torpedo"""
        self.__x_location = new_x
        self.__y_location = new_y

    def get_radius(self):
        """returns the radius of a torpedo"""
        return self.__TORPEDO_RADIUS

    def get_life_cycle(self):
        """returns the game cycle when the torpedo was created"""
        return self.__life_cycle


