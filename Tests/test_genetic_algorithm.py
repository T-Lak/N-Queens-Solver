import unittest

from Genetic_Algorithm.chromosome import Chromosome
from Genetic_Algorithm.genome import Genome
from Utilities.lookup_tables import create_attack_lut


class GeneticAlgorithmTest(unittest.TestCase):

    def test_fitness_evaluation(self):
        n = 8
        ideal_fitness = n * (n - 1) // 2

        create_attack_lut(n)

        chromosome_1 = 0x00000000000000FF
        genome_1 = Genome(chromosome_1, n)

        chromosome_2 = 0x8000000000000001
        genome_2 = Genome(chromosome_2, n)

        chromosome_3 = 0x8000000000040001
        genome_3 = Genome(chromosome_3, n)

        chromosome_4 = 0x0000000000000001
        genome_4 = Genome(chromosome_4, n)

        self.assertEqual(genome_1.fitness, 0)
        self.assertEqual(genome_2.fitness, ideal_fitness - 1)
        self.assertEqual(genome_3.fitness, ideal_fitness - 3)
        self.assertEqual(genome_4.fitness, ideal_fitness)

    def test_chromosome_class(self):
        n = 8
        create_attack_lut(n)

        sequence_1 = 0x4000000000000081
        chromosome = Chromosome(sequence_1, n)
        print(chromosome.genes)
        self.assertEqual([0, 7, 62], chromosome.genes)


if __name__ == '__main__':
    unittest.main()
