import unittest

from Genetic_Algorithm.Operators.mutation import *
from Utilities.lookup_tables import create_attack_lut, create_file_masks, create_file_square_lut, FILE_MASK_LUT


class MutationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.n = 8
        self.bb = 0x01120040A8040000
        create_attack_lut(self.n)
        create_file_masks(self.n)
        create_file_square_lut(self.n)

    def test_swap_neighbor(self):
        offset = SwapNeighbor(1, self.n).compute([self.bb])

        for i in range(self.n):
            self.assertEqual(1, bin(self.bb & FILE_MASK_LUT[i]).count("1"))

        self.assertNotEqual(self.bb, offset[0])

    def test_swap_random(self):
        offset = SwapRandom(1, self.n).compute([self.bb])

        for i in range(self.n):
            self.assertEqual(1, bin(self.bb & FILE_MASK_LUT[i]).count("1"))

        self.assertNotEqual(self.bb, offset[0])


if __name__ == '__main__':
    unittest.main()
