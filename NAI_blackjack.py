# Authors: Hubert Korzeniewski, Adrian Szostak
# This program uses the easyAI library
# Instructions for downloading the library: https://zulko.github.io/easyAI/installation.html

import random

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax


class GameBlackJack(TwoPlayerGame):
    '''
    A class to represent a game Blackjack with using AI

    Attributes
    -----------------
    players : list
        list of players [Human_Player, AI_Player]
    cards_value_player : int
        starting total after the deal to the first player
    cards_value_player_2 : int
        starting total after the deal to the second player
    current_player : int
        declaration of which player started the game
    finish_player_1 : bool
        player 1 has ended the game (lost or won)
    finish_player_2 : bool
        player 1 has ended the game (lost or won)
    '''


    def __init__(self, players):
        '''
        Constructs all the necessary attributes for the GameBlackJack object and initialization of the game.
        
        Parameters
        ----------
        players : list
            list of players [Human_Player, AI_Player]
        cards_value_player : int
            starting total after the deal to the first player
        cards_value_player_2 : int
            starting total after the deal to the second player
        current_player : int
            declaration of which player started the game
            returns the current player to whom the move belongs
        finish_player_1 : bool
            player 1 has ended the game (lost or won)
        finish_player_2 : bool
            player 1 has ended the game (lost or won)
        '''
        
        self.players = players
        self.cards_value_player = random.randint(1, 11)   # start with 2 random cards
        self.cards_value_player_2 = random.randint(1, 11)  # start with 2 random cards
        self.current_player = 2  # AI starts
        self.finish_player_1 = False
        self.finish_player_2 = False


    def possible_moves(self):
        '''
        Return all posible moves

        Returns
        -------
        list
            1 or 2.
                1 - hit card
                2 - stop taking card
        '''
        
        if self.current_player == 1 and self.finish_player_1:
            return [2]
        elif self.current_player == 2 and self.finish_player_2:
            return [2]
        else:
            return [1, 2]



    def make_move(self, move):
        '''
        Transforms the game according to the move.

        Parameters
        ----------
        move : int
            Move can be 1 or 2.
            1 - take card and add to your card value
            2 - stop taking card for the rest of a game
        '''
        
        if self.current_player == 1 and not self.finish_player_1:
            if move == 1:
                self.cards_value_player += random.randint(1, 11)  # add radnom card.
            else:
                self.finish_player_1 = True
        if self.current_player == 2 and not self.finish_player_2:
            if move == 1:
                self.cards_value_player_2 += random.randint(1, 11)  # add radnom card.
            else:
                self.finish_player_2 = True



    def is_over(self):
        '''
        The function checks if the game is over

        Returns
        -------
        Bool
            Game is over when someone has more than 21 card value or both players stop taking cards
        '''
        
        return (self.finish_player_1 and self.finish_player_2) or (
                self.cards_value_player > 21 or self.cards_value_player_2 >= 21)



    def show(self):
        '''
        Show communicate before play
        '''
        
        print(str(self.cards_value_player) + " cards value in your hand, and " + str(
            self.cards_value_player_2) + " value in ai hand. Press 1 to hit or 2 to stay")


    def scoring(self):
        '''
        Gives a score to the current game. Help ai to make correct play

        Returns
        -------
        int
            adds or subtracts points

        '''
        if self.current_player == 2:
            if (self.cards_value_player_2 > self.cards_value_player) and self.finish_player_1:
                return 21
            elif self.cards_value_player_2 > 21 or self.cards_value_player_2 < 11:
                return -20
            elif self.cards_value_player_2 < self.cards_value_player:
                return -20
            else:
                return self.cards_value_player_2

        if self.current_player == 1:
            if self.cards_value_player > 21 or self.cards_value_player < 11:
                return -20
            elif (self.cards_value_player > self.cards_value_player_2) and self.finish_player_2:
                return 20
            elif self.cards_value_player < self.cards_value_player_2:
                return -20
            else:
                return self.cards_value_player


ai = Negamax(10)
'''
The Negamax algorithm always looks for the shortest path to victory, or the longest path to defeat
'''
game = GameBlackJack([Human_Player(), AI_Player(ai)])
history = game.play()
