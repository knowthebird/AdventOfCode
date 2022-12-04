# Part 1
first_sections = []
second_sections = []
count = 0;
with open('Day_4_Input.txt') as file:
    for line in file:
         comma_index = line.find(',')
         dash_indexes = [i for i, ltr in enumerate(line) if ltr == '-']
         start_range_one = int(line[0:dash_indexes[0]])
         end_range_one = int(line[dash_indexes[0]+1:comma_index])
         start_range_two = int(line[comma_index+1:dash_indexes[1]])
         end_range_two = int(line[dash_indexes[1]+1:-1])
         range_one = list(range(start_range_one, end_range_one+1))
         range_two = list(range(start_range_two, end_range_two+1))
         #print(range_one)
         #print(range_two)
         if all(elem in range_one  for elem in range_two) or all(elem in range_two  for elem in range_one):
             count += 1
print(count)

# Part 2
first_sections = []
second_sections = []
count = 0;
with open('Day_4_Input.txt') as file:
    for line in file:
         comma_index = line.find(',')
         dash_indexes = [i for i, ltr in enumerate(line) if ltr == '-']
         start_range_one = int(line[0:dash_indexes[0]])
         end_range_one = int(line[dash_indexes[0]+1:comma_index])
         start_range_two = int(line[comma_index+1:dash_indexes[1]])
         end_range_two = int(line[dash_indexes[1]+1:-1])
         range_one = list(range(start_range_one, end_range_one+1))
         range_two = list(range(start_range_two, end_range_two+1))
         #print(range_one)
         #print(range_two)
         if any(elem in range_one  for elem in range_two) or any(elem in range_two  for elem in range_one):
             count += 1
print(count)
