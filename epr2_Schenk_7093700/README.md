# epr2 Aufgabe 2
Aufgabe ÜE-01

Berechnung von Harmonischem und arithmetischem Mittel von zwei Zahlen in python=3.0 oder neuer

Ein- und Ausgabeformat:
------------------------------

Ein: 3 Integer-Zahlen, die ersten beiden zwischen 0 & 110.
Aus: Da Antwortsätze ausgegeben werden sollen in beiden Fällen, gebe ich es in diesem Fall als ein f-string aus, sodass dabei die entstehenden Bonus Punkte für die Klausur ausgegeben werden.

Annahmen:
------------------------------

So wie programmiert: keine, der Nutzer wird auf alle möglichen Fehler hingewiesen.

Entwurfsmuster:
------------------------------

Ich werde auch in Zukunft nach einem ähnlichen Muster vorgehen, nämlich dass die Überfunktion "def main" regelmäßig weitere Funktionen aufruft und somit als "oberste Funktion" gilt. 
Aus Gründen der Übersichtlichkeit füge ich mehrere ähnliche Aufgaben dann zu kleinen Unterfunktionen zusammen, sodass diese von "def main" aus gesteuert werden.

Code: siehe epr1.py
------------------------------

Test1:
In: 90, 40, 50
Out: The bonus points for the input would be 9.29 points

Test2:
In: -10, 40, 10
Out: First number and second number have to be between 0 and 110

Test3:
In: 0, 106.9
Out: All input has to be integer.

Test4: 
In 110, 110, 50
Out: The bonus points for the input would be 12.5 points

Beschreibung des Programms:
------------------------------

Nach Input der Werte in der Konsole sichert das Programm die Funktion und den User wissend durch die try-except funktion ab, sodass nur integer-Werte in die folgenden Berechnungen aufgenommen werden.
Nach erfolgreicher integer-entsprechenden Zahlen springt das Programm zur Berechnung der maximalen Range (0 - 110) für die ersten beiden Werte uns informiert den Nutzer erneut bei falschen Angaben.
Bei richtiger Angabe der Werte erfolgt die Berechnung der zum Bestehen notwendigen Punkten (ZBNP).
Mittels f-string wird der errechnete Wert (ZBNP) gerundet auf 2 Nachkommastellen wie in einem angegebenem Beispiel ausgegeben.
https://github.com/philippschenk2000/epr/tree/main/epr2_Schenk_7093700