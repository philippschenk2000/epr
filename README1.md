# epr1
Aufgabe ÜE-00-1

Berechnung von Harmonischem und arithmetischem Mittel von zwei Zahlen in python=3.0 oder neuer


Ein- und Ausgabeformat:
------------------------------

Ein: 2 Zahlen, da aber auch mit nachkommazahlen umgegangen werden möchte, wird der Input mittels float entgegen genommen.
Aus: Da Antwortsätze ausgegeben werden sollen in beiden Fällen, gebe ich es in diesem Fall als ein f-string aus, sodass nur eine variable pro print-funktion ausgegebne wird.

Entwurfsmuster:
------------------------------

Ich werde auch in Zukunft nach einem ähnlichen Muster vorgehen, nämlich dass die Überfunktion "def main" regelmäßig weitere Funktionen aufruft und somit als "oberste Funktion" gilt. 
Aus Gründen der Übersichtlichkeit füge ich mehrere ähnliche Aufgaben dann zu kleinen Unterfunktionen zusammen, sodass diese von "def main" aus gesteuert werden.

Code: siehe epr1.py
------------------------------

Test1:
In: -4.2, mmed3
Out: Input has to be a float or integer.

Test2:
In: 4, 71
Out: 7.573333333333333, 37.5

Test3:
In: 5769.6749, 63748.0
Out: 10581.632255517223, 34758.83745

Beschreibung des Programms:
------------------------------

Nach Input der Werte in der Konsole sichert das Programm die Funktion und den User wissend durch die try-except funktion ab.
Nach erfolgreicher float oder integer-entsprechenden Zahlen springt das Programm zur Berechnung des harmonischen und arithmetischen Mittels, welche abgespeichert und daraufhin in die letzte Funktion zum Output in der Konsole weitergegeben werden.
Mittels f-string werden beide berechneten Werte ungerundet ausgegeben.