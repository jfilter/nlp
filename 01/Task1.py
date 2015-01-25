# 1.a)

def mysucc(n):
	return n + 1

# 1.b)

def mymax(n, k):
	if k > n:
		return k
	return n

# 2

def countWords(input):
	words = input.split(" ")
	print(len(words))

	dic = {}
	for w in words:
		dic[w] = dic.get(w, 0) + 1
	for (k, v) in sorted(dic.items()):
		print(k + " " + str(v))

# 3

def orderWords(li):
	dic = {}
	for i in li:
		dic[i] = dic.get(i, 0) + 1
	return sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True) # ist umgekehrt lexiografisch sortiert

# 4

from curses.ascii import isalpha

def shorten(sentence, n):
	dic = {}
	for c in sentence:
		if isalpha(c):
			dic[c] = dic.get(c, 0) + 1

	chars_to_replace = set()
	tuples_should_be_replace = sorted(dic.items(), key=lambda x: (x[1], x[0]))[-n:]

	for (k, v) in (tuples_should_be_replace):
		chars_to_replace.add(k)
	print(chars_to_replace)

	res = ""
	for c in sentence:
		if not c in chars_to_replace:
			res += c
	return res
