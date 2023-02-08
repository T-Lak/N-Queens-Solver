from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.lookup_tables import *


if __name__ == '__main__':
    bitboard = 0x0
    size = 8
    create_attack_lut(size)
    create_file_masks(size)
    create_file_square_lut(size)
    gen_algo = GeneticAlgorithm(10, size)
    print(gen_algo.population.genomes)
