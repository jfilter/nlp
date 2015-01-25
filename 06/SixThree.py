import nltk
 	
grammar1 = nltk.CFG.fromstring("""
  S -> SENT S |
  SENT -> SUB VERB OBJ

  SUB -> "I" | "Andre" | "the Jamaica Observer" | "Usain Bolt"
  VERB -> "thought" | "said" | "reported that" | "broke"
  OBJ -> "the 100m record" |
  """)

text =  ["I", "thought", "Andre", "said", "the Jamaica Observer", "reported that",  "Usain Bolt", "broke", "the 100m record"]

for tree in nltk.RecursiveDescentParser(grammar1).parse(text):
	print(tree)
