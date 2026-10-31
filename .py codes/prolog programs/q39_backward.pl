% Initial Facts

known(has_fever).
known(has_cough).

% Rules

rule(flu, [has_fever, has_cough]).
rule(take_rest, [flu]).
rule(drink_water, [flu]).

% Backward Chaining

prove(Goal) :-
    known(Goal).

prove(Goal) :-
    rule(Goal, Conditions),
    prove_all(Conditions).

% Check All Conditions

prove_all([]).

prove_all([X | Rest]) :-
    prove(X),
    prove_all(Rest).