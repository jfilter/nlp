# a)
import nltk
 	
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> N | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "I" | "hill" | "telescope"
  P -> "in" | "on" | "by" | "with"
  """)
 	
sent = "I saw the man on the hill with a telescope".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

# b)
"""
1. "Ich sah den Mann auf dem Teleskopberg."
(S
  (NP (N I))
  (VP
    (V saw)
    (NP
      (Det the)
      (N man)
      (PP
        (P on)
        (NP
          (Det the)
          (N hill)
          (PP (P with) (NP (Det a) (N telescope))))))))


2. "Ich sah den Mann auf dem Teleskopberg."
(S
  (NP (N I))
  (VP
    (V saw)
    (NP (Det the) (N man))
    (PP
      (P on)
      (NP
        (Det the)
        (N hill)
        (PP (P with) (NP (Det a) (N telescope)))))))


3. "Ich habe den Mann auf dem Hügel durch eine Telescio gesehen"
(S
  (NP (N I))
  (VP
    (V saw)
    (NP (Det the) (N man) (PP (P on) (NP (Det the) (N hill))))
    (PP (P with) (NP (Det a) (N telescope)))))

Jede Baumart gab es doppel. Ich haben die Baeume in drei verschiedenen Arten eingeteilt. Die ersten beiden sind sehr aehnlich und ich kann keine Beudeutungsaenderung feststellen.

Der dritte Baum sieht eine komplett andere Bedeutung in dem Satz.

"""