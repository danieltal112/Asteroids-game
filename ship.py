#############################################################
# FILE   : ship.py
# WRITER : OREN EYAL, oreneyal15
# WRITER : DANIEL TAL, danieltal
# EXERCISE : intro2cs1 ex10 2021
#############################################################
class Ship:
    """this class creates a ship for the game asteroids"""

    __SHIP_RADIUS = 1

    def __init__(self, x_location, y_location, direction=0):
        self.__x_speed = 0
        self.__y_speed = 0
        self.__x_location = x_location
        self.__y_location = y_location
        self.__direction = direction

    def get_location(self):
        """returns the location of the ship"""
        return self.__x_location, self.__y_location

    def get_direction(self):
        """return the direction of the ship"""
        return self.__direction

    def get_x_speed(self):
        """returns the speed of the ship on the x line"""
        return self.__x_speed

    def get_y_speed(self):
        """returns the speed of the ship on the y line"""
        return self.__y_speed

    def set_new_location(self, new_x, new_y):
        """sets a new location to the ship"""
        self.__x_location = new_x
        self.__y_location = new_y

    def set_direction(self, new_direction):
        """sets the ships direction to a new one"""
        self.__direction = new_direction

    def set_y_speed(self, new_speed):
        """sets a new speed to the y line"""
        self.__y_speed += new_speed

    def set_x_speed(self, new_speed):
        """sets a new speed to the x line"""
        self.__x_speed += new_speed

    def get_radius(self):
        """returns the ship radius"""
        return self.__SHIP_RADIUS
