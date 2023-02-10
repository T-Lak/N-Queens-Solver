import unittest

from Genetic_Algorithm.genome import Genome
from Utilities.board_utils import rotate_90_deg_clockwise
from Utilities.ga_utils import derive_solutions_from
from Utilities.lookup_tables import *


class BitOperationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.bitboard = 0x1E2222120E0A1222
        self.n = 8
        create_attack_lut(self.n)
        create_file_masks(self.n)
        create_rank_masks(self.n)
        create_file_square_lut(self.n)

    def test_vertical_mirroring(self):
        vertically_mirrored = mirror_vertically(self.bitboard, self.n)
        redo_mirroring = mirror_vertically(vertically_mirrored, self.n)
        self.assertEqual(self.bitboard, redo_mirroring)

    def test_horizontal_mirroring(self):
        horizontally_mirrored = mirror_horizontally(self.bitboard, self.n)
        redo_mirroring = mirror_horizontally(horizontally_mirrored, self.n)
        self.assertEqual(self.bitboard, redo_mirroring)

    def test_clockwise_rotation(self):
        valid_bb_90_deg  = 0x00ff888c92610000
        valid_bb_180_deg = 0x4448507048444478
        valid_bb_270_deg = 0x000086493111ff00

        bb_90_deg  = rotate_90_deg_clockwise(self.bitboard, self.n)
        bb_180_deg = rotate_90_deg_clockwise(bb_90_deg, self.n)
        bb_270_deg = rotate_90_deg_clockwise(bb_180_deg, self.n)

        self.assertEqual(valid_bb_90_deg, bb_90_deg)
        self.assertEqual(valid_bb_180_deg, bb_180_deg)
        self.assertEqual(valid_bb_270_deg, bb_270_deg)

    def test_get_total_num_of_solutions_8x8(self):
        unique_solutions = [
            0x0840048002100120, 0x1002084004802001, 0x0802400420801001, 0x0820800401401002,
            0x0420800108401002, 0x1004800840012002, 0x1040080104802002, 0x0801108020044002,
            0x0420080180104002, 0x2002400108801004, 0x0840018010022004, 0x2008400180021004
        ]
        solutions_set = set()
        solutions_set.update(unique_solutions)
        self.assertEqual(len(unique_solutions), len(solutions_set))
        solutions_set.clear()

        for _, solution in enumerate(unique_solutions):
            self.assertEqual(28, Genome(solution, 8).fitness)

        for _, solution in enumerate(unique_solutions):
            subset = derive_solutions_from(solution, 8)
            solutions_set.update(subset)
        self.assertEqual(92, len(solutions_set))


if __name__ == '__main__':
    unittest.main()
