import unittest

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


if __name__ == '__main__':
    unittest.main()
