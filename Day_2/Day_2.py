# Part 1
Scores = []
with open('Day_2_Input.txt') as file:
    for line in file:
        match line[0]:
            case "A":
                match line[2]:
                    case "X":
                        Scores.append(int(1+3))
                    case "Y":
                        Scores.append(int(2+6))
                    case "Z":
                        Scores.append(int(3+0))
            case "B":
                match line[2]:
                    case "X":
                        Scores.append(int(1+0))
                    case "Y":
                        Scores.append(int(2+3))
                    case "Z":
                        Scores.append(int(3+6))
            case "C":
                match line[2]:
                    case "X":
                        Scores.append(int(1+6))
                    case "Y":
                        Scores.append(int(2+0))
                    case "Z":
                        Scores.append(int(3+3))
print(sum(Scores))

# Part 2
Scores = []
with open('Day_2_Input.txt') as file:
    for line in file:
        match line[0]:
            case "A":
                match line[2]:
                    case "X":
                        Scores.append(int(3+0))
                    case "Y":
                        Scores.append(int(1+3))
                    case "Z":
                        Scores.append(int(2+6))
            case "B":
                match line[2]:
                    case "X":
                        Scores.append(int(1+0))
                    case "Y":
                        Scores.append(int(2+3))
                    case "Z":
                        Scores.append(int(3+6))
            case "C":
                match line[2]:
                    case "X":
                        Scores.append(int(2+0))
                    case "Y":
                        Scores.append(int(3+3))
                    case "Z":
                        Scores.append(int(1+6))
print(sum(Scores))
