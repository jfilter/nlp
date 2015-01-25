a)
d --> [].

b)
dog is refering to a rule dog.
[dog] is a list with dog as element of it.

c)
It's not working, but I don't know why...

f(n,s) :- s=[H|T],((H = a, f(n + 1, T));(H = b, g(n - 1,T))).
g(n,s) :- s=[H|T],((s = [], n =:= 0);(H = b, g(n - 1,T))).
