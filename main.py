from Genetic_Algorithm.genetic_algorithm import GeneticAlgorithm
from Utilities.lookup_tables import create_attack_lut, create_file_masks, create_rank_masks, create_file_square_lut

if __name__ == '__main__':
    size = 12
    create_attack_lut(size)
    create_file_masks(size)
    create_rank_masks(size)
    create_file_square_lut(size)

    generations = []

    ga = GeneticAlgorithm(250, size)
    ga.run()