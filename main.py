from Genetic_Algorithm.Operators.mutation import Greedy, SwapNeighbor, SwapRandom
from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.board_utils import display, to_binary_string, rotate_90_deg_clockwise
from Utilities.lookup_tables import *


if __name__ == '__main__':
    bitboard = 0x0
    size = 8
    create_attack_lut(size)
    create_file_masks(size)
    create_rank_masks(size)
    create_file_square_lut(size)
    # gen_algo = GeneticAlgorithm(10, size)
    # print(gen_algo.population.genomes)
    # bb = 0x01120040A8040000
    # l = SwapRandom(1, size).compute([bb])

    sq = 0x1E2222120E0A1222
    bb_1 = rotate_90_deg_clockwise(sq, size)
    bb_2 = rotate_90_deg_clockwise(bb_1, size)
    bb_3 = rotate_90_deg_clockwise(bb_2, size)
    # print(bb_1, bb_2, bb_3)
    # bb_3 = rotate_270_deg_clockwise(sq)
    # sq = (((sq * 0x20800000) & (2**32 - 1)) >> 26) ^ 56
    display(to_binary_string(0x4448507048444478, size))
    # display(to_binary_string(sq, size))
    # display(to_binary_string(bb_1, size))
    # display(to_binary_string(bb_2, size))
    # display(to_binary_string(bb_3, size))
    # display(to_binary_string(bb_3, size))
