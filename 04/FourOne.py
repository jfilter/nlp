def a(t):
	return [len(w) for w in t if 'a' in w]

def b(t):
	return [w for w in set(t) if len(w) == 4]

print(a(['Daies', 'ist', 'eain', 'Beispiel', '.']))
print(b(['Daies', 'ist', 'eain','eain', 'Beispiel', '.']))
