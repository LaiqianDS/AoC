from collections import defaultdict, deque

ordering_rules = [l.strip() for l in open("input").readlines() if "|" in l]
updates = [
    list(map(int, l.strip().split(",")))
    for l in open("input").readlines()
    if "|" not in l.strip() and len(l.strip()) > 0
]


def is_valid(update, rules):
    pos = {page: idx for idx, page in enumerate(update)}
    for rule in rules:
        x, y = map(int, rule.split("|"))
        if x in pos and y in pos and pos[x] > pos[y]:
            return False
    return True


def find_mid(update):
    n = len(update)
    return update[n // 2]


def correct(update, rules):
    pos = {page: idx for idx, page in enumerate(update)}
    relevant_rules = [
        (int(x), int(y))
        for x, y in (rule.split("|") for rule in rules)
        if int(x) in pos and int(y) in pos
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
    if is_valid(update, ordering_rules):
        valid_updates.append(update)

middle_pages_direct = [find_mid(update) for update in valid_updates]

result = sum(middle_pages_direct)

print(result)

incorrect_updates = []
corrected_updates = []

for update in updates:
    if not is_valid(update, ordering_rules):
        incorrect_updates.append(update)
        corrected_updates.append(correct(update, ordering_rules))

mid_correct = [find_mid(update) for update in corrected_updates]
result2 = sum(mid_correct)

print(result2)
