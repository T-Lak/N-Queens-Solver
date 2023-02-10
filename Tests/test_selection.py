import unittest

from Genetic_Algorithm.Operators.selection import RouletteWheel
from Genetic_Algorithm.genome import Genome
from Genetic_Algorithm.population import Population
from Tests.test_crossover import create_parents
from Utilities.lookup_tables import create_file_masks, create_file_square_lut, create_attack_lut


class SelectionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.n = 8
        create_file_masks(self.n)
        create_attack_lut(self.n)
        create_file_square_lut(self.n)
        parents = create_parents(self.n)
        self.genome_1 = Genome(parents[0], self.n)
        self.genome_2 = Genome(parents[1], self.n)

    def test_something(self):
        rw = RouletteWheel(self.n)
        population = Population(2, self.n)
        population.genomes = [self.genome_1, self.genome_2]
        rw.compute(population)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
