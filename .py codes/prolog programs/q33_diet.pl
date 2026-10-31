% Diet Suggestions Based on Disease

diet(diabetes, vegetables).
diet(diabetes, whole_grains).
diet(diabetes, green_salad).

diet(blood_pressure, low_salt_food).
diet(blood_pressure, fruits).
diet(blood_pressure, vegetables).

diet(obesity, low_calorie_food).
diet(obesity, fruits).
diet(obesity, green_salad).

diet(anemia, spinach).
diet(anemia, dates).
diet(anemia, beans).

% Rule to suggest diet

suggest_diet(Disease, Food) :-
    diet(Disease, Food).