from inputs.day_2 import input

splitted = input.split("\n")
reports = []

for i in range(1, len(splitted) - 1):
    current_report = splitted[i].split(" ")
    reports.append([int(level) for level in current_report])

def is_increasing(report: list) -> bool:
    tolerant = 0
    last = report[0]

    for i in range(1, len(report)):
        if not (report[i] > last and 1 <= abs(report[i] - last) <= 3):
            if tolerant == 0:
                tolerant += 1
                last = report[i-2] if i - 2 >= 0 else report[0]
                continue
            else:
                print("Increasing", report)
                return False
        last = report[i]
    return True

def is_decreasing(report: list) -> bool:
    tolerant = 0
    last = report[0]

    for i in range(1, len(report)):
        if not (report[i] < last and 1 <= abs(report[i] - last) <= 3):
            if tolerant == 0:
                last = report[i-2] if i - 2 >= 0 else report[0]
                tolerant += 1
            else:
                print("Decreasing", report)
                return False
        last = report[i]
    return True

def find_safe_reports(reports: list) -> int:
    result = 0

    for report in reports:
        if is_increasing(report):
            result += 1
        if is_decreasing(report):
            result += 1

    return result

print(find_safe_reports(reports))
