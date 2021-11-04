%reversing a list
reversed(List1, M) :- reversed(List1, [], M).
reversed([], R, R).
reversed([H|T], Acc, M) :- reversed(T,  [H|Acc], M).


test_answer :- 
    reversed([1, 2, 3, 4, 5], M),
    writeln(M).