% Initial State:
% Monkey is at door, box is at window,
% banana is at middle.

% Actions

move(state(door, window, on_floor, has_not),
     walk_to_window,
     state(window, window, on_floor, has_not)).

move(state(window, window, on_floor, has_not),
     push_box_to_middle,
     state(middle, middle, on_floor, has_not)).

move(state(middle, middle, on_floor, has_not),
     climb_box,
     state(middle, middle, on_box, has_not)).

move(state(middle, middle, on_box, has_not),
     grasp_banana,
     state(middle, middle, on_box, has)).

% Goal State

goal(state(_, _, _, has)).

% Planning Rule

solve(State, []) :-
    goal(State).

solve(State, [Action | Rest]) :-
    move(State, Action, NextState),
    solve(NextState, Rest).