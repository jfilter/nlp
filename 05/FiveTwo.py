import nltk

patterns = []
patterns += [(r'^[A-Z]+(.*)(er$|el$|or$|eur$|ent$|ant$|ist$|oge$|us$|e$|t$|ung$|heit$|keit$|schaft$|tion$|ur$|ar$|ät$|a$|ei$|ie$|in$|ine$|euse$|chen$|lein$|nis$|um$|ium$)', 'Nomen')]
patterns += [(r'^[a-z]+(sam$|ig$|lich$|isch$|haft$|bar$|los$)','Adjektiv')]


regexp_tagger = nltk.RegexpTagger(patterns)

f = open("linus.txt", mode="r", encoding="utf8")
text = f.read()

token = nltk.word_tokenize(text)
tagged_text = regexp_tagger.tag(token)

[print(t) for t in tagged_text if t[1] != None]

# Die Leistungsfaegigkeit wurde an dem Text uberprueft. Es gibt wenige False Positives auch viele False Negatives.
# Die Deutsche Sprache ist zu komplex um sie mit Hilfe seine simples Taggers zu klassifizieren.
