from inputs.day_1 import input
from collections import Counter

list1, list2 = [], []
splitted = input.split("\n")

for i in range(1, len(splitted) - 1):
    l1, l2 = splitted[i].split("  ", 2)
    list1.append(int(l1))
    list2.append(int(l2))


def find_distance_part1(list1: list, list2: list) -> int:
    list1.sort()
    list2.sort()

    result = 0

    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        result += distance

    return result

print(find_distance_part1(list1, list2))

def find_distance_part2(list1: list, list2: list) -> int:
    result = 0
    l2_counter = Counter(list2)

    for num in list1:
        result += num * l2_counter[num] if num in l2_counter else 0

    return result

print(find_distance_part2(list1, list2))
