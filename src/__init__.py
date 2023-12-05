import random

from datetime import timedelta
from timeit import default_timer as timer

from algorithms.greedy import *
from algorithms.brute_force import *
from algorithms.cost_scaling import *
from algorithms.branch_bound import *

from algorithms.test_set import *

if __name__ == "__main__":
    for i in range(0, 7):
        universe, subsets, costs = test_data(i)

        while True:
            try:
                start = timer()
                result = brute_force(universe, subsets, costs)
                end = timer()

                print("Brute Force result: ", result, "Elapsed time: ", timedelta(seconds=end-start), "(", i, ")")

                start = timer()
                result = greedy(universe, subsets, costs)
                end = timer()

                print("Greedy result: ", result, "Elapsed time: ", timedelta(seconds=end-start), "(", i, ")")

                start = timer()
                result = cover_cost_scaling(universe, subsets, costs)
                end = timer()

                print("Approximation by Cost result: ", result, "Elapsed time: ", timedelta(seconds=end-start), "(", i, ")")

                start = timer()
                result = branch_bound(universe, subsets, costs)
                end = timer()

                print("Branch & Bound result: ", result, "Elapsed time: ", timedelta(seconds=end-start), "(", i, ")")

                print("--------------------")
                print("Universe: ", universe)
                print("Subsets: ", subsets)
                print("Costs: ", costs)
                print("----------------------------------------------")
                
                break
            except Exception as e:
                universe = 30

                # Generate random subsets
                num_subsets = 10
                subsets = [frozenset(random.sample(range(1, universe + 1), random.randint(5, 10))) for _ in range(num_subsets)]

                # Generate random costs
                costs = [random.randint(1, 10) for _ in range(num_subsets)]