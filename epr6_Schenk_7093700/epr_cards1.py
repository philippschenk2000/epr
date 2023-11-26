""" This script contains 5 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"
import random


def create_card_list(number_of_cards, colors) -> [(int, str)]:
    """ This function creates a list full of tuples containing a card color and a card value.

    """
    # DIRECTLY MAKES THE VALUES DEPENDENT ON THE NUMBER OF COLORS
    values = [i for i in range(1, number_of_cards // len(colors) + 1)]
    # CREATE A LIST FULL OF TUPLES
    cards = [(i, j) for i in values for j in colors]
    print('In the complete set there are', len(cards), 'cards\n')
    return cards


def shuffle_card_list(cards) -> [(int, str)]:
    """ This function shuffles the card list from the first function.

    """
    # JUST MIXING THE CARDS
    random.shuffle(cards)
    print('These are all the available cards:')
    print(cards, '\n')
    return cards


def compare_two_cards(card_one, card_two) -> int:
    """ This function compares the first 2 cards from the shuffled list based on their value.

    """
    card_one_value = card_one[0]
    card_two_value = card_two[0]
    print(card_one_value, card_two_value)
    # COMPARE NOT THE COLOR BUT THE VALUE OF THE FIRST 2 CARDS
    if card_one_value < card_two_value:
        return 0
    elif card_one_value == card_two_value:
        return 1
    else:
        return 2


def compare_two_cards_trump(card_one, card_two, trump) -> int:
    """ This function compares the first 2 cards from the shuffled list based on their value ands the trump.

    """
    card_one_value = card_one[0]
    card_two_value = card_two[0]
    card_one_color = card_one[1]
    card_two_color = card_two[1]
    print(card_one_color, card_two_color, trump)
    # NOW COMPARES NOT JUST THE COLOR BUT ALSO THE VALUE OF THE FIRST 2 CARDS
    if card_one_color == card_two_color == trump:
        return 1
    elif card_one_color == trump or card_one_value > card_two_value:
        print('first card won')
        return 2
    else:
        print('second card won')
        return 0


def hand_out_cards(list_cards, players, number_of_cards) -> [(int, str)]:
    """ This function hands out an even number of shuffled cards to each player.

    """
    # SAME NUMBER OF CARDS TO EACH OF THE PLAYERS: 32 cards, 4 players --> 8 cards each
    big_list = [list_cards[p*number_of_cards:(p + 1)*number_of_cards] for p in range(players)]
    return big_list
