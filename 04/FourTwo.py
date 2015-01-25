import nltk
from nltk.corpus import brown

patterns = []
patterns = patterns + [(r'the$', 'AT')]
patterns = patterns + [(r'to$', 'TO')]
patterns = patterns + [(r'are$', 'BER')]
patterns = patterns + [(r'is$', 'BEZ')]
patterns = patterns + [(r'[.?!;]$', '.')]

patterns = patterns +  [(r'.*ing$', 'VBG'),(r'.*ed$', 'VBD'),(r'.*es$', 'VBZ'),(r'.*ould$', 'MD'),(r'.*\'s$', 'NN$'),(r'.*s$', 'NNS'),(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),(r'.*', 'NN')]

regexp_tagger = nltk.RegexpTagger(patterns)


sents = brown.sents(categories='news')
regexp_tagger.tag(sents[3])
res = regexp_tagger.evaluate(brown.tagged_sents(categories='news'))
print('Evaluation:' + str(res))

# Perfomance with the given Patterns
# 0.20326391789486245

# Improvements of my incremently added patterns, order of appearance
# 0.2585377011357082
# 0.2706903753207232
# 0.2739423593293156
# 0.2811921952383794
# 0.32546691330031624

my_text = 'We are going to the place you mentioned in your talks. On the way, I could buy you 15 donouts at Tiffany\'s Bakery. After we arrvied we saw a little chield. He cried really loudly.'
my_tokens = nltk.word_tokenize(my_text)
my_tagged_text = regexp_tagger.tag(my_tokens)
print(my_tagged_text)

counter = 0
for (_,tag) in my_tagged_text:
	counter = counter + 1 if tag == 'NN' else counter
print(counter / len(my_tagged_text))

# Without my Improvements 0.7804878048780488 of words are NN
# With Improvements 0.5121951219512195 of words are NN
