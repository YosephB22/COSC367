element_at(B, [B|_], 1).
element_at(H, [_|T], NUmber) :- Num is NUmber - 1, element_at(H, T, Num).



test_answer :- 
    element_at(X,[a,b,c,d,e],3),
    writeln(X).