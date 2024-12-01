from inputs.day_1 import input

list1, list2 = [], []
splitted = input.split("\n")

for i in range(1, len(splitted) - 1):
    l1, l2 = splitted[i].split("  ", 2)
    list1.append(int(l1))
    list2.append(int(l2))


def find_distance(list1: list, list2: list) -> int:
    list1.sort()
    list2.sort()

    result = 0

    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        result += distance

    return result

print(find_distance(list1, list2))
