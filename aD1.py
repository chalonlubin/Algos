"""Advent of Code 2022, Day 1"""

# Get data
with open('aD1.in') as file:
    data = [i for i in file.read().strip().split("\n")]


def find_max(data):
    max = 0
    count = 0

    for item in data:
        if item == "":
            count = 0
        else:
            num = int(item)
            count += num
        if count > max:
            max = count

def find_top_three(data):
    all_elf = []
    cur_count = 0

    for item in data:
        if item == "":
            all_elf.append(int(cur_count))
            cur_count = 0
        else:
            num = int(item)
            cur_count += num
    all_elf.sort(reverse=True)
    return sum(all_elf[0:3])





print(find_top_three(data))