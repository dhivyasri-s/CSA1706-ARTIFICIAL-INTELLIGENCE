% Bird Facts

bird(parrot).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

% Birds that cannot fly

cannot_fly(ostrich).
cannot_fly(penguin).

% Rule to check flying ability

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).