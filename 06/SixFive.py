"""
Die Schwierigkeiten lagen daran die Struktur der deutschen Zahlen zu verstehen.
Zudem gibt es auch hier einige Ausnahmen. z.B. bei "eine Million" oder "ein hundert" <-> "einz
Mit der Hilfe meines Ansatzen ist es aber sehr einfach weitere Zahlen hinzufügen.
"""

import nltk
 	
grammar1 = nltk.CFG.fromstring("""
S -> NULL | Number_9

Number_9 -> EINTO10 'hundert' NOTHING_1TO100 'millionen' NOTHING_Number_6 | Number_8
Number_8 -> 11TO100 'millionen' NOTHING_Number_6 | Number_7
Number_7 -> 2TO10 'millionen' NOTHING_Number_6 | Number_6 | 'eine' 'million' NOTHING_Number_6

NOTHING_Number_6 -> Number_6 |

Number_6 -> EINTO10 'hundert' NOTHING_1TO100 'tausend' NOTHING_Number_3 | Number_5
Number_5 -> 11TO100 'tausend' NOTHING_Number_3 | Number_4
Number_4 -> EINTO10 'tausend' NOTHING_Number_3 | Number_3

NOTHING_Number_3 -> Number_3 | 

Number_3 -> EINTO10 'hundert' Number_2 | Number_2
Number_2 -> 11TO100 | Number_1
Number_1 -> 1TO10

NULL -> 'null'
EINTO10 -> 'ein' | 2TO10
1TO10 -> 'eins' | 2TO10
2TO10 -> 'zwei' | 'drei' | 'vier' | 'fünf' | 'sechs' | 'sieben' | 'acht' | 'neun'

11TO100 -> EINTO10 'und' 20TO90 | 11TO20 | 20TO90
11TO20 -> 'zehn'| 'elf' | 'zwölf' | 'dreizehn' | 'vierzehn' | 'fünfzehn' | 'sechzehn' | 'siebzehn' | 'achtzehn' | 'neunzehn'
20TO90 -> 'zwanzig' | 'dreißig' | 'vierzig' | 'fünfzig' | 'sechzig' | 'siebzig' | 'achtzig' | 'neunzig'

NOTHING_1TO100 -> EINTO10 | 11TO100 |

""")

text =  ["eine million", "acht hundert ein und dreißig millionen fünf hundert zwölf tausend ein hundert elf", "eine million dreißig", "neun und achtzig millionen drei hundert ein und zwanzig", "acht millionen", "sieben hundert ein tausend fünf" ,"drei tausend zwei hundert vier und zwanzig", "vierzig tausend sieben", "null", "drei und zwanzig", "vier hundert eins", "neun und neunzig tausend ein hundert dreizehn"]

counter = 0
for t in text:
	failed = True
	trees = nltk.ChartParser(grammar1).parse(t.split())
	for tree in trees:
		failed = False
		# print(tree)
	if failed:
		print(t)
	else:
		counter += 1

print('%s Procent Successful' % (counter / len(text) * 100))
# 100.0 Procent Successful