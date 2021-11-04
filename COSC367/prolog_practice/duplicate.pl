
dupli([], []).
dupli([H|T], [H, H|T2]) :- dupli(T, T2).


test_answer :- 
    dupli([a,b,c,c,d],X),
    writeln(X).