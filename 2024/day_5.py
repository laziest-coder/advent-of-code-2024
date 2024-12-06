from inputs.day_5 import rules, updates
from collections import defaultdict

rules_dict = defaultdict(set)
rules_splitted = rules.split("\n")

for i in range(1, len(rules_splitted) - 1):
    x, y = rules_splitted[i].split("|")
    rules_dict[x].add(y)

updates_splitted = updates.split("\n")
updates_list = []

for i in range(1, len(updates_splitted) - 1):
    updates_list.append(updates_splitted[i].split(","))

def part_1() -> int:
    result = 0
    valid_updates = []

    for update in updates_list:
        is_valid = True

        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in rules_dict[update[i]]:
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            valid_updates.append(update)
    
    for update in valid_updates:
        mid = len(update) // 2
        result += int(update[mid])

    return result

print(f"Result for part 1: {part_1()}")

# {
#     75: set(29, 53, 47, 61, 13),
#     47: set(53, 13, 61, 29)
# }