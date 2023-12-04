# Approximation by Cost Algorithm O(log n)
def cover_cost_scaling(universe, subsets, costs):
    num_subsets = len(subsets)
    remaining_elements = set(range(1, universe + 1))
    scaled_costs = [costs[i] / len(subsets[i]) for i in range(num_subsets)]
    selected_subsets = []
    total_cost = 0

    while remaining_elements:
        best_subset = None
        min_scaled_cost = float('inf')

        for i in range(num_subsets):
            if i not in selected_subsets:
                intersection_size = len(subsets[i].intersection(remaining_elements))
                current_scaled_cost = scaled_costs[i] / intersection_size if intersection_size > 0 else float('inf')

                if current_scaled_cost < min_scaled_cost:
                    min_scaled_cost = current_scaled_cost
                    best_subset = i

        if best_subset is not None:
            selected_subsets.append(best_subset)
            remaining_elements -= subsets[best_subset]
            total_cost += costs[best_subset]
        else:
            break

    return selected_subsets, total_cost