# epr6 Aufgabe -- ANALYSE
Programmierung eines Kartenspiels in python==3.0 oder neuer

Ein- und Ausgabeformat:
------------------------------
Ein: 3 bis 4 Spielernamen, getrennt durch Kommas
Aus: Spielzwischenstände und Sieger

Annahmen:
------------------------------
Gespielt wird mit 3 – 4 Spielern. Jeder Spieler spielt reihum genau eine Karte aus der Hand aus. Diese Karten bilden den Stich. In einem Spiel
werden so viele Stiche gespielt, wie Spieler Handkarten besitzen. Der beginnende Spieler kann jede Karte aus
der Hand abspielen. Die Farbe der ersten ausgespielten Karte in einem Stich ist Trumpf und muss ‚bedient‘
werden. Das heißt, hat ein Spieler die Farbe der erstgelegten Karte auf der Hand, muss er diese spielen. Kann
ein Spieler die Trumpffarbe nicht spielen, darf dieser Spieler eine andere Farbe spielen. Am Anfang jedes Stichs
wird die Trumpffarbe neu bestimmt. Die Karte mit dem höchsten Wert der Trumpffarbe gewinnt und der
Spieler, der diese Karte ausgespielt hat, bekommt alle Karten des Stichs. Karten, die eine andere Farbe als die
Trumpffarbe haben, können einen Stich nie gewinnen. Nach jedem Stich werden die Stichkarten ausgewertet
und die Strafpunkte der Spieler aufaddiert. Jede Kreuz-Karte ergibt einen Strafpunkt. Es gibt drei verschiedene Farben 
(Karo, Herz, und Kreuz). Die jeweils höchste Karte einer Farbe ist die 4, die
niedrigste eine 1. Zu Beginn des Spiels werden alle Karten vollständig an die Spieler verteilt.

Entwurfsmuster:
------------------------------
Ich werde auch in Zukunft nach einem ähnlichen Muster vorgehen, nämlich dass die Überfunktion "def main" regelmäßig weitere Funktionen aufruft und somit als "oberste Funktion" gilt. 
Aus Gründen der Übersichtlichkeit füge ich mehrere ähnliche Aufgaben dann zu kleinen Unterfunktionen zusammen, sodass diese von "def main" aus gesteuert werden.


# epr6 Aufgabe -- TESTS
Code: siehe epr3_exc2_Schenk_7093700.py
------------------------------

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

# epr6 Aufgabe -- DOKUMENTATION
Beschreibung des Programms:
------------------------------
Das vorliegende Python-Skript beschreibt ein Kartenspiel, das aus mehreren Funktionen besteht, welche jeweils einen spezifischen Teil des Spielablaufs abdecken. 
Zunächst müssen die Spieler ihre Namen einzugeben, die dann in einer Liste gespeichert werden. Die Namen müssen durch Kommas getrennt eingegeben werden, und das Spiel erfordert zwischen drei und vier Spielern.
Danach werden Karten erstellt, gemischt und an die Spieler verteilt.
Danach wird ein dictionary erstellt, das die Karten jedes Spielers sowie einen Punktestand für jeden Spieler enthält.
Die Kernfunktion des Spiels ist play_game(players, score, player_cards), die den Spielablauf steuert. In jeder Runde wird ein Trumpf bestimmt, und die Spieler legen ihre Karten aus.
dabei wird der Gewinner jeder Runde bestimmt, woraufhin der Punktestand aktualisiert wird.
Zur Aktualisierung des Punktestands dient die Funktion update_score(card_played, score, rest_players, playing_order). Sie erhält Informationen über die gespielte Karte und den Rundengewinner und passt dementsprechend den Punktestand an.
Schließlich wird der oder die Gewinner des Spiels, basierend auf den gesammelten Punkten, ermittelt.
