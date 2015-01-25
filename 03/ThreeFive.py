# In allen drei Kategorien ist Noun am häufigsten vertreten, gefolgt von Verb. Generell sind News und Learned sehr ähnlich in der Verteilung. Nur det und . sind einmal vertauscht. Fiction stich ein wenig aus der Reihe. Der Unterschied zwischen Noun und Verb ist nur sehr gering. Auch ist APD schon an der dritten Stelle. 

import nltk
from nltk.corpus import brown

tagged_news = brown.tagged_words(categories="news", tagset="universal")
tagged_learned = brown.tagged_words(categories="learned", tagset="universal")
tagged_fiction = brown.tagged_words(categories="fiction", tagset="universal")

tagged_all = tagged_news + tagged_learned + tagged_fiction

fdist_all = nltk.FreqDist([t for (_,t) in tagged_all])
# fdist_all.plot()

fdist_news = nltk.FreqDist([t for (_,t) in tagged_news])
# fdist_news.plot()

fdist_learned = nltk.FreqDist([t for (_,t) in tagged_learned])
# fdist_learned.plot()

fdist_fiction = nltk.FreqDist([t for (_,t) in tagged_fiction])
# fdist_fiction.plot()

def proportion_coverd(dist, max, num_common):
	n = 0
	for (_,t) in dist.most_common(num_common):
		n += t
	return n / max

print('Most Common Cover - all')
print(proportion_coverd(fdist_all, len(tagged_all), 4))
print(proportion_coverd(fdist_all, len(tagged_all), 8))

print('Most Common Cover - news')
print(proportion_coverd(fdist_news, len(tagged_news), 4))
print(proportion_coverd(fdist_news, len(tagged_news), 8))

print('Most Common Cover - learned')
print(proportion_coverd(fdist_learned, len(tagged_learned), 4))
print(proportion_coverd(fdist_learned, len(tagged_learned), 8))

print('Most Common Cover - fiction')
print(proportion_coverd(fdist_fiction, len(tagged_fiction), 4))
print(proportion_coverd(fdist_fiction, len(tagged_fiction), 8))