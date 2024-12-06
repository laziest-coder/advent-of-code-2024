from inputs.day_2 import input

splitted = input.split("\n")
reports, unsafe_reports = [], []

for i in range(1, len(splitted) - 1):
    current_report = splitted[i].split(" ")
    reports.append([int(level) for level in current_report])

def _is_increasing(report: list) -> bool:
    for i in range(1, len(report)):
        if not (report[i] > report[i-1] and 1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return True

def _is_decreasing(report: list) -> bool:
    for i in range(1, len(report)):
        if not (report[i] < report[i-1] and 1 <= abs(report[i] - report[i-1]) <= 3):
            return False
    return True

def find_safe_reports_part1(reports: list) -> int:
    result = 0

    for report in reports:
        if _is_increasing(report) or _is_decreasing(report):
            result += 1
        else:
            unsafe_reports.append(report)

    return result

safe_reports_count = find_safe_reports_part1(reports)

print(f"Result for part 1: {safe_reports_count}")


def find_safe_reports_part2() -> int:
    result = 0

    for report in unsafe_reports:
        success = False
        for i in range(len(report)):
            if success:
                break

            curr = report[:i] + report[i+1:]
            if _is_increasing(curr) or _is_decreasing(curr):
                result += 1
                success = True

    return result

print(f"Result for part 2: {safe_reports_count + find_safe_reports_part2()}")
