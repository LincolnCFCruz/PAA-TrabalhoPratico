from itertools import chain, combinations

# Brute Force Algorithm O(n^2)
def brute_force(universe, subsets, costs):
    n = len(subsets)
    min_cost = float('inf')
    min_set = None

    for combo in chain(*map(lambda x: combinations(range(n), x), range(0, n + 1))):
        cover = set().union(*(subsets[i] for i in combo))
        cost = sum(costs[i] for i in combo)

        if cover == set(range(1, universe + 1)) and cost < min_cost:
            min_cost = cost
            min_set = combo

    return min_set, min_cost