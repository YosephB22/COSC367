remove_at([], 1, []).
remove_at(Target, [H|T], N, [H|Result]) :- Dec is N - 1, N =\= 1, remove_at(Target, T, Dec, Result).


test_answer :- 
    remove_at(X,[a,b,c,d],2,R),
    writeln(R),
    writeln(R).