s(S1,S3) :- a(S1,S2), s2(S2,S3).
s2(S1,S3) :- s(S1,S2), b(S2,S3).
/*s2(S1,S3) :- b(S1,S3).*/
a([a|X], X).
b([b|X], X).