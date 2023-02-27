from scipy.spatial.distance import hamming
import pandas as pd

from Genetic_Algorithm.ga_factory import create_ga
from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.board_utils import to_binary_string
from Utilities.lookup_tables import ALL_SOLUTIONS_LUT

data = {
    'Setting': [],
    'Pop_Size': [],
    'N': [],
    'Num Gens': [],
    'Conv': [],
    'SR_sub': [],
    'SR_opt': [],
    'avg_gens_per_sol': []
}

ga_settings = {
    "standard": [
        {"TM": [.1, .2], "OP": .9, "SN": .03}, {"TM": [.1, .2], "OP": .9, "SR": .03},
        {"TM": [.1, .2], "TP": .9, "SN": .03}, {"TM": [.1, .2], "TP": .9, "SR": .03},
        {"RW": .2, "OP": .9, "SN": .03}, {"RW": .2, "OP": .9, "SR": .03},
        {"RW": .2, "TP": .9, "SN": .03}, {"RW": .2, "TP": .9, "SR": .03}
    ],
    "standard_mc": [
        {"TM": [.1, .2], "OP": .9, "SN": .03, "MC": [.1, 1]}, {"TM": [.1, .2], "OP": .9, "SR": .03, "MC": [.1, 1]},
        {"TM": [.1, .2], "TP": .9, "SN": .03, "MC": [.1, 1]}, {"TM": [.1, .2], "TP": .9, "SR": .03, "MC": [.1, 1]},
        {"RW": .2, "OP": .9, "SN": .03, "MC": [.1, 1]}, {"RW": .2, "OP": .9, "SR": .03, "MC": [.1, 1]},
        {"RW": .2, "TP": .9, "SN": .03, "MC": [.1, 1]}, {"RW": .2, "TP": .9, "SR": .03, "MC": [.1, 1]}
    ],
    "standard_w_mc": [
        {"TM": [.1, .2], "OP": .9, "SR": .03, "MC": [.1, 3]}, {"RW": .2, "OP": .9, "SR": .03, "MC": [.1, 3]}
    ],
    'rw_mc': [
        {"RW": .2, "OP": .9, "SN": .03, "MC": [.1, 8]}, {"RW": .2, "OP": .9, "SR": .03, "MC": [.1, 8]},
        {"RW": .2, "TP": .9, "SN": .03, "MC": [.1, 8]}, {"RW": .2, "TP": .9, "SR": .03, "MC": [.1, 8]}
    ],
    'mc': [
        {"RW": .2, "TP": .9, "SN": .03, "MC": [.5, 12]},
        # {"TM": [.1, .2], "TP": .9, "SN": .03, "MC": [.5, 12]}, {"RW": .2, "TP": .9, "SN": .03, "MC": [.5, 12]}
    ]
}


def run() -> None:
    num_it = 30
    pop_size = 200
    n = 12
    for setting in ga_settings['mc']:
        convergence = 0
        sr_sub = 0
        sr_opt = 0
        gens = []
        avg_gens_per_sol = []
        for i in range(num_it):
            ga = create_ga(setting, pop_size, n)
            ga.run()
            gens.append(ga.generations)
            convergence += calc_convergence(ga)
            if ga.history[-1].contains_sub_optimal_solution():
                sr_sub += 1
            # if ga.history[-1].contains_optimal_solution():
            #     sr_opt += 1
            if len(ga.solutions) == ALL_SOLUTIONS_LUT[n]:
                sr_opt += 1
            print(calc_diversity(ga, pop_size, n))
            if ga.unique_sols > 0:
                avg_gens_per_sol.append(ga.generations)
        data['Setting'].append(setting)
        data['Pop_Size'].append(pop_size)
        data['N'].append(n)
        data['Num Gens'].append(round(sum(gens) / len(gens), 2))
        data['Conv'].append(round(convergence / num_it, 2))
        data['SR_sub'].append(round(sr_sub / num_it, 2))
        data['SR_opt'].append(round(sr_opt / num_it, 2))
        if avg_gens_per_sol:
            data['avg_gens_per_sol'].append(round(sum(avg_gens_per_sol) / len(avg_gens_per_sol), 2))
        else:
            data['avg_gens_per_sol'].append('-')

    df = pd.DataFrame(data)
    df.to_csv('./results/ga_mc_all_sols/mc50p_' + str(n) + '_' + str(pop_size) + '.csv', index=False)
    print(df)


def calc_convergence(ga: GeneticAlgorithm) -> int:
    return 0
    # if ga.stopping_cause == 'converged':
    #     return ga.generations - ga.stagnation_limit
    # elif ga.stopping_cause == 'optimum found':
    #     return 0


def calc_diversity(ga: GeneticAlgorithm, pop_size: int, n: int) -> list:
    avg_hamming_distances = []
    for i in range(0, len(ga.history), 10):
        generation = ga.history[i].genomes
        hamming_distances = []
        for j, k in zip(range(0, pop_size - 1), range(1, pop_size)):
            individual_1 = to_binary_string(generation[j].chromosome, n)
            individual_2 = to_binary_string(generation[k].chromosome, n)
            hamming_distances.append(hamming(list(individual_1), list(individual_2)))
        avg_hd = sum(hamming_distances) / len(hamming_distances)
        avg_hamming_distances.append(round(avg_hd, 2))
    return avg_hamming_distances


if __name__ == '__main__':
    run()
