import nltk, random

def sentgen(g):
  res = ''
  stack = [g.start()]

  while len(stack) > 0:
    s = stack.pop(0)
    new_symbols = random.choice(g.productions(s)).rhs()
    for new_symbol in reversed(new_symbols): # Because we are adding it at the front: reverse
      if type(new_symbol) == str:
        res += new_symbol + ' '
      else:
        stack = [new_symbol] + stack
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
""")

parser = nltk.ChartParser(g)
for i in range(0, 5):
    sentence = sentgen(g)
    print('%s. %s'%(i + 1, sentence))
    for t in parser.parse(sentence.split()):
        print(t)

"""
1. John saw an cat with the cat on Bob 
(S
  (NP John)
  (VP
    (V saw)
    (NP (Det an) (N cat) (PP (P with) (NP (Det the) (N cat))))
    (PP (P on) (NP Bob))))
(S
  (NP John)
  (VP
    (V saw)
    (NP (Det an) (N cat))
    (PP (P with) (NP (Det the) (N cat) (PP (P on) (NP Bob))))))
(S
  (NP John)
  (VP
    (V saw)
    (NP
      (Det an)
      (N cat)
      (PP (P with) (NP (Det the) (N cat) (PP (P on) (NP Bob)))))))
2. Bob saw Mary in Mary 
(S (NP Bob) (VP (V saw) (NP Mary) (PP (P in) (NP Mary))))
3. the park with Mary ate Bob 
(S
  (NP (Det the) (N park) (PP (P with) (NP Mary)))
  (VP (V ate) (NP Bob)))
4. my telescope in Mary saw a park with Bob 
(S
  (NP (Det my) (N telescope) (PP (P in) (NP Mary)))
  (VP (V saw) (NP (Det a) (N park)) (PP (P with) (NP Bob))))
(S
  (NP (Det my) (N telescope) (PP (P in) (NP Mary)))
  (VP (V saw) (NP (Det a) (N park) (PP (P with) (NP Bob)))))
5. Bob saw Bob 
(S (NP Bob) (VP (V saw) (NP Bob)))
"""