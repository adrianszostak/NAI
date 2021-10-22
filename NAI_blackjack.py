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
        self.finish_player_1 = False
        self.finish_player_2 = False

    '''
    return all posible moves
    1 - hit card
    2 - stop taking card
    '''
    def possible_moves(self):
        return [1, 2]

    '''
    make move
    1 - take card and add to your card value
    2 - stop taking card for the rest of a game
    '''
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
    '''
    game is over when someone has more than 21 card value or both players stop taking cards
    '''
    def is_over(self):
        return (self.finish_player_1 and self.finish_player_2) or (
                    self.cards_value_player > 21 or self.cards_value_player_2 > 21)
    '''
    show communicate after before play
    '''
    def show(self):
        print(str(self.cards_value_player) + " cards value in your hand, and " + str(
            self.cards_value_player_2) + " value in ai hand. Press 1 to hit or 2 to stay")
    '''
    help ai to make correct decision
    '''
    def scoring(self):
        if self.current_player == 2:
            if self.cards_value_player_2 > 21:
                return -100
            else:
                return self.cards_value_player_2

        if self.current_player == 1:
            if self.cards_value_player > 21:
                return -100
            else:
                return self.cards_value_player


ai = Negamax(4)
game = GameBlackJack([Human_Player(), AI_Player(ai)])
history = game.play()