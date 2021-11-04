duplicate([], []).
duplicate([H|T], [H, H|X]) :- duplicate(T, X).

test_answer :- 
    duplicate([1, 2, 3, 4, 5], M),
    writeln(M).