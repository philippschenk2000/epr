""" This script contains the chatgpt exercise in epr """

__author__ = "7093700, Schenk 8017459, Ratnakumar"


def is_happy(s):
    """Überprüft, ob ein String 'happy' ist."""
    if len(s) % 2 != 0:  # Die Länge des Strings muss gerade sein
        return False
    mid = len(s) // 2
    #print(s[mid:])
    return s[:mid] == s[mid:]

def count_happy_substrings(S, l, r):
    """Rekursive Funktion zum Zählen der 'happy' Substrings."""
    if l > r:
        return 0
    count = 0
    if is_happy(S[l:r+1]):
        print(is_happy(S[l:r+1]))
        count += 1
    # Rekursive Aufrufe für die nächsten Substrings
    count += count_happy_substrings(S, l + 1, r)
    count += count_happy_substrings(S, l, r - 1)
    count -= count_happy_substrings(S, l + 1, r - 1)  # Vermeidung von Doppelzählung
    return count

def main():
    """Hauptfunktion zum Testen der Funktionalität."""
    S = '20230322'
    # -1, da die Indizes bei 0 beginnen, aber in der Aufgabe von 1 an gezählt wird
    result = count_happy_substrings(S, 0, len(S))
    print(f"Anzahl der 'happy' Substrings: {result}")


if __name__ == "__main__":
    main()

