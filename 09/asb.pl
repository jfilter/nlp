f(n,s) :- s=[H|T],((H = a, f(n + 1, T));(H = b, g(n - 1,T))).
g(n,s) :- s=[H|T],((s == [], n =:= 0);(H = b, g(n - 1,T))).
