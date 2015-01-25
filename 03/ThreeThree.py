import nltk
from nltk.corpus import brown

news_text = brown.words(categories="fiction")
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ["what", "when", "where", "who", "why"]

for m in modals:
    print(m + ':', fdist[m], end=" ")

# Result: what: 186 when: 192 where: 89 who: 112 why: 42