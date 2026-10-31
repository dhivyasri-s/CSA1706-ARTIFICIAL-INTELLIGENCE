planet(mercury).
planet(venus).
planet(earth).
planet(mars).
planet(jupiter).
planet(saturn).
planet(uranus).
planet(neptune).

display_planets :-
    planet(X),
    write(X),
    nl,
    fail.

display_planets.