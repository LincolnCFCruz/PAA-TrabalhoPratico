import random

# Data sets for testing
def test_data(i):
    if i == 0:
        universe = 5
        subsets = [ set([1, 2]), set([2, 3]), set([4, 5]) ]
        costs = [10, 5, 8]

        return universe, subsets, costs

    if i == 1:
        universe = 5
        subsets = [set([1, 2, 3]), set([3, 4]), set([4, 5]), set([1, 2, 5])]
        costs = [2, 3, 4, 5]

        return universe, subsets, costs

    if i == 2:
        universe = 7
        subsets = [set([1, 2, 3]), set([3, 4]), set([4, 5]), set([1, 2, 5]), set([6, 7])]
        costs = [2, 3, 4, 5, 1]

        return universe, subsets, costs

    if i == 3:
        universe = 4
        subsets = [set([1, 2]), set([2, 3]), set([3, 4]), set([1, 4])]
        costs = [2, 3, 4, 1]

        return universe, subsets, costs

    if i == 4:
        universe = 4
        subsets = [set([1, 2]), set([2, 3]), set([3]), set([1, 4])]
        costs = [2, 3, 1, 5]
    
        return universe, subsets, costs
    
    if i == 5:
        universe = 5
        subsets = [frozenset([1, 2]), frozenset([3, 4]), frozenset([1, 3]), frozenset([2, 4]), frozenset([5])]
        costs = [1, 2, 3, 4, 5]

        return universe, subsets, costs
    
    if i == 6:
        universe = 30

        # Generate random subsets
        num_subsets = 10
        subsets = [frozenset(random.sample(range(1, universe + 1), random.randint(5, 10))) for _ in range(num_subsets)]

        # Generate random costs
        costs = [random.randint(1, 10) for _ in range(num_subsets)]

        return universe, subsets, costs
    
    if i == 7:
        universe = 50

        # Generate random subsets
        num_subsets = 30
        subsets = [frozenset(random.sample(range(1, universe + 1), random.randint(5, 10))) for _ in range(num_subsets)]

        # Generate random costs
        costs = [random.randint(1, 10) for _ in range(num_subsets)]

        return universe, subsets, costs
    
    if i == 8:
        universe = 50
        subsets = [frozenset([i, i+1]) for i in range(1, 51, 2)]
        costs = [1 for _ in range(25)]

        return universe, subsets, costs
    
    if i == 9:
        universe = 100
        subsets = [frozenset([i, i+1]) for i in range(1, 101, 2)]
        costs = [1 for _ in range(50)]

        return universe, subsets, costs