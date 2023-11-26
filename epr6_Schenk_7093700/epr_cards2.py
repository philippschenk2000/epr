""" This script contains 5 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"
import epr_cards1


def load_players() -> [str]:
    #players_together = input('Enter the names of the players (separated by comma): ').replace(' ', '')
    players_together = 'hans,jens,phil'
    players = players_together.split(',')
    if len(players) < 3 or len(players) > 4:
        print('Count of players should be 3 or 4.')
    else:
        return players


def initialize_variables(players) -> {str: int} and {str: list}:
    # DETERMINE THE GAME VARIABLES
    number_of_cards = 12
    colors = ['Kreuz', 'Herz', 'Karo']
    # CALL THE FUNCTIONS FOR THE EXERCISES a) - e)
    cards = epr_cards1.create_card_list(number_of_cards, colors)
    shuffled_cards = epr_cards1.shuffle_card_list(cards)
    handed_out_cards = epr_cards1.hand_out_cards(shuffled_cards, len(players), number_of_cards // len(players))
    players_cards_dict = {}
    score = {}

    for p in range(len(players)):
        player = players[p]
        cards_for_this_player = handed_out_cards[p]
        print(player, 'gets the following cards:', cards_for_this_player)
        players_cards_dict[player] = cards_for_this_player
        score[player] = 0
    return players_cards_dict, score

