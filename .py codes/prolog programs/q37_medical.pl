% Symptoms

symptom(ravi, fever).
symptom(ravi, cough).

symptom(raja, headache).
symptom(raja, fever).

symptom(priya, sneezing).
symptom(priya, cough).

% Disease Rules

diagnosis(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough).

diagnosis(Person, common_cold) :-
    symptom(Person, sneezing),
    symptom(Person, cough).

diagnosis(Person, headache_problem) :-
    symptom(Person, headache).

% Display Diagnosis

check_disease(Person, Disease) :-
    diagnosis(Person, Disease).