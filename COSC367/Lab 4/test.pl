tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

listtran([], []).
listtran([H|T1], [H2|T2]) :- tran(H,H2), listtran(T1, T2).

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).