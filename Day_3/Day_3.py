import string

# Part 1
count = 0
with open('Day_3_Input.txt') as file:
    for line in file:
        items = []
        items[:0] = line
        first_bag = items[:len(items)//2]
        second_bag = items[len(items)//2:-1]
        item_in_both_bags = set([item for item in first_bag if item in second_bag]).pop()
        if item_in_both_bags in string.ascii_lowercase:
            count += (string.ascii_lowercase.index(item_in_both_bags)+1)
        else:
            count += (string.ascii_uppercase.index(item_in_both_bags)+27)
print(count)

# Part 2
count = 0
elve_num = 0
first_bag = []
second_bag = []
third_bag = []
with open('Day_3_Input.txt') as file:
    for line in file:
        elve_num += 1
        third_bag = second_bag
        second_bag = first_bag
        first_bag = []
        first_bag[:0] = line[:-1]
        print(first_bag)
        if elve_num % 3 == 0:
            items_in_two_bags = [item for item in first_bag if item in second_bag]
            item_in_three_bags = set([item for item in items_in_two_bags if item in third_bag]).pop()
            if item_in_three_bags in string.ascii_lowercase:
                count += (string.ascii_lowercase.index(item_in_three_bags)+1)
            else:
                count += (string.ascii_uppercase.index(item_in_three_bags)+27)
print(count)
