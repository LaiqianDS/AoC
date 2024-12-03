def is_safe(report):
    """Check if a report is safe."""
    if all(report[i + 1] - report[i] in range(1, 4) for i in range(len(report) - 1)):
        return True
    if all(report[i] - report[i + 1] in range(1, 4) for i in range(len(report) - 1)):
        return True
    return False


def is_safe_with_dampener(report):
    """Check if a report is safe with the Problem Dampener."""
    if is_safe(report):
        return True
    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports_with_dampener(reports):
    return sum(is_safe_with_dampener(report) for report in reports)


reports = [list(map(int, line.split())) for line in open("Day2/input", "r").readlines()]

part1 = sum(is_safe(report) for report in reports)
part2 = count_safe_reports_with_dampener(reports)

print(f"Number of safe reports: {part1}")
print(f"Number of safe reports with dampener: {part2}")
