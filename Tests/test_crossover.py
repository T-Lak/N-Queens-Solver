import unittest

from Genetic_Algorithm.Operators.crossover import *
from Utilities.lookup_tables import FILE_SQUARE_LUT, create_file_square_lut, create_file_masks


class MyTestCase(unittest.TestCase):

    def test_single_point_crossover_8x8(self):
        n = 8
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(SinglePoint(8))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_single_point_crossover_12x12(self):
        n = 12
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(SinglePoint(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_single_point_crossover_17x17(self):
        n = 17
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(SinglePoint(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_two_point_crossover_8x8(self):
        n = 8
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(TwoPoint(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_two_point_crossover_13x13(self):
        n = 13
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(TwoPoint(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_two_point_crossover_20x20(self):
        n = 20
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(TwoPoint(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_uniform_crossover_8x8(self):
        n = 8
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(Uniform(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_uniform_crossover_11x11(self):
        n = 11
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(Uniform(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])

    def test_uniform_crossover_16x16(self):
        n = 16
        create_file_masks(n)
        create_file_square_lut(n)
        parents = create_parents(n)

        context = CrossoverContext(Uniform(n))
        children = context.execute(parents, 2)

        c1_p1 = children[0] & parents[0]
        c2_p1 = children[1] & parents[0]
        c1_p2 = children[0] & parents[1]
        c2_p2 = children[1] & parents[1]

        self.assertEqual(c1_p1 | c2_p1, parents[0])
        self.assertEqual(c1_p2 | c2_p2, parents[1])


def create_parents(n: int) -> list:
    parents = []
    for _ in range(2):
        bitboard = 0x0
        for i in range(n):
            squares = FILE_SQUARE_LUT.get(i)
            square = random.choice(squares)
            bitboard |= 0x1 << square
        parents.append(bitboard)
    return parents


if __name__ == '__main__':
    unittest.main()
