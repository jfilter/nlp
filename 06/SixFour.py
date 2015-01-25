import nltk


grammar1 = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I' | N
VP -> V NP | VP PP | V NP VP

Det -> 'a' | 'an' | 'my'
N -> 'John' | 'elephant' | 'pajamas' | 'cage'
V -> 'saw' | 'shooting'
P -> 'in'
""")

text = 'I saw John shooting an elephant in my pajamas in a cage'.split()

for tree in nltk.ChartParser(grammar1).parse(text):
	print(tree)


"""
Es gibt 8 unterschiedliche Baeume.


(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP
        (VP (V shooting) (NP (Det an) (N elephant)))
        (PP (P in) (NP (Det my) (N pajamas))))
      (PP (P in) (NP (Det a) (N cage))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP
        (V shooting)
        (NP
          (Det an)
          (N elephant)
          (PP (P in) (NP (Det my) (N pajamas)))))
      (PP (P in) (NP (Det a) (N cage))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (VP (V shooting) (NP (Det an) (N elephant)))
      (PP
        (P in)
        (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage))))))))
(S
  (NP I)
  (VP
    (V saw)
    (NP (N John))
    (VP
      (V shooting)
      (NP
        (Det an)
        (N elephant)
        (PP
          (P in)
          (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage)))))))))
(S
  (NP I)
  (VP
    (VP
      (VP
        (V saw)
        (NP (N John))
        (VP (V shooting) (NP (Det an) (N elephant))))
      (PP (P in) (NP (Det my) (N pajamas))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP
        (VP (V shooting) (NP (Det an) (N elephant)))
        (PP (P in) (NP (Det my) (N pajamas)))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP
        (V shooting)
        (NP
          (Det an)
          (N elephant)
          (PP (P in) (NP (Det my) (N pajamas))))))
    (PP (P in) (NP (Det a) (N cage)))))
(S
  (NP I)
  (VP
    (VP
      (V saw)
      (NP (N John))
      (VP (V shooting) (NP (Det an) (N elephant))))
    (PP
      (P in)
      (NP (Det my) (N pajamas) (PP (P in) (NP (Det a) (N cage)))))))
"""