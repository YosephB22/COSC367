% finding the last element of the list
last([X], X).
last([_|T], L) :- last(T, L).




test_answer :- 
    last([1, 2, 3, 4, 5], M),
    writeln(M).