""" This script is the start for the different functions for the new exercise """

__author__ = "7093700, Schenk"

import epr_cards2


def main():

    players = epr_cards2.load_players()
    player_cards, score = epr_cards2.initialize_variables(players)
    epr_cards2.play_game(players, score, player_cards)


main()


# TEST 1:
# IN: Philipp,Tim,Josef SHOULD: one or two winners (look at out)
# OUT: In the complete set there are 12 cards
#
# These are all the available cards:
# [(3, 'Herz'), (2, 'Herz'), (1, 'Kreuz'), (2, 'Karo'), (3, 'Kreuz'), (4, 'Karo'), (2, 'Kreuz'), (1, 'Karo'), (3, 'Karo'), (1, 'Herz'), (4, 'Herz'), (4, 'Kreuz')]
#
# Philipp gets the following cards: [(3, 'Herz'), (2, 'Herz'), (1, 'Kreuz'), (2, 'Karo')]
# Tim gets the following cards: [(3, 'Kreuz'), (4, 'Karo'), (2, 'Kreuz'), (1, 'Karo')]
# Josef gets the following cards: [(3, 'Karo'), (1, 'Herz'), (4, 'Herz'), (4, 'Kreuz')]
#
# Round 1:
# First player is Josef , so Karo is trump.
# First played card: (3, 'Karo')
# The cards from the others are: (2, 'Herz') (4, 'Karo')
# Herz Karo Karo
# second card won
# Winner of this round is: Philipp
# {'Philipp': 0, 'Tim': 1, 'Josef': 0}
#
# Round 2:
# First player is Josef , so Herz is trump.
# First played card: (1, 'Herz')
# The cards from the others are: (3, 'Herz') (2, 'Herz')
# Herz Herz Herz
# Winner of this round is: Josef
# {'Philipp': 0, 'Tim': 1, 'Josef': 1}
#
# Round 3:
# First player is Philipp , so Kreuz is trump.
# First played card: (1, 'Kreuz')
# The cards from the others are: (4, 'Herz') (3, 'Kreuz')
# Herz Kreuz Kreuz
# first card won
# Winner of this round is: Philipp
# {'Philipp': 0, 'Tim': 1, 'Josef': 2}
#
# Round 4:
# First player is Tim , so Karo is trump.
# First played card: (1, 'Karo')
# The cards from the others are: (3, 'Karo') (4, 'Karo')
# Karo Karo Karo
# Winner of this round is: Tim
# {'Philipp': 0, 'Tim': 2, 'Josef': 2}
# The Winner(s): Tim and Josef



# Test 2:
# IN: 42 SHOULD: look at out
# OUT: In the complete set there are 12 cards
#
# These are all the available cards:
# [(3, 'Herz'), (3, 'Kreuz'), (4, 'Kreuz'), (1, 'Karo'), (4, 'Herz'), (4, 'Karo'), (2, 'Kreuz'), (1, 'Kreuz'), (2, 'Karo'), (3, 'Karo'), (2, 'Herz'), (1, 'Herz')]
#
# Philipp gets the following cards: [(3, 'Herz'), (3, 'Kreuz'), (4, 'Kreuz'), (1, 'Karo')]
# Tim gets the following cards: [(4, 'Herz'), (4, 'Karo'), (2, 'Kreuz'), (1, 'Kreuz')]
# Josef gets the following cards: [(2, 'Karo'), (3, 'Karo'), (2, 'Herz'), (1, 'Herz')]
#
# Round 1:
# First player is Tim , so Herz is trump.
# First played card: (4, 'Herz')
# The cards from the others are: (2, 'Herz') (3, 'Herz')
# Herz Herz Herz
# Winner of this round is: Tim
# {'Philipp': 0, 'Tim': 1, 'Josef': 0}
#
# Round 2:
# First player is Philipp , so Kreuz is trump.
# First played card: (3, 'Kreuz')
# The cards from the others are: (3, 'Herz') (1, 'Kreuz')
# Herz Kreuz Kreuz
# first card won
# Winner of this round is: Philipp
# {'Philipp': 0, 'Tim': 1, 'Josef': 1}
#
# Round 3:
# First player is Josef , so Herz is trump.
# First played card: (2, 'Herz')
# The cards from the others are: (4, 'Herz') (1, 'Karo')
# Herz Karo Herz
# first card won
# Winner of this round is: Josef
# {'Philipp': 0, 'Tim': 2, 'Josef': 1}
#
# Round 4:
# First player is Philipp , so Karo is trump.
# First played card: (1, 'Karo')
# The cards from the others are: (1, 'Herz') (4, 'Karo')
# Herz Karo Karo
# second card won
# Winner of this round is: Josef
# {'Philipp': 0, 'Tim': 3, 'Josef': 1}
# The Winner(s): Tim



# Test 3:
# IN: Philipp,Tim,Josef,Tobias SHOULD: have 4 players but still work
# OUT: In the complete set there are 12 cards
#
# These are all the available cards:
# [(4, 'Karo'), (2, 'Karo'), (4, 'Herz'), (2, 'Kreuz'), (4, 'Kreuz'), (1, 'Herz'), (1, 'Kreuz'), (3, 'Herz'), (2, 'Herz'), (3, 'Karo'), (3, 'Kreuz'), (1, 'Karo')]
#
# Philipp gets the following cards: [(4, 'Karo'), (2, 'Karo'), (4, 'Herz')]
# Tim gets the following cards: [(2, 'Kreuz'), (4, 'Kreuz'), (1, 'Herz')]
# Josef gets the following cards: [(1, 'Kreuz'), (3, 'Herz'), (2, 'Herz')]
# Tobias gets the following cards: [(3, 'Karo'), (3, 'Kreuz'), (1, 'Karo')]
#
# Round 1:
# First player is Philipp , so Karo is trump.
# First played card: (4, 'Karo')
# The cards from the others are: (4, 'Karo') (2, 'Kreuz')
# Karo Kreuz Karo
# first card won
# Winner of this round is: Philipp
# {'Philipp': 0, 'Tim': 0, 'Josef': 0, 'Tobias': 1}
#
# Round 2:
# First player is Philipp , so Karo is trump.
# First played card: (2, 'Karo')
# The cards from the others are: (4, 'Karo') (1, 'Karo')
# Karo Karo Karo
# Winner of this round is: Philipp
# {'Philipp': 1, 'Tim': 0, 'Josef': 0, 'Tobias': 1}
#
# Round 3:
# First player is Tim , so Herz is trump.
# First played card: (1, 'Herz')
# The cards from the others are: (1, 'Kreuz') (1, 'Karo')
# Kreuz Karo Herz
# second card won
# Winner of this round is: Josef
# {'Philipp': 1, 'Tim': 0, 'Josef': 0, 'Tobias': 2}
# The Winner(s): Tobias
