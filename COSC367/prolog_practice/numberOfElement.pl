%finding the number of element
element_number([], 0).
element_number([_|T], N) :- element_number(T, P), N is P + 1.


test_answer :- 
    element_number([1, 2], M),
    writeln(M).