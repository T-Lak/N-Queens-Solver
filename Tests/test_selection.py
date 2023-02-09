import unittest

from Genetic_Algorithm.Operators.selection import RouletteWheel
from Genetic_Algorithm.genome import Genome
from Genetic_Algorithm.population import Population
from Tests.test_crossover import create_parents
from Utilities.lookup_tables import create_file_masks, create_file_square_lut, create_attack_lut


class MyTestCase(unittest.TestCase):

    def test_something(self):
        n = 8
        create_file_masks(n)
        create_attack_lut(n)
        create_file_square_lut(n)
        parents = create_parents(n)
        rw = RouletteWheel(n)
        population = Population(2, n)
        population.genomes = [Genome(parents[0], n), Genome(parents[1], n)]
        rw.compute(population)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
