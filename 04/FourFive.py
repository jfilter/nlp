import nltk
from nltk.corpus import brown

tagged_sents = brown.tagged_sents(categories='news')

size = int(len(tagged_sents) * 0.9)
train_sents = tagged_sents[:size]
test_sents = tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print(t3.evaluate(test_sents))

# The perfomance of the TrigramTagger is worse than the perfomance of the BigramTagger.
# BigramTagger: 0.8451111332602412
# TrigramTagger: 0.8439150802352238