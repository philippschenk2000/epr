""" This script contains 5 different functions for the new exercise in epr """

__author__ = "7093700, Schenk"

import random

import epr_cards1


def load_players() -> [str]:
    """ This function creates a list of players for the following game.

    """
    players_together = input('Enter the names of the players (separated by comma): ').replace(' ', '')
    #players_together = 'hans,jens,phil'
    players = players_together.split(',')
    if len(players) < 3 or len(players) > 4:
        print('Count of players should be 3 or 4.')
    else:
        return players


def initialize_variables(players) -> {str: int} and {str: list}:
    """ This function creates a dictionary full of shuffled cards for every player of the game.

    """
    # DETERMINE THE GAME VARIABLES
    number_of_cards = 12
    colors = ['Kreuz', 'Herz', 'Karo']
    # CALL THE FUNCTIONS FOR THE EXERCISES a) - e) OF THE OLD EXERCISE
    cards = epr_cards1.create_card_list(number_of_cards, colors)
    shuffled_cards = epr_cards1.shuffle_card_list(cards)
    handed_out_cards = epr_cards1.hand_out_cards(shuffled_cards, len(players), number_of_cards // len(players))
    players_cards_dict = {}
    score = {}

    # HAND OUT CARDS TO EVERY PLAYER OF THE GAME AND SET EVERY SCORE TO ZERO
    for p in range(len(players)):
        player = players[p]
        cards_for_this_player = handed_out_cards[p]
        print(player.title(), 'gets the following cards:', cards_for_this_player)
        players_cards_dict[player] = cards_for_this_player
        score[player] = 0
    return players_cards_dict, score


def play_game(players, score, player_cards) -> {str: int}:
    """ This function plays the game with selecting for each round a trump and plays this card against the other cards of the other players.
    Also, the score and the winner gets updated at the end of the function.

    """

    # EACH ROUND (OF THE COUNT OF CARDS / COUNT OF PLAYERS) GETS PLAYED
    for rounding in range(len(list(player_cards[players[0]]))):
        playing_order = players.copy()
        random.shuffle(playing_order)
        # THE TRUMP OF EACH ROUND GETS SELECTED BY THE FIRST PLAYER
        trump = [player_cards[player][rounding][1] for player in playing_order][0]
        print(f'\nRound {rounding + 1}:\nFirst player is', playing_order[0].title(), ', so', trump, 'is trump.')
        print('First played card:', player_cards[playing_order[0]][rounding])
        rest_players = [p for p in playing_order if p != playing_order[0]]
        card_one = ''
        card_two = ''
        # THE OTHER CARDS WILL BE SELECTED (NOT THE CARD OF THE FIRST PLAYER)
        for p in range(0, len(rest_players)):
            player = players[p]
            if trump in player_cards[player][1]:
                if p == 0:
                    card_one = player_cards[player][p]
                elif p == 1:
                    card_two = player_cards[player][p]
        if card_one == '':
            card_one = random.choice(player_cards[rest_players[0]])
        if card_two == '':
            card_two = random.choice(player_cards[rest_players[1]])
        print('The cards from the others are:', card_one, card_two)
        # THE WINNER OF ALL CARDS WILL BE SELECTED
        card_played = epr_cards1.get_winner(card_one, card_two, trump)
        # THE SCORE GETS UPDATED IN ANOTHER FUNCTION
        score = update_score(card_played, score, rest_players, playing_order)
        print(score)

    # PRINT OUT THE WINNER AT THE END
    determine_winner(score)
    return score


def update_score(card_played, score, rest_players, playing_order) -> {str: int}:
    """ This function only updates the score and gets called by the play_game function.

    """
    if card_played == 1:
        score[str(playing_order[0])] = score[str(playing_order[0])] + 1
        print('Winner of this round is:', playing_order[0])
    elif card_played == 0:
        score[str(rest_players[1])] = score[str(rest_players[1])] + 1
        print('Winner of this round is:', playing_order[1])
    elif card_played == 2:
        score[str(rest_players[0])] = score[str(rest_players[0])] + 1
        print('Winner of this round is:', playing_order[0])
    return score


def determine_winner(scores) -> list:
    """ This function only determines the winner by looking at the scores-dictionary.

    """
    max_keys = [key for key, value in scores.items() if value == max(scores.values())]
    print('The Winner(s):', str(max_keys).replace("['", '').replace("']", '').replace("', '", ' and '))
    return max_keys
