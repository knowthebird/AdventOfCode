# Part 1
MostCalories = 0
CurrentCalories = 0
with open('input.txt') as file:
    for line in file:
        if line in ['\n', '\r\n']:
            if CurrentCalories > MostCalories:
                MostCalories = CurrentCalories
            CurrentCalories = 0
        else:
            CurrentCalories += int(line);
print(MostCalories)

# Part 2
Calories = []
CurrentCalories = 0
with open('input.txt') as file:
    for line in file:
        if line in ['\n', '\r\n']:
            Calories.append(CurrentCalories)
            CurrentCalories = 0
        else:
            CurrentCalories += int(line);
print(sum(sorted(Calories)[-3:]))
