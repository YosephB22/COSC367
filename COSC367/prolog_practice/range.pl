range(N, N, [N]).
range(P, N, [P|New]) :- M is P + 1, range(M, N, New).

test_answer :- 
    range(4,9,L),
    writeln(L).