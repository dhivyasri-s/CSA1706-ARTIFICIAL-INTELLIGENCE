% Name and Date of Birth Database

person(dhivya, 15, 5, 2006).
person(rahul, 10, 8, 2005).
person(priya, 20, 3, 2006).
person(ajay, 12, 1, 2004).

% Display person details

show_person(Name, Day, Month, Year) :-
    person(Name, Day, Month, Year),
    write('Name: '),
    write(Name),
    nl,
    write('DOB: '),
    write(Day), write('/'),
    write(Month), write('/'),
    write(Year),
    nl.