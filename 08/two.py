# 1.
# http://en.wikipedia.org/wiki/Mass_noun
# Water is not countable. Check for determiner if noun is countable

# 2.
# A noun alone is not countable. When it's not countable you cannot use V[TENSE=pres, NUM=sg]
# Check for that case
# See in Line 16: ?x only when used without determiner.

import nltk

g = nltk.grammar.FeatureGrammar.fromstring("""

S -> NP[NUM=?n, CNT=?x] VP[NUM=?n, CNT=?x]

NP[NUM=?n, CNT=?x] -> N[NUM=?n, CNT=?x] | PropN[NUM=?n] | Det[NUM=?n, CNT=?c] N[NUM=?n, CNT=?c]
NP[NUM=pl] -> N[NUM=pl] 

VP[TENSE=?t, NUM=?n, CNT=?x] -> IV[TENSE=?t, NUM=?n, CNT=?x] | TV[TENSE=?t, NUM=?n] NP | IS ADJ

ADJ -> 'gone' | 'precious'
IS -> 'is' | 'was'

Det[NUM=sg] -> 'this'
Det[Num=sg, +CNT] -> 'every'
Det[NUM=pl] -> 'these' | 'all'
Det -> 'the' | 'some' | 'several'

PropN[NUM=sg] -> 'Kim' | 'Jody'

N[NUM=sg, -CNT] -> 'dog' | 'girl' | 'car' | 'child' | 'boy'
N[NUM=pl] -> 'dogs' | 'girls' | 'cars' | 'children' | 'boys' 
N[-CNT] -> 'water'

IV[TENSE=pres, NUM=sg, +CNT] -> 'disappears' | 'walks' | 'sings'
TV[TENSE=pres, NUM=sg, +CNT] -> 'sees' | 'likes' 

IV[TENSE=pres, NUM=pl] -> 'disappear' | 'walk' | 'sing'
TV[TENSE=pres, NUM=pl] -> 'see' | 'like' 

IV[TENSE=past] -> 'disappeared' | 'walked' | 'sang'
TV[TENSE=past] -> 'saw' | 'liked'

""")

p = nltk.FeatureChartParser(g) 

correct = ["the boy sings","the boys sing","boys sing","the water is precious","water is precious","all water is gone"]


false = ["boy sings", "every water is gone"]

for w in correct:
	token = w.split()
	print(w)
	if len(list(p.parse(token))) == 0:
		print('fail')

	for t in p.parse(token):
		print(t)

for w in false:
	token = w.split()
	print(w)
	if len(list(p.parse(token))) > 0:
		print('fail')
	for t in p.parse(token):
		print(t)
