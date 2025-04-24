!/usr/bin/python

""" 
Version 0.1

Written by Ktopham

This is a simple Object Oriented Magic the Gathering life counter.

Pre-requisites:
Python3
termcolor

"""

import sys
from termcolor import colored

player_list = []

class Player:
    """Initializes a player with a name and life total."""
    def __init__(self, name):
        """Initializes self for the class."""
        self.life = 20
        self.name = name

    def add_life(self, y):
        """Adds a given value to a player's life total."""
        print("Player " + self.name + colored(" gained life!", "blue"))
        result = self.life + y
        self.life = result
        return self.life

    def sub_life(self, y):
        """Subtracts a given value from a player's life total."""
        print("Player " + self.name + colored(" took damage!", "red"))
        result = y + self.life # Required plus or it will become a double negative/becomes positive
        self.life = result
        return self.life

def life_change(player, amount):
    """Calls the functions that modify life totals."""
    if amount > 0:
        player.add_life(amount)
    elif amount < 0:
        player.sub_life(amount)
    else:
        print("Input a correct value: ")

def player_count(quantity):
    """Sets the player count."""
    init_number = 0
    if quantity > 8:
        print("Too many players!")
        sys.exit()
    for _ in range(0, quantity):
        player_name = str(input("Player's name?: "))
        player_name = Player(player_name)
        player_list.append(player_name)
        init_number += 1
    return player_list

def game_check(player_total_list):
    """Checks if the game is over."""
    alive_list = []
    for each in player_total_list:
        if each.life > 0:
            alive_list.append(each)
    if len(alive_list) > 1:
        return False
    print("Game over!")
    print("Final life totals: ")
    get_life(player_total_list)
    for each in alive_list:
        print(each.name + " wins!")
    return True

def get_life(player_life_list):
    """Prints life totals."""
    for obj in player_life_list:
        print(obj.name, obj.life)

def game_start():
    """Creates the game with two players."""
    quantity = int(input("How many players?: "))
    check = game_check(player_count(quantity))
    while check is False:
        try:
            get_life(player_list)
            player_x = input("Which players life is changing? ")
            amount = int(input("How much life? "))
            for each in player_list:
                if each.name == player_x:
                    life_change(each, amount)
        except ValueError:
            print("No good value given")
        except KeyboardInterrupt:
            sys.exit()
        check = game_check(player_list)

if __name__ == "__main__":
    game_start()
