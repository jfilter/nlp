# Es muss erst eine ungerade Zahl auftreten, dann gelangt man in den Zustand A.
# Dort darf nur eine weitere ungerade Zahl auftreten, wenn auch genau eine folgt.
# Die geraden werden ignoriert, weil sie irellevant sind.
# Damit die Quersumm ungerade ist, muss die Anzahl der ungerade Zahlen ungerade sein.

import nltk
 	
grammar1 = nltk.CFG.fromstring("""
  S -> EVEN S | ODD A
  A -> EVEN A | ODD B ODD A |
  B -> ODD B |
  ODD -> "1" | "3" | "5" | "7" | "9"
  EVEN -> "2" | "4" | "6" | "8" | "0"
  """)

positive_tests = ["1", "0 0 9", "1 4", "0 1 5 0 3", "2 7", "0 3"]
negative_tests = ["2", "0 2 4", "0 0 2", "9 9 0 0"]

print('Positve Tests:')
for word in positive_tests:
  rd_parser = nltk.RecursiveDescentParser(grammar1)
  [print('success') for tree in rd_parser.parse(word.split()) if len(tree) > 0]

print('Negatives Tests:')
for word in negative_tests:
  rd_parser = nltk.RecursiveDescentParser(grammar1)
  [print('fail') for tree in rd_parser.parse(word.split()) if len(tree) > 0]

