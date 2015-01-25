suf = ['ten', 'en', 'te', 'st', 'e', 't'] # mind the order!

def rootform(input):
	for s in suf:
		if input.endswith(s):
			return input[:len(input)-len(s)]
	return input

def inflect(root):
	return 'ich %(root)se, du %(root)sst , er/sie/es %(root)st, wir %(root)sen, ihr %(root)st, sie %(root)sen' % {'root': root}

print(inflect('lieb'))
print(rootform('liebe'))
print(rootform('winkte'))
print(rootform('taten'))

# c) 
# Ja, es funktiniet nur bei regelmäßigen Verben. Negagitve Beispiele: fuhr, trunk, ging
# Oder auch zum Beispiel bei a) versagt mein Algorithmus bei taten. Der Stamm ist natürlich nicht 'ta'
# So ein Stemmer ist eine eher komplexe Angelegenheit und laesst sich nicht durch so ein simples Python-Script loesen. ;)

