import nltk

g = nltk.grammar.FeatureGrammar.fromstring(
"""
S -> NP

NP -> DET[CASE=?c, GND=?g, NUM=?n, DETER=?d] ADJECTIVE[CASE=?c, GND=?g, NUM=?n, DETER=?d] N[CASE=?c, GND=?g, NUM=?n]

ADJECTIVE[CASE=?c, GND=?g, NUM=?n, DETER=?d] -> ADJ[CASE=?c, GND=?g, NUM=?n, DETER=?d] | ADJ[CASE=?c, GND=?g, NUM=?n, DETER=?d] COMMA ADJECTIVE[CASE=?c, GND=?g, NUM=?n, DETER=?d] | 

COMMA -> ','

ADJ -> 'groß'

DET[CASE=nom, GND=w, NUM=sg, DETER=definite] -> 'die'
DET[CASE=gen, GND=w, NUM=sg, DETER=definite] -> 'der' 
DET[CASE=dat, GND=w, NUM=sg, DETER=definite] -> 'der' 
DET[CASE=akk, GND=w, NUM=sg, DETER=definite] -> 'die'

DET[CASE=nom, GND=w, NUM=sg, DETER=indefinite] -> 'eine'
DET[CASE=gen, GND=w, NUM=sg, DETER=indefinite] -> 'einer'
DET[CASE=dat, GND=w, NUM=sg, DETER=indefinite] -> 'einer'
DET[CASE=akk, GND=w, NUM=sg, DETER=indefinite] -> 'eine'

DET[CASE=nom, GND=n, NUM=sg, DETER=definite] -> 'das'
DET[CASE=gen, GND=n, NUM=sg, DETER=definite] -> 'des'
DET[CASE=dat, GND=n, NUM=sg, DETER=definite] -> 'dem'
DET[CASE=akk, GND=n, NUM=sg, DETER=definite] -> 'das'

DET[CASE=nom, GND=n, NUM=sg, DETER=indefinite] -> 'ein'
DET[CASE=gen, GND=n, NUM=sg, DETER=indefinite] -> 'eines'
DET[CASE=dat, GND=n, NUM=sg, DETER=indefinite] -> 'einem'
DET[CASE=akk, GND=n, NUM=sg, DETER=indefinite] -> 'ein'

DET[CASE=nom, GND=m, NUM=sg, DETER=definite] -> 'der'
DET[CASE=gen, GND=m, NUM=sg, DETER=definite] -> 'des'
DET[CASE=dat, GND=m, NUM=sg, DETER=definite] -> 'dem'
DET[CASE=akk, GND=m, NUM=sg, DETER=definite] -> 'den'

DET[CASE=nom, GND=m, NUM=sg, DETER=indefinite] -> 'ein'
DET[CASE=gen, GND=m, NUM=sg, DETER=indefinite] -> 'eines'
DET[CASE=dat, GND=m, NUM=sg, DETER=indefinite] -> 'einem'
DET[CASE=akk, GND=m, NUM=sg, DETER=indefinite] -> 'einen'

DET[NUM=pl, DETER=indefinite] ->

DET[CASE=nom, NUM=pl] -> 'die'
DET[CASE=gen, NUM=pl] -> 'der'
DET[CASE=dat, NUM=pl] -> 'den'
DET[CASE=akk, NUM=pl] -> 'die'

N[GND=w, NUM=sg] -> 'Sonne'

N[GND=w, NUM=pl] -> 'Sonnen'

N[CASE=nom, GND=n, NUM=sg] -> 'Sonnensystem'
N[CASE=gen, GND=n, NUM=sg] -> 'Sonnensystems'
N[CASE=dat, GND=n, NUM=sg] -> 'Sonnensystem'
N[CASE=akk, GND=n, NUM=sg] -> 'Sonnensystem'

N[CASE=nom, GND=n, NUM=pl] -> 'Sonnensysteme'
N[CASE=gen, GND=n, NUM=pl] -> 'Sonnensysteme'
N[CASE=dat, GND=n, NUM=pl] -> 'Sonnensystemen'
N[CASE=akk, GND=n, NUM=pl] -> 'Sonnensystem'

N[CASE=nom, GND=m, NUM=sg] -> 'Mond'
N[CASE=gen, GND=m, NUM=sg] -> 'Monds'
N[CASE=dat, GND=m, NUM=sg] -> 'Mond'
N[CASE=akk, GND=m, NUM=sg] -> 'Mond'

N[CASE=nom, GND=m, NUM=pl] -> 'Monde'
N[CASE=gen, GND=m, NUM=pl] -> 'Monde'
N[CASE=dat, GND=m, NUM=pl] -> 'Monden'
N[CASE=akk, GND=m, NUM=pl] -> 'Monde'

ADJ[CASE=nom, NUM=sg, GND=w] -> 'große'
ADJ[CASE=gen, NUM=sg, GND=w] -> 'großen' 
ADJ[CASE=dat, NUM=sg, GND=w] -> 'großen' 
ADJ[CASE=akk, NUM=sg, GND=w] -> 'großen'

ADJ[CASE=nom, NUM=sg, GND=n] -> 'großes'
ADJ[CASE=gen, NUM=sg, GND=n] -> 'großes' 
ADJ[CASE=dat, NUM=sg, GND=n] -> 'großen' 
ADJ[CASE=akk, NUM=sg, GND=n] -> 'großen'

ADJ[CASE=nom, NUM=sg, GND=m] -> 'großer'
ADJ[CASE=gen, NUM=sg, GND=m] -> 'großen' 
ADJ[CASE=dat, NUM=sg, GND=m] -> 'großen' 
ADJ[CASE=akk, NUM=sg, GND=m] -> 'großen'

ADJ[NUM=pl] -> 'großen'

""")

test =['des Sonnensystems', 'dem großen Mond', 'einer großen Sonne', 'Sonnen', 'der großen Sonnen', 'das große Sonnensystem', 'die großen Sonnensysteme', 'ein großer Mond', 'einen großen Mond', 'ein großes , großes Sonnensystem', 'eine große Sonne' ]

p = nltk.FeatureChartParser(g)

for w in test:
	res = p.parse(w.split())

	run = False

	for tree in res:
		run = True
		print(tree)

	if run:
		print('success')
	else:
		print('fail: ' + w)


# (S[]
#   (NP[]
#     (DET[CASE='gen', DETER='definite', GND='n', NUM='sg'] des)
#     (ADJECTIVE[CASE=?c, DETER=?d, GND=?g, NUM=?n] )
#     (N[CASE='gen', GND='n', NUM='sg'] Sonnensystems)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='dat', DETER='definite', GND='m', NUM='sg'] dem)
#     (ADJECTIVE[CASE='dat', DETER=?d, GND='m', NUM='sg']
#       (ADJ[CASE='dat', GND='m', NUM='sg'] großen))
#     (N[CASE='dat', GND='m', NUM='sg'] Mond)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='gen', DETER='indefinite', GND='w', NUM='sg'] einer)
#     (ADJECTIVE[CASE='gen', DETER=?d, GND='w', NUM='sg']
#       (ADJ[CASE='gen', GND='w', NUM='sg'] großen))
#     (N[GND='w', NUM='sg'] Sonne)))
# (S[]
#   (NP[]
#     (DET[CASE='dat', DETER='indefinite', GND='w', NUM='sg'] einer)
#     (ADJECTIVE[CASE='dat', DETER=?d, GND='w', NUM='sg']
#       (ADJ[CASE='dat', GND='w', NUM='sg'] großen))
#     (N[GND='w', NUM='sg'] Sonne)))
# success
# (S[]
#   (NP[]
#     (DET[DETER='indefinite', NUM='pl'] )
#     (ADJECTIVE[CASE=?c, DETER=?d, GND=?g, NUM=?n] )
#     (N[GND='w', NUM='pl'] Sonnen)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='gen', NUM='pl'] der)
#     (ADJECTIVE[CASE=?c, DETER=?d, GND=?g, NUM='pl']
#       (ADJ[NUM='pl'] großen))
#     (N[GND='w', NUM='pl'] Sonnen)))
# success
# fail: das große Sonnensystem
# (S[]
#   (NP[]
#     (DET[CASE='nom', NUM='pl'] die)
#     (ADJECTIVE[CASE=?c, DETER=?d, GND=?g, NUM='pl']
#       (ADJ[NUM='pl'] großen))
#     (N[CASE='nom', GND='n', NUM='pl'] Sonnensysteme)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='nom', DETER='indefinite', GND='m', NUM='sg'] ein)
#     (ADJECTIVE[CASE='nom', DETER=?d, GND='m', NUM='sg']
#       (ADJ[CASE='nom', GND='m', NUM='sg'] großer))
#     (N[CASE='nom', GND='m', NUM='sg'] Mond)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='akk', DETER='indefinite', GND='m', NUM='sg'] einen)
#     (ADJECTIVE[CASE='akk', DETER=?d, GND='m', NUM='sg']
#       (ADJ[CASE='akk', GND='m', NUM='sg'] großen))
#     (N[CASE='akk', GND='m', NUM='sg'] Mond)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='nom', DETER='indefinite', GND='n', NUM='sg'] ein)
#     (ADJECTIVE[CASE='nom', DETER=?d, GND='n', NUM='sg']
#       (ADJ[CASE='nom', GND='n', NUM='sg'] großes)
#       (COMMA[] ,)
#       (ADJECTIVE[CASE='nom', DETER=?d, GND='n', NUM='sg']
#         (ADJ[CASE='nom', GND='n', NUM='sg'] großes)))
#     (N[CASE='nom', GND='n', NUM='sg'] Sonnensystem)))
# success
# (S[]
#   (NP[]
#     (DET[CASE='nom', DETER='indefinite', GND='w', NUM='sg'] eine)
#     (ADJECTIVE[CASE='nom', DETER=?d, GND='w', NUM='sg']
#       (ADJ[CASE='nom', GND='w', NUM='sg'] große))
#     (N[GND='w', NUM='sg'] Sonne)))
# success
