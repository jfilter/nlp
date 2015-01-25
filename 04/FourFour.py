from nltk.corpus import brown
from collections import defaultdict

dic = defaultdict(set)

# for (w, t) in brown.tagged_words(categories='news', tagset='universal'):
for (w, t) in brown.tagged_words(categories='news'):
     dic[w].add(t)
 
counter = 0
for word in dic:
     if len(dic[word]) > 1:
             print(word, dic[word])
     else:
     		counter = counter + 1

print(counter/len(dic))

# b)
# Wenn in einem Text nur Types genommen werden, sind 100% der Woerter des Eingabetextes Woerter mit nur einem Tag. Da sie ja nicht in mehrere Saetzen vorkommen koennen, da sie ja nur einmal angesehen werden.
# Wenn sie als Token betrachtet werden, erhalten wir das Ergebnis bei c)

# c)
# Mit dem Standart-Tagset
# 0.8802973461164374 der Wörter haben nur ein Tag.

# Mit dem 'universal' tagset (simplified)
# 0.952827567041823 der Wörter haben nur ein Tag.
