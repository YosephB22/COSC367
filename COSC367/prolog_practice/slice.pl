slice([H], 1, 1, [H]).
slice([H|T1], 1, N2, [H|Result]) :- N2 > 1, Two is N2 - 1, slice(T1, 1, Two, Result).
slice([_|T], N1, N2, Result) :- N1 > 1, One is N1 - 1, Two is N2 - 1, slice(T, One, Two, Result).


test_answer :- 
    slice([a,b,c,d,e,f,g,h,i,k],3,7,L),
    writeln(L).
% L = [c, d, e, f, g].