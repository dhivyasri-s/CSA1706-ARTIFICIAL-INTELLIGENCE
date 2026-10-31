% Initial Facts

:- dynamic known/1.

known(has_fever).
known(has_cough).

% Rules

rule([has_fever, has_cough], flu).
rule([flu], take_rest).
rule([flu], drink_water).

% Forward Chaining

derive :-
    rule(Conditions, Result),
    forall(member(X, Conditions), known(X)),
    \+ known(Result),
    !,
    assertz(known(Result)),
    derive.

derive.

% Display All Derived Facts

forward_chain :-
    derive,
    known(X),
    write(X),
    nl,
    fail.

forward_chain.