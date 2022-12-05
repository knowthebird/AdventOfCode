# Part 1
List = []
List.append("NSDCVQT")
List.append("MFV")
List.append("FQWDPNHM")
List.append("DQRTF")
List.append("RFMNQHVB")
List.append("CFGNPWQ")
List.append("WFRLCT")
List.append("TZNS")
List.append("MSDJRQHN")
# Note, for both parts removed section of input file with initial orders of lists.
with open('Day_5_Input.txt') as file:
    for line in file:
        space_indexes = [i for i, ltr in enumerate(line) if ltr == " "]
        count = int(line[space_indexes[0]:space_indexes[1]])
        from_set = int(line[space_indexes[2]:space_indexes[3]]) - 1
        to_set = int(line[space_indexes[4]:-1]) - 1
        List[to_set] += List[from_set][-count:][::-1]
        List[from_set] = List[from_set][:-count]
result = ""
for item in List:
    result += item[-1]
print(result)

# Part 2
List = []
List.append("NSDCVQT")
List.append("MFV")
List.append("FQWDPNHM")
List.append("DQRTF")
List.append("RFMNQHVB")
List.append("CFGNPWQ")
List.append("WFRLCT")
List.append("TZNS")
List.append("MSDJRQHN")
with open('Day_5_Input.txt') as file:
    for line in file:
        space_indexes = [i for i, ltr in enumerate(line) if ltr == " "]
        count = int(line[space_indexes[0]:space_indexes[1]])
        from_set = int(line[space_indexes[2]:space_indexes[3]]) - 1
        to_set = int(line[space_indexes[4]:-1]) - 1
        List[to_set] += List[from_set][-count:]
        List[from_set] = List[from_set][:-count]
result = ""
for item in List:
    result += item[-1]
print(result)
