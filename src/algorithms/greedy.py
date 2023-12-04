# Greedy Algorithm O(n^2)
def greedy(universe, subsets, costs):
    universe = set(range(1, universe + 1))
    subset_indices = list(range(len(subsets)))
    used_subsets = []

    while universe:
        min_cost_per_element = float('inf')
        chosen_subset = None

        for i in subset_indices:
            subset = subsets[i]
            cost = costs[i]
            unused_elements = len(subset.intersection(universe))
            if unused_elements == 0:
                continue
            cost_per_element = cost / unused_elements
            if cost_per_element < min_cost_per_element:
                min_cost_per_element = cost_per_element
                chosen_subset = i

        used_subsets.append(chosen_subset)
        universe -= subsets[chosen_subset]
        subset_indices.remove(chosen_subset)

    return used_subsets, sum(costs[i] for i in used_subsets)