import nltk
from nltk.corpus import brown

#sent = "The talk group members talk about group talk."
#sent = "We drink tea and you are going to order the special drink."
sent = "Let's try the new game because it is a really good try to take over this genre."

tokens = nltk.word_tokenize(sent)

brown_tagged_sents = brown.tagged_sents(categories=["news"])

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
bigram_tagger = nltk.BigramTagger(brown_tagged_sents, backoff=unigram_tagger)

print("UnigramTagger:", unigram_tagger.tag(tokens))
print("BigramTagger: ", bigram_tagger.tag(tokens))

# Results:
#
# UnigramTagger: [('The', 'AT'), ('talk', 'VB'), ('group', 'NN'), ('members', 'NNS'),
#                 ('talk', 'VB'), ('about', 'IN'), ('group', 'NN'), ('talk', 'VB'), ('.', '.')]
#
# BigramTagger:  [('The', 'AT'), ('talk', 'VB'), ('group', 'NN'), ('members', 'NNS'),
#                 ('talk', 'VB'), ('about', 'IN'), ('group', 'NN'), ('talk', 'NN'), ('.', '.')]