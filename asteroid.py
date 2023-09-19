#############################################################
# FILE   : asteroid.py
# WRITER : OREN EYAL, oreneyal15
# WRITER : DANIEL TAL, danieltal
# EXERCISE : intro2cs1 ex10 2021
#############################################################
import math


class Asteroid:
    """this class creates an asteroid for the game asteroids"""

    def __init__(self, x_location, y_location, x_speed, y_speed, size):
        self.__x_speed = x_speed
        self.__size = size
        self.__y_speed = y_speed
        self.__x_location = x_location
        self.__y_location = y_location

    def get_location(self):
        """returns the location of the asteroid"""
        return self.__x_location, self.__y_location

    def get_x_speed(self):
        """returns the speed of the asteroid on the x line"""
        return self.__x_speed

    def get_y_speed(self):
        """returns the speed of the asteroid on the y line"""
        return self.__y_speed

    def set_new_location(self, new_x, new_y):
        """sets a new location to the asteroid"""
        self.__x_location = new_x
        self.__y_location = new_y

    def has_intersection(self, obj):
        """this function checks if an object hit the asteroid"""
        obj_x, obj_y = obj.get_location()
        ast_x, ast_y = self.get_location()
        distance = ((obj_x - ast_x) ** 2 + (obj_y - ast_y) ** 2) ** 0.5
        if distance <= self.get_radius() + obj.get_radius():
            return True
        else:
            return False

    def get_radius(self):
        """returns the asteroids radius"""
        return self.__size * 10 - 5

    def get_size(self):
        """returns the asteroids size"""
        return self.__size
