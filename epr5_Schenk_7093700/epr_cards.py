""" This script contains 3 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"
import random


def create_card_list(number_of_cards) -> [(int, str)]:
    colors = ['Pik', 'Kreuz', 'Herz', 'Karo']
    values = [i for i in range(1, number_of_cards // len(colors) + 1)]
    cards = [(i, j) for i in values for j in colors]
    #print(cards)
    print(len(cards))
    return cards


def shuffle_card_list(cards) -> [(int, str)]:
    random.shuffle(cards)
    print(cards)
    return cards


def compare_two_cards(card_one, card_two) -> int:
    card_one_value = card_one[0]
    card_two_value = card_two[0]
    print(card_one_value, card_two_value)
    if card_one_value < card_two_value:
        return 0
    elif card_one_value == card_two_value:
        return 1
    else:
        return 2


def compare_two_cards_trump(card_one, card_two, trump) -> int:
    card_one_value = card_one[0]
    card_two_value = card_two[0]
    print(card_one_value, card_two_value, trump)
    if card_one_value < card_two_value:
        return 0
    elif card_one_value == card_two_value:
        return 1
    else:
        return 2


if __name__ == '__main__':
    cards = create_card_list(32)
    shuffled_cards = shuffle_card_list(cards)
    comparison = compare_two_cards(shuffled_cards[0], shuffled_cards[1])
    compare_two_cards_trump(shuffled_cards[0], shuffled_cards[1], 'Pik')