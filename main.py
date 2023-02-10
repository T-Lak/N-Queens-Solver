from Utilities.board_utils import display, to_binary_string
from Utilities.lookup_tables import *


if __name__ == '__main__':
    size = 5
    create_attack_lut(size)
    create_file_masks(size)
    create_rank_masks(size)
    create_file_square_lut(size)

    # gen_algo = GeneticAlgorithm(10, size)
    # print(gen_algo.population.genomes)

