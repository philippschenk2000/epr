""" This script is the start for the different functions for the new exercise """

__author__ = "7093700, Schenk"

import epr_cards2


def main():

    players = epr_cards2.load_players()
    player_cards, score = epr_cards2.initialize_variables(players)
    epr_cards2.play_game(players, score, player_cards)



main()
