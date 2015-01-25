import nltk

f = open("staedte.txt", mode="r", encoding="utf8")
names = [line.strip() for line in f.readlines()]

# print(names)

pattern = [(r'[Bad .*$ | .*leben$]', 'City'), (r'.*rode$', 'City'),  (r'.*burg$', 'City'),  (r'.*dorf$', 'City'), (r'.*stadt$', 'City'), (r'.*heim$', 'City'),  (r'.*furt$', 'City'),  (r'.*ow$', 'City'), (r'.*feld$', 'City'), (r'.*thal$', 'City'),  (r'.*ingen$', 'City'),  (r'.*bach$', 'City'),  (r'.*kirchen$', 'City')]

regex_tagger = nltk.RegexpTagger(pattern)

tagged = regex_tagger.tag(names)
# print(tagged)

counter = 0

for _,tag in tagged:
	counter = counter + 1 if tag != None else counter

print('Correctly classified: ' + str(counter / len(tagged)))
# Correctly classified: 0.36403723664870163

# a)
# Liste der Städte gibt es hier: https://de.wikipedia.org/wiki/Liste_der_Städte_in_Deutschland
# Man müsste sie ggfs. aus dem HTML herausparsen.

# b)
# In der Liste der Woerter nach Haeufigkeiten analysieren. Strukturen erkennen etc.

# c)
# Der Anteil liegt bei circa 36%.

# d)
# Ja, z.B. Kinderheim, Innenstadt, Stadtleben.


