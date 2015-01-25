import nltk

g = nltk.grammar.FeatureGrammar.fromstring(
"""
S -> NP

NP[CASE=?c, GND=?g, NUM=?n] -> DET[CASE=?c, GND=?g, NUM=?n] N[CASE=?c, GND=?g, NUM=?n]

DET[CASE=nom, GND=w, NUM=sg] -> 'die' | 'eine'
DET[CASE=gen, GND=w, NUM=sg] -> 'der' | 'einer'
DET[CASE=dat, GND=w, NUM=sg] -> 'der' | 'einer'
DET[CASE=akk, GND=w, NUM=sg] -> 'die' | 'eine'

DET[CASE=nom, GND=n, NUM=sg] -> 'das' | 'ein'
DET[CASE=gen, GND=n, NUM=sg] -> 'des' | 'eines'
DET[CASE=dat, GND=n, NUM=sg] -> 'dem' | 'einem'
DET[CASE=akk, GND=n, NUM=sg] -> 'das' | 'ein'

DET[CASE=nom, GND=m, NUM=sg] -> 'der' | 'ein'
DET[CASE=gen, GND=m, NUM=sg] -> 'des' | 'eines'
DET[CASE=dat, GND=m, NUM=sg] -> 'dem' | 'einem'
DET[CASE=akk, GND=m, NUM=sg] -> 'den' | 'einen'

N[GND=w, NUM=sg] -> 'Sonne'

N[CASE=nom, GND=n, NUM=sg] -> 'Sonnensystem'
N[CASE=gen, GND=n, NUM=sg] -> 'Sonnensystems'
N[CASE=dat, GND=n, NUM=sg] -> 'Sonnensystem'
N[CASE=akk, GND=n, NUM=sg] -> 'Sonnensystem'

N[CASE=nom, GND=m, NUM=sg] -> 'Mond'
N[CASE=gen, GND=m, NUM=sg] -> 'Monds'
N[CASE=dat, GND=m, NUM=sg] -> 'Mond'
N[CASE=akk, GND=m, NUM=sg] -> 'Mond'
""")

test =['des Sonnensystems', 'dem Mond', 'einer Sonne']

p = nltk.FeatureChartParser(g)

for w in test:
	for tree in p.parse(w.split()):
		print(tree)

# (S[]
#   (NP[CASE='gen', GND='n', NUM='sg']
#     (DET[CASE='gen', GND='n', NUM='sg'] des)
#     (N[CASE='gen', GND='n', NUM='sg'] Sonnensystems)))
# (S[]
#   (NP[CASE='dat', GND='m', NUM='sg']
#     (DET[CASE='dat', GND='m', NUM='sg'] dem)
#     (N[CASE='dat', GND='m', NUM='sg'] Mond)))
# (S[]
#   (NP[CASE='gen', GND='w', NUM='sg']
#     (DET[CASE='gen', GND='w', NUM='sg'] einer)
#     (N[GND='w', NUM='sg'] Sonne)))
# (S[]
#   (NP[CASE='dat', GND='w', NUM='sg']
#     (DET[CASE='dat', GND='w', NUM='sg'] einer)
#     (N[GND='w', NUM='sg'] Sonne)))