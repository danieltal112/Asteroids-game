#############################################################
# FILE   : asteroids_main.py
# WRITER : OREN EYAL, oreneyal15
# WRITER : DANIEL TAL, danieltal
# EXERCISE : intro2cs1 ex10 2021
#############################################################

from screen import Screen
import sys
import random
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import math

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    __LIFE_CYCLE_TORPEDO = 200
    __DEG = 7
    __LOW_SCORE = 20
    __MID_SCORE = 50
    __HIGH_SCORE = 100
    __BIG_SIZE = 3
    __MID_SIZE = 2
    __SMALL_SIZE = 1
    __MAX_TORPEDO = 10
    __SPEED_ASTEROID_LST = [-4, -3, -2, -1, 1, 2, 3, 4]

    def __init__(self, asteroids_amount):
        """this function initialize the game"""
        self.__screen = Screen()
        self.__num_asteroids = asteroids_amount
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        self.__game_ship = self.__init_ship()
        self.__game_asteroids = self.__init_asteroids()
        self.__life_ship = 3
        self.__game_torpedo = []
        self.__score = 0
        self.__flag_loop = 0

    def __init_ship(self):
        """this function create the first game ship"""
        x_location = random.randint(self.__screen_min_x, self.__screen_max_x)
        y_location = random.randint(self.__screen_min_y, self.__screen_max_y)
        ship = Ship(x_location, y_location)
        return ship

    def __init_asteroids(self):
        """this function create the asteroids for the game"""
        asteroid_lst = []
        x, y = self.__game_ship.get_location()
        for i in range(self.__num_asteroids):

            x_location = random.randint(self.__screen_min_x,
                                        self.__screen_max_x)
            y_location = random.randint(self.__screen_min_y,
                                        self.__screen_max_y)
            speed_x = random.choice(self.__SPEED_ASTEROID_LST)
            speed_y = random.choice(self.__SPEED_ASTEROID_LST)

            asteroid = Asteroid(x_location, y_location, speed_x, speed_y,
                                self.__BIG_SIZE)
            while asteroid.has_intersection(self.__game_ship):
                asteroid.x_location = random.randint(self.__screen_min_x,
                                                     self.__screen_max_x)
                asteroid.y_location = random.randint(self.__screen_min_y,
                                                     self.__screen_max_y)

            asteroid_lst.append(asteroid)
            self.__screen.register_asteroid(asteroid, self.__BIG_SIZE)
        return asteroid_lst

    def __draw_all_asteroids(self):
        """this function draws the asteroids in the game"""
        for asteroid in self.__game_asteroids:
            x, y = asteroid.get_location()
            self.__screen.draw_asteroid(asteroid, x, y)

    def __draw_all_torpedo(self):
        """this function draws the torpedos in the game"""
        for torpedo in self.__game_torpedo:
            x, y = torpedo.get_location()
            self.__screen.draw_torpedo(torpedo, x, y, torpedo.get_direction())

    def __move_obj(self, obj):
        """this function moves objects in the game"""
        x, y = obj.get_location()
        y_speed = obj.get_y_speed()
        x_speed = obj.get_x_speed()
        new_x = self.__screen_min_x + (x + x_speed - self.__screen_min_x) % (
                self.__screen_max_x - self.__screen_min_x)
        new_y = self.__screen_min_y + (y + y_speed - self.__screen_min_y) % (
                self.__screen_max_y - self.__screen_min_y)
        obj.set_new_location(new_x, new_y)

    def __move_all_asteroids(self):
        """this function uses __move_obj to move asteroids in the game"""
        for asteroid in self.__game_asteroids:
            self.__move_obj(asteroid)

    def __move_right(self):
        """this function change the degree of the ship head to the right """
        new_direction = self.__game_ship.get_direction() - self.__DEG
        self.__game_ship.set_direction(new_direction)

    def __move_left(self):
        """this function change the degree of the ship head to the left """
        new_direction = self.__game_ship.get_direction() + self.__DEG
        self.__game_ship.set_direction(new_direction)

    def __move_up(self):
        """this function increases the speed of the ship """
        heading = math.radians(self.__game_ship.get_direction())
        self.__game_ship.set_x_speed(math.cos(heading))
        self.__game_ship.set_y_speed(math.sin(heading))
        self.__move_obj(self.__game_ship)

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def __check_asteroid_intersection(self):
        """the function checks and return True if the ship hits an asteroid"""
        for asteroid in self.__game_asteroids:
            if asteroid.has_intersection(self.__game_ship):
                self.__screen.unregister_asteroid(asteroid)
                self.__game_asteroids.remove(asteroid)
                return True
        return False

    def check_torpedo_hit_asteroid(self):
        """the function checks and return True if
         the torpedo hits an asteroid"""
        for torpedo in self.__game_torpedo:
            for asteroid in self.__game_asteroids:
                if asteroid.has_intersection(torpedo):
                    self.__add_score(asteroid)
                    self.__split_asteroid(asteroid, torpedo)
                    self.__screen.unregister_torpedo(torpedo)
                    self.__game_torpedo.remove(torpedo)
                    return True
        return False

    def __add_score(self, asteroid):
        """the function update the score of the player"""
        if asteroid.get_size() == self.__BIG_SIZE:
            self.__score += self.__LOW_SCORE
        if asteroid.get_size() == self.__MID_SIZE:
            self.__score += self.__MID_SCORE
        if asteroid.get_size() == self.__SMALL_SIZE:
            self.__score += self.__HIGH_SCORE

    def __get_new_asteroids(self, asteroid, torpedo):
        """this function return two asteroid after an asteroid is hit"""
        x_location, y_location = asteroid.get_location()
        size = asteroid.get_size()
        asteroid_speed_x = asteroid.get_x_speed()
        asteroid_speed_y = asteroid.get_y_speed()
        torpedo_speed_x = torpedo.get_x_speed()
        torpedo_speed_y = torpedo.get_x_speed()
        constant = (asteroid_speed_x ** 2 + asteroid_speed_y ** 2) ** 0.5
        new_speed_x = (torpedo_speed_x + asteroid_speed_x) / constant
        new_speed_y = (torpedo_speed_y + asteroid_speed_y) / constant

        asteroid1 = Asteroid(x_location, y_location, new_speed_x, new_speed_y,
                             size - 1)
        asteroid2 = Asteroid(x_location, y_location, -new_speed_x,
                             -new_speed_y, size - 1)
        return asteroid1, asteroid2

    def __split_asteroid(self, asteroid, torpedo):
        """this function manages the split and append of asteroid"""
        if asteroid.get_size() == 1:
            self.__screen.unregister_asteroid(asteroid)
            self.__game_asteroids.remove(asteroid)
        else:
            asteroid1, asteroid2 = self.__get_new_asteroids(asteroid, torpedo)
            self.__screen.unregister_asteroid(asteroid)
            self.__game_asteroids.remove(asteroid)
            self.__game_asteroids.append(asteroid1)
            self.__game_asteroids.append(asteroid2)
            self.__screen.register_asteroid(asteroid1, asteroid1.get_size())
            self.__screen.register_asteroid(asteroid2, asteroid2.get_size())

    def __delete_torpedo(self):
        """this function delete torpedo after 200 round of move"""
        for torpedo in self.__game_torpedo:
            if (torpedo.get_life_cycle() + self.__LIFE_CYCLE_TORPEDO) == \
                    self.__flag_loop:
                self.__screen.unregister_torpedo(torpedo)
                self.__game_torpedo.remove(torpedo)

    def __add_torpedo(self):
        """this function adds a torpedo to the game"""
        x_location, y_location = self.__game_ship.get_location()
        direction = self.__game_ship.get_direction()
        heading = math.radians(direction)
        x_speed = self.__game_ship.get_x_speed()
        y_speed = self.__game_ship.get_y_speed()
        torpedo_x_speed = x_speed + 2 * math.cos(heading)
        torpedo_y_speed = y_speed + 2 * math.sin(heading)
        torpedo = Torpedo(x_location, y_location, torpedo_x_speed,
                          torpedo_y_speed, direction, self.__flag_loop)
        if len(self.__game_torpedo) < self.__MAX_TORPEDO:
            self.__screen.register_torpedo(torpedo)
            self.__game_torpedo.append(torpedo)

    def __move_all_torpedo(self):
        """this function moves all the torpedoes in the game"""
        self.__flag_loop += 1
        for torpedo in self.__game_torpedo:
            self.__move_obj(torpedo)

    def __check_game_finish(self):
        """this function checks if the game is over"""
        if self.__life_ship == 0:
            self.__screen.show_message("finish game", "GAME OVER")
            self.__screen.end_game()
            sys.exit()

        if len(self.__game_asteroids) == 0:
            if self.__life_ship > 0:
                self.__screen.show_message("finish game", "WINNER")
                self.__screen.end_game()
                sys.exit()
            else:
                self.__screen.show_message("finish game", "GAME OVER")
                self.__screen.end_game()
                sys.exit()

        if self.__screen.should_end():
            self.__screen.show_message("press Q to Exit", "finish game ")
            self.__screen.end_game()
            sys.exit()

    def __where_to_move(self):
        """this function executes the commands from the player in the game"""
        if self.__screen.is_left_pressed():
            self.__move_left()
        if self.__screen.is_right_pressed():
            self.__move_right()
        if self.__screen.is_up_pressed():
            self.__move_up()
        if self.__screen.is_space_pressed():
            self.__add_torpedo()

    def _game_loop(self):
        """this function manages the complete game"""
        self.__where_to_move()
        self.__move_all_asteroids()
        self.__draw_all_asteroids()
        self.__move_obj(self.__game_ship)

        x, y = self.__game_ship.get_location()
        self.__screen.draw_ship(x, y, self.__game_ship.get_direction())
        if self.__check_asteroid_intersection():
            self.__life_ship -= 1
            self.__screen.show_message("you have crashed", "BOOM")
            self.__screen.remove_life()

        if self.__game_torpedo:
            self.__move_all_torpedo()
            self.__draw_all_torpedo()
            self.check_torpedo_hit_asteroid()
            self.__delete_torpedo()
        self.__screen.set_score(self.__score)
        self.__check_game_finish()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
