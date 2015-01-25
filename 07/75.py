import nltk

fs1  = nltk.FeatStruct("[A = ?x, B= [C = ?x]]")
fs2  = nltk.FeatStruct("[B = [D = d]]")
fs3  = nltk.FeatStruct("[B = [C = d]]")
fs4  = nltk.FeatStruct("[A = (1)[B = b], C->(1)]")
fs5  = nltk.FeatStruct("[A = (1)[D = ?x], C = [E -> (1), F = ?x] ]")
fs6  = nltk.FeatStruct("[A = [D = d]]")
fs7  = nltk.FeatStruct("[A = [D = d], C = [F = [D = d]]]")
fs8  = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs9  = nltk.FeatStruct("[A = [B = b], C = [E = [G = e]]]")
fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")

print('f1 and f2')
print(fs1.unify(fs2))
print()
print(nltk.FeatStruct("[A = ?x, B= [C = ?x, D = d]]"))

print('f1 and f3')
print(fs1.unify(fs3))
print()
print(nltk.FeatStruct("[A = d, B= [C = d]]"))

print('f4 and f5')
print(fs4.unify(fs5))
print()
print(nltk.FeatStruct("[A = (1)[B = b, D = ?x, E -> (1), F = ?x], C->(1)]"))

print('f5 and f6')
print(fs5.unify(fs6))
print()
print(nltk.FeatStruct("[A = (1)[D = d], C = [E -> (1), F = d] ]"))

print('f5 and f7')
print(fs5.unify(fs7))
print()
print('Nich moeglich')

print('f8 and f9')
print(fs8.unify(fs9))
print()
print(nltk.FeatStruct("[A = (1)[B = b, D = e, G = e], C = [B = e, E -> (1)] ]"))

print('f8 and f10')
print(fs8.unify(fs10))
print()
print(nltk.FeatStruct("[A = (1)[B = b, D = b, E -> (1), G = b], C -> (1)]"))



"""

fs8  = nltk.FeatStruct("[A = (1)[D = ?x, G = ?x], C = [B = ?x, E -> (1)] ]")
fs10 = nltk.FeatStruct("[A = (1)[B = b], C -> (1)]")
fs8fs10 = nltk.FeatStruct("[A = (1)[B = b, D = b, E -> (1), G = b], C -> (1)]")

In : fs8.unify(fs10)
Out: [A=(1)[B='b', D='b', E->(1), G='b'], C->(1)]

"""