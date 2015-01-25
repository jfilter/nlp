a)
[A='Fnord']

b)
1. Waehle eine Feature-Struktur aus und erstelle eine Kopie K. Die andere Struktur wird im weiteren Y genannt.
2. Iteriere via Tiefensuche ueber die Knoten in Y. Fuer einen Knoten N:
	2.1 Wenn das Feature nicht vorhanden ist: Fuege N zu K hinzu (mit dem Wert) (und allen uebergeornden Knoten)
	2.2 Es ist in K vorhanden:
		2.2.1 In K: Mit einer Variable belegt:
			2.2.1.1. N ist auch eine Variable: Ersetzte in Y die Variable mit der aus K
			2.2.1.2. N ist eine atomar Wert: Erste alle Vorkommen der Variable mit dem Wert von N.
		2.2.2 In K: Es ist ein spezifiziert:
			2.2.2.1. N ist auch eine Variable: Ersetzte in Y die Variable mit dem Wert.
			2.2.2.2. N ist eine atomar Wert:
				2.2.2.2.1. Wenn sie gleich sind: Mache nichts
				2.2.2.2.2. Wenn nicht: Widerspruch! Es kan keine Unification geben.		
3. K ist die Vereinigung.