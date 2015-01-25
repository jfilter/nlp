import nltk, random

def get_terminals(g):
	res = set()

	for p in g.productions():
		for symbol in p.rhs():
			if type(symbol) != nltk.grammar.Nonterminal:
				res.add(symbol)
	return res

def get_nonterminals(g):
	res = set()

	for p in g.productions():
		for symbol in p.rhs():
			if type(symbol) == nltk.grammar.Nonterminal:
				res.add(symbol)
	return res

def special_symbols(g):
	res = set()
	res = res.union(get_terminals(g))
	last_size = -1

	while not last_size == len(res):
		last_size = len(res)
		for p in g.productions():
			# print(res)
			add = True
			for symbol in p.rhs():
				if not symbol in res:
					add = False	
			if add:
				res = res.union([p.lhs()])
	return res



def sent_gen(g, n):
	possible_result = _sent_gen(g, g.start(), n, '', 1)

	# only need if algorithm is stuck in greey approach
	if len(possible_result.split()) > n:
		return possible_result
	else:
		return sent_gen(g, n)

def _sent_gen(g, x, n, res, d):

	rhs = random.choice(g.productions(x)).rhs()

	 # add random, so you may get a result if the greedy approach isn't working
	if random.random() > 0.1 and n > len(res.split()) + d:
		best_to_choose = g.productions(x)

		max_len = -1
		best = -1
		for i in range(0, len(best_to_choose)):
			c_l = len(best_to_choose[i].rhs())
			if c_l > max_len:
				best = i
				max_len = c_l

		rhs = best_to_choose[best].rhs()

	for a in rhs:
		if type(a) == str:
			res += ' ' + a
		else:
			res = _sent_gen(g, a, n, res, d + 1)
	return res


g = nltk.CFG.fromstring("""
S   -> NP VP
VP  -> V NP | V NP PP
PP  -> P NP
V   -> 'saw' | 'ate' | 'walked'
NP  -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
Det -> 'a' | 'an' | 'the' | 'my'
N   -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P   -> 'in' | 'on' | 'by' | 'with'
PETER -> LALA
""")

g_a = nltk.CFG.fromstring("""
S -> S S
S -> 'a'
""")

# print(get_terminals(g))
# print(get_nonterminals(g))
# print(special_symbols(g))
print(sent_gen(g_a, 3)) # wigh
"""
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 a a a a
Johanness-MacBook-Pro:07 filter$ 
"""

print(sent_gen(g, 3))
print(sent_gen(g, 10))
"""
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 a park with the cat with my dog in John ate Mary
 a man in a man by Mary ate John with an telescope
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 the park with the man by my dog by Bob saw Bob
 a man in a man with Bob walked the man with Mary on a cat
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 the park on Bob walked Bob
 a man in a dog in the man with the dog saw a dog with my park
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 my dog with a cat with a dog walked my cat
 a man in Mary saw a man by an park in a dog on a cat in John
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 an park by Bob ate an cat in Bob by John
 a man in John saw a park with an man in an dog with an dog in John
Johanness-MacBook-Pro:07 filter$ python3 76.py 
 my telescope in the telescope walked Bob with Bob
 a man with a man by Bob saw Bob on Bob
"""

"""
d) Es werden nur Nicht-Terminale gefunden, die auch wirklich real verwendet werden koennen.
"""
