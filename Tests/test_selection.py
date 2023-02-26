import unittest

from Genetic_Algorithm.Operators.selection import RouletteWheel, Tournament
from Genetic_Algorithm.population import Population
from Utilities.lookup_tables import create_file_masks, create_file_square_lut, create_attack_lut, create_rank_masks


class SelectionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.rates = [.1, .2, .3, .4, .5, .6, .7, .8, .9]
        self.n = 8

        create_attack_lut(self.n)
        create_file_masks(self.n)
        create_rank_masks(self.n)
        create_file_square_lut(self.n)

        self.population_100 = Population(100)
        self.population_100.populate(self.n)
        self.population_200 = Population(200)
        self.population_200.populate(self.n)
        self.population_300 = Population(300)
        self.population_300.populate(self.n)

    def test_roulette_wheel_selection(self):

        for rate in self.rates:
            rw = RouletteWheel(rate)
            parents_1 = rw.compute(self.population_100)
            parents_2 = rw.compute(self.population_200)
            parents_3 = rw.compute(self.population_300)

            print([g.fitness for g in parents_1])
            print(self.population_100.worst().fitness, self.population_100.fittest().fitness)

            self.assertEqual(int(self.population_100.size * rate), len(parents_1))
            self.assertEqual(int(self.population_200.size * rate), len(parents_2))
            self.assertEqual(int(self.population_300.size * rate), len(parents_3))

    def test_tournament_selection(self):
        for rate in self.rates:
            tm = Tournament(10, rate)

            parents_1 = tm.compute(self.population_100)
            parents_2 = tm.compute(self.population_200)
            parents_3 = tm.compute(self.population_300)

            self.assertEqual(int(self.population_100.size * rate), len(parents_1))
            self.assertEqual(int(self.population_200.size * rate), len(parents_2))
            self.assertEqual(int(self.population_300.size * rate), len(parents_3))


if __name__ == '__main__':
    unittest.main()
