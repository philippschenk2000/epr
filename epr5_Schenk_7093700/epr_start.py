""" This script is the start for the different functions for the new exercise """

__author__ = "7093700, Schenk"
import epr_cards


def main():

    # DETERMINE THE GAME VARIABLES
    number_of_cards = 32
    players = 4
    trump = 'Pik'
    # CALL THE FUNCTIONS FOR THE EXERCISES a) - e)
    cards = epr_cards.create_card_list(number_of_cards)
    shuffled_cards = epr_cards.shuffle_card_list(cards)
    epr_cards.compare_two_cards(shuffled_cards[0], shuffled_cards[1])
    print(epr_cards.compare_two_cards_trump(shuffled_cards[0], shuffled_cards[1], trump))
    print(epr_cards.hand_out_cards(shuffled_cards, players, number_of_cards // players))


main()
