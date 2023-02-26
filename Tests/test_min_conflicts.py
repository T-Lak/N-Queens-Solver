import unittest

from Genetic_Algorithm.Operators.min_conflicts import MinConflicts
from Genetic_Algorithm.population import Population
from Utilities.lookup_tables import create_attack_lut, create_file_masks, create_rank_masks, create_file_square_lut


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.size = 8

        create_attack_lut(self.size)
        create_file_masks(self.size)
        create_rank_masks(self.size)
        create_file_square_lut(self.size)

        self.population = Population(1000)
        self.population.populate(self.size)

    def test_something(self):
        mc = MinConflicts(1., 1, self.size)
        chromosomes = [g.chromosome for g in self.population.genomes]

        for c in chromosomes:
            new_c = mc.execute([c])[0]
            self.assertEqual(self.size, bin(new_c).count("1"))
            self.assertNotEqual(c, new_c)


if __name__ == '__main__':
    unittest.main()
