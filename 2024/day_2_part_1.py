from inputs.day_2 import input

splitted = input.split("\n")
reports = []

for i in range(1, len(splitted) - 1):
    current_report = splitted[i].split(" ")
    reports.append([int(level) for level in current_report])

def is_increasing(report: list) -> bool:
    for i in range(1, len(report)):
        if not (report[i] > report[i-1] and 1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return True

def is_decreasing(report: list) -> bool:
    for i in range(1, len(report)):
        if not (report[i] < report[i-1] and 1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return True

def find_safe_reports(reports: list) -> int:
    result = 0

    for report in reports:
        if is_increasing(report) or is_decreasing(report):
            result += 1

    return result

print(find_safe_reports(reports))
