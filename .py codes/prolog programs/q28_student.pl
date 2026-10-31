student(dhivya, teacher1, cs101).
student(rahul, teacher2, cs102).
student(priya, teacher1, cs103).
student(ajay, teacher3, cs104).

student_teacher(Name, Teacher, Subject) :-
    student(Name, Teacher, Subject).