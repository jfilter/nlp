import nltk
from nltk.corpus import brown

def tag_ratio(tagset, tag): 
	counter = 0

	for (_,t) in tagset:
		if t == tag:
			counter += 1

	return counter / len(tagset)

# print(brown.tagged_words(categories="news", tagset="universal"))

print(tag_ratio(brown.tagged_words(categories="news", tagset="universal"), "NOUN"))