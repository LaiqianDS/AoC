from collections import defaultdict, deque

ordering_rules = [l.strip() for l in open("input").readlines() if "|" in l]
updates = [
    list(map(int, l.strip().split(",")))
    for l in open("input").readlines()
    if "|" not in l.strip() and len(l.strip()) > 0
]


def is_valid_update_direct(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    for rule in rules:
        x, y = map(int, rule.split("|"))
        if x in position and y in position and position[x] > position[y]:
            return False
    return True


def find_middle_page(update):
    n = len(update)
    return update[n // 2]


def correct_update_order(update, rules):
    position = {page: idx for idx, page in enumerate(update)}
    relevant_rules = [
        (int(x), int(y))
        for x, y in (rule.split("|") for rule in rules)
        if int(x) in position and int(y) in position
    ]
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in relevant_rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree.setdefault(x, 0)

    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


valid_updates = []
for update in updates:
    if is_valid_update_direct(update, ordering_rules):
        valid_updates.append(update)

middle_pages_direct = [find_middle_page(update) for update in valid_updates]

result = sum(middle_pages_direct)

print(result)

incorrect_updates = []
corrected_updates = []

for update in updates:
    if not is_valid_update_direct(update, ordering_rules):
        incorrect_updates.append(update)
        corrected_updates.append(correct_update_order(update, ordering_rules))

middle_pages_corrected = [find_middle_page(update) for update in corrected_updates]
result_corrected = sum(middle_pages_corrected)

print(result_corrected)
