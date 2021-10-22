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
    # THE PLANNING PHASE

    def __init__(self, players):
        self.players = players
        self.cards_value_player = random.randint(1, 11) + random.randint(1, 11)  # start with 2 random cards
        self.cards_value_player_2 = random.randint(1, 11) + random.randint(1, 11)  # start with 2 random cards
        self.current_player = 1  # player 1 starts
        self.nplayer = 1  # player 1 starts
        self.finish_player_1 = False
        self.finish_player_2 = False
        print(type(players))

    def possible_moves(self):
        return [1, 2]

    def make_move(self, move):
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
        return (self.finish_player_1 and self.finish_player_2) or (self.cards_value_player > 21 or self.cards_value_player_2 > 21)

    def show(self):
        print( str(self.cards_value_player) + " cards value in your hand, and " + str(self.cards_value_player_2) + " value in ai hand. Press 1 to hit or 2 to stay")

    def scoring(self):
        if self.cards_value_player_2 == 21:
            return 100
        elif self.cards_value_player_2 == 20:
            return 90
        elif self.cards_value_player_2 == 19:
            return 80
        elif self.cards_value_player_2 == 18:
            return 80
        elif self.cards_value_player_2 == 17:
            return 70
        elif self.cards_value_player_2 == 16:
            return 60
        elif self.cards_value_player_2 == 15:
            return 50
        elif self.cards_value_player_2 == 14:
            return 40
        elif self.cards_value_player_2 == 13:
            return 30
        elif self.cards_value_player_2 == 12:
            return 20
        elif self.cards_value_player_2 == 11:
            return 10
        else:
            return 0


ai = Negamax(11, win_score=70)
game = GameBlackJack([Human_Player(), AI_Player(ai)])
history = game.play()