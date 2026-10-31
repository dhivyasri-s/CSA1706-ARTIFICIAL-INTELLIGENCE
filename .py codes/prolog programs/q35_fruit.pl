% Fruit and Colour Facts

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(guava, green).

% Rule to display fruit and colour

show_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).